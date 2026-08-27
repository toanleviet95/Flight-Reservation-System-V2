# Định nghĩa bảng DB (SQLModel table)

from typing import Optional
from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True, alias="user_id")
    full_name: Optional[str] = Field(default=None, max_length=255, alias="full_name")
    email: Optional[str] = Field(default=None, max_length=255)
    password_hash: Optional[str] = Field(default=None, max_length=255, alias="password_hash")
    phone: Optional[str] = Field(default=None, max_length=255)
    auth_provider: Optional[str] = Field(default=None, max_length=255, alias="auth_provider")