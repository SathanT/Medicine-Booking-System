from pydantic import BaseModel,EmailStr
from typing import Optional

class ManufacturerBase(BaseModel):
    name : str
    email : EmailStr
    phone_no : str

class ManufacturerCreate(ManufacturerBase):
    pass

class ManufacturerUpdate(BaseModel):
    name : Optional[str] = None
    email : Optional[EmailStr] = None
    phone_no : Optional[str] = None

class ManufacturerResponse(ManufacturerBase):
    id : int

    class Config:
        orm_mode=True