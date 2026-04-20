from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship

from db.base import Base


class MedicineDB(Base):
    __tablename__ = "medicines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)
    manfact = relationship(
        "manufacturers", back_populates="medicine", cascade="all, delete"
    )
    cg = relationship("catogories", back_populates="medicine", cascade="all, delete")


class ManufacturerDB(Base):
    __tablename__ = "manufacturers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone_no = Column(String, nullable=False)
    medicine_id = Column(Integer, ForeignKey("medicines.id", ondelete="CASCADE"))
    medicine = relationship("medicines", back_populates="manfact")


class CatogoryDB(Base):
    __tablename__ = "catogories"

    id = Column(Integer, primary_key=True, index=True)
    catogory = Column(String, nullable=False)
    medicine_id = Column(Integer, ForeignKey("medicines.id", ondelete="CASCADE"))
    medicine = relationship("medicines", back_populates="cg")
