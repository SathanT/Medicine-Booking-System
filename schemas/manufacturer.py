from pydantic import BaseModel, ConfigDict
from typing import Optional

class ManufacturerBase(BaseModel):
    name : str
    email : str
    phone_no : str

class ManufacturerCreate(ManufacturerBase):
    pass

class ManufacturerUpdate(BaseModel):
    name : Optional[str] = None
    email : Optional[str] = None
    phone_no : Optional[str] = None

class ManufacturerResponse(ManufacturerBase):
    id : int
    model_config = ConfigDict(from_attributes=True)
