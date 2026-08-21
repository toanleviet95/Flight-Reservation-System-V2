"""User DB table model."""

from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    user_id: int | None = Field(default=None, primary_key=True)
    full_name: str | None = Field(default=None, max_length=255)
    email: str = Field(unique=True, index=True, max_length=255)
    hashed_password: str
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)
