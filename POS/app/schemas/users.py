from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    full_name: str
    email: EmailStr
    role: str


class UserCreate(UserBase):
    password_hash: str


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[str] = None
    password_hash: Optional[str] = None


class UserResponse(UserBase):
    user_id: int

    class Config:
        from_attributes = True
