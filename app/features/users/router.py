# Chỉ định nghĩa endpoint, nhận request, gọi service, trả response
from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.db.session import get_session
from .schemas import UserCreate, UserRead, UserLogin
from . import service

router = APIRouter(
    prefix="/users",
    tags=["Users"]
) # Nơi khai báo các route

@router.post("/register",response_model=UserRead)
def register(user_in: UserCreate, session: Session = Depends(get_session)):
    return service.register_user(session, user_in)

@router.post("/login",response_model=UserRead)
def login(credentials: UserLogin, session: Session = Depends(get_session)):
    return service.authenticate_user(session, credentials)
