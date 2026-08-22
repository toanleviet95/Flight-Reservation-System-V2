"""UserRepository — data-access layer for the User entity."""

from sqlmodel import Session, select
from app.features.users.models import User


class UserRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_all(self, offset: int = 0, limit: int = 100) -> list[User]:
        return list(self.session.exec(select(User).offset(offset).limit(limit)).all())

    def get_by_id(self, user_id: int) -> User | None:
        return self.session.get(User, user_id)

    def get_by_email(self, email: str) -> User | None:
        return self.session.exec(select(User).where(User.email == email)).first()
