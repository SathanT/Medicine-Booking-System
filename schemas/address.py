from pydantic import BaseModel, ConfigDict
from typing import List, Optional

from schemas.user import UserResponse


class AddressBase(BaseModel):
    door_no: int
    street: str
    city: str
    district: str
    state: str


class AddressCreate(AddressBase):
    pass


class AddressUpdate(BaseModel):
    door_no: Optional[int] = None
    street: Optional[str] = None
    city: Optional[str] = None
    district: Optional[str] = None
    state: Optional[str] = None


class AddressResponse(AddressBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class UserWithAddress(UserResponse):
    address: List[AddressResponse]
