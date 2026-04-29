from pydantic import BaseModel, ConfigDict
from typing import Optional

from enums.roles import Role

class UserBase(BaseModel):
    name: str
    email: str
    age: int
    role : Role


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    password: Optional[str] =  None


class UserResponse(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
