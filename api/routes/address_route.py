from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.sessions import get_db
from schemas.address import AddressCreate, AddressUpdate, AddressResponse
from service.user_service import *

router = APIRouter(prefix="/addresses", tags=["Addresses"])


# ------------------ CREATE ------------------
@router.post("/user/{user_id}", response_model=AddressResponse)
def create_address_ep(
    user_id: int,
    data: AddressCreate,
    db: Session = Depends(get_db)
):
    return create_address_service(db, user_id, data)


# ------------------ GET BY ID ------------------
@router.get("/{address_id}", response_model=AddressResponse)
def get_address_ep(
    address_id: int,
    db: Session = Depends(get_db)
):
    return get_address_service(db, address_id)


# ------------------ GET ALL ADDRESSES OF USER ------------------
@router.get("/user/{user_id}", response_model=list[AddressResponse])
def get_user_addresses_ep(
    user_id: int,
    db: Session = Depends(get_db)
):
    return get_user_addresses_service(db, user_id)


# ------------------ UPDATE ------------------
@router.patch("/{address_id}", response_model=AddressResponse)
def update_address_ep(
    address_id: int,
    data: AddressUpdate,
    db: Session = Depends(get_db)
):
    return update_address_service(db, address_id, data)


# ------------------ DELETE ------------------
@router.delete("/{address_id}")
def delete_address_ep(
    address_id: int,
    db: Session = Depends(get_db)
):
    return delete_address_service(db, address_id)
