# Định nghĩa hình dạng dữ liệu vào/ra API (Pydantic)

from pydantic import BaseModel, ConfigDict


# --- Request schemas ---

class UserCreate(BaseModel):
    """Schema nhận dữ liệu từ client khi đăng ký."""
    fullname: str
    email: str
    password: str
    phone: str
    authprovider: str

class UserLogin(BaseModel):
    """Schema nhận dữ liệu từ client khi đăng nhập."""
    email: str
    password: str


# --- Response schemas ---

class UserRead(BaseModel):
    """Schema trả về cho client — không lộ passwordhash."""
    user_id: int
    full_name: str
    email: str

    model_config = ConfigDict(from_attributes=True)
