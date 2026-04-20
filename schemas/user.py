from pydantic import BaseModel, EmailStr
from typing import Optional

from enums.roles import Role

class UserBase(BaseModel):
    name: str
    email: EmailStr
    age: int
    role : Role


class UserCreate(UserBase):
    password: int


class UserUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    password: Optional[str] =  None


class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
