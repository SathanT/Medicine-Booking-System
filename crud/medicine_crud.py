from sqlalchemy.orm import Session

from models.medicine import MedicineDB, ManufacturerDB, CatogoryDB
from schemas.medicine import MedicineCreate, MedicineUpdate
from schemas.manufacturer import ManufacturerCreate, ManufacturerUpdate
from schemas.catogory import CatogoryCreate, CatogoryUpdate
from custom_exception.dbexception import DatabaseException


# ------------------ CREATE ------------------

def create_medicine(db: Session, medicine: MedicineCreate):
    try:
        new_medicine = MedicineDB(
            name=medicine.name,
            description=medicine.description,
            price=medicine.price,
            stock=medicine.stock,
        )
        db.add(new_medicine)
        db.commit()
        db.refresh(new_medicine)
        return new_medicine

    except Exception as e:
        db.rollback()
        raise DatabaseException()


def create_manufacturer(db: Session, medicine_id: int, data: ManufacturerCreate):
    try:
        manufacturer = ManufacturerDB(
            name=data.name,
            email=data.email,
            phone_no=data.phone_no,
            medicine_id=medicine_id,
        )
        db.add(manufacturer)
        db.commit()
        db.refresh(manufacturer)
        return manufacturer

    except Exception as e:
        db.rollback()
        raise DatabaseException()


def create_category(db: Session, medicine_id: int, data: CatogoryCreate):
    try:
        catogory = CatogoryDB(
            catogory=data.catogory,
            medicine_id=medicine_id,
        )
        db.add(catogory)
        db.commit()
        db.refresh(catogory)
        return catogory

    except Exception as e:
        db.rollback()
        raise DatabaseException()


# ------------------ READ ------------------

def get_medicine_by_id(db: Session, medicine_id: int):
    try:
        return db.query(MedicineDB).filter(MedicineDB.id == medicine_id).first()
    except Exception as e:
        print(str(e))


def get_all_medicines(db: Session):
    try:
        return db.query(MedicineDB).all()
    except Exception as e:
        print(str(e))


def get_manufacturers_by_medicine(db: Session, medicine_id: int):
    try:
        return db.query(ManufacturerDB).filter(ManufacturerDB.medicine_id == medicine_id).all()
    except Exception as e:
        print(str(e))


def get_categories_by_medicine(db: Session, medicine_id: int):
    try:
        return db.query(CatogoryDB).filter(CatogoryDB.medicine_id == medicine_id).all()
    except Exception as e:
        print(str(e))


# ------------------ UPDATE ------------------

def update_medicine(db: Session, medicine_id: int, data: MedicineUpdate):
    try:
        medicine = db.query(MedicineDB).filter(MedicineDB.id == medicine_id).first()

        if not medicine:
            return None

        update_data = data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(medicine, key, value)

        db.commit()
        db.refresh(medicine)
        return medicine

    except Exception as e:
        db.rollback()
        raise DatabaseException()


def update_manufacturer(db: Session, manufacturer_id: int, data: ManufacturerUpdate):
    try:
        manufacturer = db.query(ManufacturerDB).filter(ManufacturerDB.id == manufacturer_id).first()

        if not manufacturer:
            return None

        update_data = data.model_dump(exclude_unset=True,exclude_none=True)

        for key, value in update_data.items():
            setattr(manufacturer, key, value)

        db.commit()
        db.refresh(manufacturer)
        return manufacturer

    except Exception as e:
        db.rollback()
        raise DatabaseException()


def update_category(db: Session, category_id: int, data: CatogoryUpdate):
    try:
        category = db.query(CatogoryDB).filter(CatogoryDB.id == category_id).first()

        if not category:
            return None

        update_data = data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(category, key, value)

        db.commit()
        db.refresh(category)
        return category

    except Exception as e:
        db.rollback()
        raise DatabaseException()


# ------------------ DELETE ------------------

def delete_medicine(db: Session, medicine_id: int):
    try:
        medicine = db.query(MedicineDB).filter(MedicineDB.id == medicine_id).first()

        if not medicine:
            return None

        db.delete(medicine)
        db.commit()

        return {"message": "Medicine deleted successfully"}

    except Exception as e:
        db.rollback()
        raise DatabaseException()


def delete_manufacturer(db: Session, manufacturer_id: int):
    try:
        manufacturer = db.query(ManufacturerDB).filter(ManufacturerDB.id == manufacturer_id).first()

        if not manufacturer:
            return None

        db.delete(manufacturer)
        db.commit()

        return {"message": "Manufacturer deleted successfully"}

    except Exception as e:
        db.rollback()
        raise DatabaseException()


def delete_category(db: Session, category_id: int):
    try:
        category = db.query(CatogoryDB).filter(CatogoryDB.id == category_id).first()

        if not category:
            return None

        db.delete(category)
        db.commit()

        return {"message": "Category deleted successfully"}

    except Exception as e:
        db.rollback()
        raise DatabaseException()
