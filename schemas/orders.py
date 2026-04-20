from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from enums.orderstatus import Status


class OrderBase(BaseModel):
    user_id: int
    status: Status
    created_at: datetime


class OrderCreate(OrderBase):
    pass


class OrderUpdate:
    status: Optional[Status] = None


class OrderResponse(OrderBase):
    id: int

    class Config:
        orm_mode = True
