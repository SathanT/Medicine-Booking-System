from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from crud import user_crud
from schemas.user import UserCreate, UserUpdate
from schemas.address import AddressCreate, AddressUpdate
from custom_exception.user import *


# ------------------ USER SERVICES ------------------

def create_user_service(db: Session, data: UserCreate):
    # Business validation
    existing_user = user_crud.get_user_by_email(db, data.email)
    if existing_user:
        raise UserAlreadyExistsException()

    return user_crud.create_user(db, data)


def get_user_by_id_service(db: Session, user_id: int):
    user = user_crud.get_user_by_id(db, user_id)

    if not user:
        raise UserNotFoundException()

    return user


def get_user_by_email_service(db: Session, user_email: str):
    user = user_crud.get_user_by_email(db, user_email)

    if not user:
        raise UserNotFoundException()

    return user


def update_user_service(db: Session, user_id: int, data: UserUpdate):
    user = user_crud.update_user(db, user_id, data)

    if not user:
        raise UserNotFoundException()

    return user


def delete_user_service(db: Session, user_id: int):
    user = user_crud.get_user_by_id(db, user_id)

    if not user:
        raise UserNotFoundException()

    user_crud.delete_user(db, user_id)

    return {"message": "User deleted successfully"}


# ------------------ ADDRESS SERVICES ------------------

def create_address_service(db: Session, user_id: int, data: AddressCreate):
    # Ensure user exists
    user = user_crud.get_user_by_id(db, user_id)

    if not user:
        raise UserNotFoundException()

    return user_crud.create_address(db, user_id, data)


def get_address_service(db: Session, address_id: int):
    address = user_crud.get_address_by_id(db, address_id)

    if not address:
        raise AddressNotFoundException()

    return address


def get_user_addresses_service(db: Session, user_id: int):
    # Optional: validate user exists
    user = user_crud.get_user_by_id(db, user_id)

    if not user:
        raise UserNotFoundException()

    return user_crud.get_all_address_by_user_id(db, user_id)


def update_address_service(db: Session, address_id: int, data: AddressUpdate):
    address = user_crud.update_address(db, address_id, data)

    if not address:
        raise AddressNotFoundException()

    return address


def delete_address_service(db: Session, address_id: int):
    address = user_crud.get_address_by_id(db, address_id)

    if not address:
        raise AddressNotFoundException()

    user_crud.delete_address(db, address_id)

    return {"message": "Address deleted successfully"}