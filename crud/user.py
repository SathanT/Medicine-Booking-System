from sqlalchemy import Session

from models.users import UserDB, AddressDB
from schemas.user import UserCreate, UserUpdate
from schemas.address import AddressCreate, AddressUpdate


def create_user(db: Session, user: UserCreate):
    try:
        new_user = UserDB(
            name=user.name,
            age=user.age,
            email=user.email,
            password=user.password,
            role=user.role,
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user
    except Exception as e:
        print(str(e))


def create_address(db: Session, userId: int, address: AddressCreate):
    try:
        address = AddressDB(
            door_no=address.door_no,
            street=address.street,
            city=address.city,
            district=address.district,
            state=address.state,
            user_id=userId,
        )
        db.add(address)
        db.commit()
        db.refresh(address)
    except Exception as e:
        print(str(e))


def get_user_by_id(db: Session, user_id: int):
    try:
        user = db.query(UserDB).filter(UserDB.id == user_id).all()
        return user
    except Exception as e:
        print(str(e))


def get_user_by_email(db: Session, user_email: str):
    try:
        user = db.query(UserDB).filter(UserDB.emai == user_email).all()
        return user
    except Exception as e:
        print(str(e))


def get_address_by_id(db: Session, add_id: int):
    try:
        address = db.query(AddressDB).filter(AddressDB.id == add_id).all()
        return address
    except Exception as e:
        print(str(e))


def get_all_address_by_user_id(db: Session, user_id: int):
    try:
        addresses = db.query(AddressDB).filter(AddressDB.user_id == user_id).all()
        return addresses
    except Exception as e:
        print(str(e))


def update_user(db: Session, user_id: int, data: UserUpdate):
    try:
        user = db.query(UserDB).filter(UserDB.id == user_id).first()
        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data:
            setattr(user, key, value)
        db.commit()
        db.refresh(user)
        return user
    except Exception as e:
        print(str(e))


def update_address(db: Session, address_id: int, data: AddressUpdate):
    try:
        address = db.query(AddressDB).filter(AddressDB.id == address_id).first()
        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data:
            setattr(address, key, value)
        db.commit()
        db.refresh(address)
        return address
    except Exception as e:
        print(str(e))


def delete_user(db: Session, user_id: int):
    try:
        user = db.query(UserDB).filter(UserDB.id == user_id).first()
        db.delete(user)
        db.commit()
    except Exception as e:
        print(str(e))


def delete_address(db: Session, address_id: int):
    try:
        address = db.query(AddressDB).filter(AddressDB.id == address_id).first()
        db.delete(address)
        db.commit()
    except Exception as e:
        print(str(e))
