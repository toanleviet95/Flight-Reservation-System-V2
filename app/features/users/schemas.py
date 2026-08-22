"""User request/response schemas."""

from sqlmodel import SQLModel, Field


class UserBase(SQLModel):
    full_name: str | None = Field(default=None, max_length=255)
    email: str = Field(max_length=255)
    is_active: bool = True
    is_superuser: bool = False


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    user_id: int


class UserUpdate(SQLModel):
    full_name: str | None = None
    email: str | None = None
    password: str | None = None
    is_active: bool | None = None
