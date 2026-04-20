from pydantic import BaseModel
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

    class Config:
        orm_mode=True