from sqlalchemy.orm import Session

from crud import medicine_crud
from schemas.medicine import MedicineCreate, MedicineUpdate
from schemas.manufacturer import ManufacturerCreate, ManufacturerUpdate
from schemas.catogory import CatogoryCreate, CatogoryUpdate
from fastapi import HTTPException, status
from custom_exception.medicine import *


# ------------------ MEDICINE SERVICES ------------------

def create_medicine_service(db: Session, data: MedicineCreate):
    # Business validation
    if data.price <= 0:
        raise InvalidPriceException()

    if data.stock < 0:
        raise InvalidStockException()

    return medicine_crud.create_medicine(db, data)


def get_medicine_service(db: Session, medicine_id: int):
    medicine = medicine_crud.get_medicine_by_id(db, medicine_id)

    if not medicine:
        raise MedicineNotFoundException()

    return medicine


def get_all_medicine_service(db: Session):
    return medicine_crud.get_all_medicines(db)


def update_medicine_service(db: Session, medicine_id: int, data: MedicineUpdate):
    medicine = medicine_crud.update_medicine(db, medicine_id, data)

    if not medicine:
        raise MedicineNotFoundException()

    return medicine


def delete_medicine_service(db: Session, medicine_id: int):
    result = medicine_crud.delete_medicine(db, medicine_id)

    if not result:
        raise MedicineNotFoundException()

    return result


# ------------------ MANUFACTURER SERVICES ------------------

def create_manufacturer_service(db: Session, medicine_id: int, data: ManufacturerCreate):
    # Ensure parent exists
    medicine = medicine_crud.get_medicine_by_id(db, medicine_id)
    if not medicine:
        raise MedicineNotFoundException()

    return medicine_crud.create_manufacturer(db, medicine_id, data)


def update_manufacturer_service(db: Session, manufacturer_id: int, data: ManufacturerUpdate):
    manufacturer = medicine_crud.update_manufacturer(db, manufacturer_id, data)

    if not manufacturer:
        raise ManufacturerNotFoundException()

    return manufacturer


def delete_manufacturer_service(db: Session, manufacturer_id: int):
    result = medicine_crud.delete_manufacturer(db, manufacturer_id)

    if not result:
        raise ManufacturerNotFoundException

    return result


def get_manufacturers_by_medicine_service(db: Session, medicine_id: int):
    return medicine_crud.get_manufacturers_by_medicine(db, medicine_id)


# ------------------ CATEGORY SERVICES ------------------

def create_category_service(db: Session, medicine_id: int, data: CatogoryCreate):
    medicine = medicine_crud.get_medicine_by_id(db, medicine_id)
    if not medicine:
        raise MedicineNotFoundException()

    return medicine_crud.create_category(db, medicine_id, data)


def update_category_service(db: Session, category_id: int, data: CatogoryUpdate):
    category = medicine_crud.update_category(db, category_id, data)

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    return category


def delete_category_service(db: Session, category_id: int):
    result = medicine_crud.delete_category(db, category_id)

    if not result:
        raise CategoryNotFoundException()

    return result


def get_categories_by_medicine_service(db: Session, medicine_id: int):
    return medicine_crud.get_categories_by_medicine(db, medicine_id)