from pydantic import BaseModel, ConfigDict
from typing import Optional,List

from schemas.manufacturer import ManufacturerResponse
from schemas.catogory import CatogoryResponse

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
    model_config = ConfigDict(from_attributes=True)

class MedicineFullResponse(MedicineResponse):
    man: List[ManufacturerResponse]
    cg: List[CatogoryResponse]
