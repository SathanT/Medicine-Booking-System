from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship

from db.base import Base


class MedicineDB(Base):
    __tablename__ = "medicines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    price = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)
    manfact = relationship(
        "ManufacturerDB", back_populates="medicine", cascade="all, delete"
    )
    cg = relationship("CatogoryDB", back_populates="medicine", cascade="all, delete")


class ManufacturerDB(Base):
    __tablename__ = "manufacturers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    phone_no = Column(String(255), nullable=False)
    medicine_id = Column(Integer, ForeignKey("medicines.id", ondelete="CASCADE"))
    medicine = relationship("MedicineDB", back_populates="manfact")


class CatogoryDB(Base):
    __tablename__ = "catogories"

    id = Column(Integer, primary_key=True, index=True)
    catogory = Column(String(255), nullable=False)
    medicine_id = Column(Integer, ForeignKey("medicines.id", ondelete="CASCADE"))
    medicine = relationship("MedicineDB", back_populates="cg")
