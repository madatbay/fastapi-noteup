from typing import Optional
from pydantic import BaseModel, EmailStr, validator
from email_validator import validate_email, EmailNotValidError


class UserBase(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    is_superuser: bool = False

    @validator('email')
    def email_validator(cls, v):
        try:
            valid = validate_email(v)
            return valid.email
        except EmailNotValidError:
            raise EmailNotValidError 


class UserCreate(UserBase):
    email: EmailStr
    password: str

class UserUpdate(UserBase):
    pass

class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

class User(UserInDBBase):
    pass