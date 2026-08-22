"""UserService — business-logic layer for users."""

from fastapi import HTTPException, status
from sqlmodel import Session

from app.features.users.repository import UserRepository
from app.features.users.models import User


class UserService:
    def __init__(self, session: Session) -> None:
        self.repo = UserRepository(session)

    def get_user(self, user_id: int) -> User:
        user = self.repo.get_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User {user_id} not found",
            )
        return user

    def list_users(self, offset: int = 0, limit: int = 100) -> list[User]:
        return self.repo.get_all(offset=offset, limit=limit)
