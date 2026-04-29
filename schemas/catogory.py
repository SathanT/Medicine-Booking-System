from pydantic import BaseModel, ConfigDict
from typing import Optional


class CatogoryBase(BaseModel):
    catogory: str


class CatogoryCreate(CatogoryBase):
    pass


class CatogoryUpdate(BaseModel):
    catogory: Optional[str] = None


class CatogoryResponse(CatogoryBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
