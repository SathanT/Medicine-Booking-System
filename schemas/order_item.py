from pydantic import BaseModel, ConfigDict
from typing import Optional

class OrderItemBase(BaseModel):
    order_id : int
    medicine_id : int
    quantity : int
    price : int

class OrderItemCreate(OrderItemBase):
    pass

class OrderItemUpdate(BaseModel):
    quantity : Optional[int] = None
    price : Optional[int] = None

class OrderItemResponse(OrderItemBase):
    id : int
    model_config = ConfigDict(from_attributes=True)
