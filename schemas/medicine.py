from pydantic import BaseModel
from typing import Optional,List

from manufacturer import ManufacturerResponse
from catogory import CatogoryResponse

class MedicineBase(BaseModel):
    name: str
    description: str
    price: int
    stock: int


class MedicineCreate(MedicineBase):
    pass


class MedicineUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None
    stock: Optional[int] = None


class MedicineResponse(MedicineBase):
    id: int

    class Config:
        orm_mode = True

class MedicineFullResponse(MedicineResponse):
    man=List[ManufacturerResponse]
    cg=List[CatogoryResponse]
