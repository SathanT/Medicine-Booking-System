from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from db.sessions import get_db
from schemas.manufacturer import ManufacturerCreate, ManufacturerUpdate, ManufacturerResponse
from service.medicine_service import *

router = APIRouter(prefix="/manufacturers", tags=["Manufacturers"])


@router.post("/medicine/{medicine_id}", response_model=ManufacturerResponse, status_code=status.HTTP_201_CREATED)
def create_manufacturer_ep(
    medicine_id: int,
    data: ManufacturerCreate,
    db: Session = Depends(get_db)
):
    return create_manufacturer_service(db, medicine_id, data)


@router.get("/medicine/{medicine_id}", response_model=list[ManufacturerResponse])
def get_manufacturers_by_medicine_ep(
    medicine_id: int,
    db: Session = Depends(get_db)
):
    return get_manufacturers_by_medicine_service(db, medicine_id)


@router.put("/{manufacturer_id}", response_model=ManufacturerResponse)
def update_manufacturer_ep(
    manufacturer_id: int,
    data: ManufacturerUpdate,
    db: Session = Depends(get_db)
):
    return update_manufacturer_service(db, manufacturer_id, data)


@router.delete("/{manufacturer_id}")
def delete_manufacturer_ep(
    manufacturer_id: int,
    db: Session = Depends(get_db)
):
    return delete_manufacturer_service(db, manufacturer_id)
