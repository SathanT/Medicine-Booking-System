from pydantic import BaseModel
from typing import List, Optional

from user import UserResponse


class AddressBase(BaseModel):
    door_no: int
    street: str
    city: str
    district: str
    state: str


class AddressCreate(AddressBase):
    pass


class AddressUpdate(BaseModel):
    door_no: Optional[int]
    street: Optional[str]
    city: Optional[str]
    district: Optional[str]
    state: Optional[str]


class AddressResponse(AddressBase):
    id: int

    class Config:
        orm_mode = True


class UserWithAddress(UserResponse):
    address: List[AddressResponse]
