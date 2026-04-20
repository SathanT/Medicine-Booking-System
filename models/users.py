from sqlalchemy import Column, String, Integer, ForeignKey, Enum as sqlEnum
from sqlalchemy.orm import relationship

from db.base import Base
from enums.roles import Role


class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String, unique=True,nullable=False)
    password = Column(String, nullable=False)
    role = Column(sqlEnum(Role), default=Role.CUSTOMER)
    address = relationship("AddressDB", back_populates="user",cascade="all, delete")


class AddressDB(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    door_no = Column(String, nullable=False)
    street = Column(String, nullable=False)
    city = Column(String, nullable=False)
    district = Column(String, nullable=False)
    state = Column(String, nullable=False)
    user_id=Column(Integer,ForeignKey("users.id", ondelete="CASCADE"))
    user = relationship("UserDB", back_populates="address")
