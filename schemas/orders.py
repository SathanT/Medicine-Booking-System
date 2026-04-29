from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

from enums.orderstatus import Status


class OrderBase(BaseModel):
    status: Status
    created_at: datetime


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    status: Optional[Status] = None


class OrderResponse(OrderBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
