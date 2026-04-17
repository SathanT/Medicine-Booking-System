from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum as sqlEnum
from sqlalchemy.orm import relationship

from db.base import Base
from enums.orderstatus import Status


class OrderDB(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    status = Column(sqlEnum(Status), nullable=False)
    created_at = Column(DateTime, nullable=False)
    oi = relationship("OrderItemDB", back_populates="order")


class OrderItemDB(Base):
    __tablename__ = "orderitem"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"))
    medicine_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    order = relationship("OrderDB", back_populates="oi")
