# Chứa logic nghiệp vụ
from fastapi import HTTPException
from sqlmodel import Session
from passlib.context import CryptContext

from .models import User
from .schemas import UserCreate, UserLogin
from . import repository

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

def register_user(session: Session, user_in: UserCreate) -> User:
    if repository.get_by_email(session, user_in.email):
        raise HTTPException(status_code=409, detail="Email already exists")

    user = User(
        full_name=user_in.fullname,
        email=user_in.email,
        password_hash=password_hash(user_in.password),
        phone=user_in.phone,
        auth_provider=user_in.authprovider
    )

    return repository.create_user(session, user)

def authenticate_user(session: Session, credentials: UserLogin) -> User:
    user = repository.get_by_email(session, credentials.email)
    if not user or not verify_password(credentials.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user