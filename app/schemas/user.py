import email
from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    is_superuser: bool = False

class UserCreate(UserBase):
    email: EmailStr

class UserUpdate(UserBase):
    pass

class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

class User(UserInDBBase):
    pass