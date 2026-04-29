from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from db.sessions import get_db
from schemas.medicine import MedicineCreate, MedicineUpdate, MedicineResponse
from service.medicine_service import *

router = APIRouter(prefix="/medicines", tags=["Medicines"])


@router.post("/", response_model=MedicineResponse, status_code=status.HTTP_201_CREATED)
def create_medicine_ep(
    data: MedicineCreate,
    db: Session = Depends(get_db)
):
    return create_medicine_service(db, data)


@router.get("/{medicine_id}", response_model=MedicineResponse)
def get_medicine_ep(
    medicine_id: int,
    db: Session = Depends(get_db)
):
    return get_medicine_service(db, medicine_id)


@router.get("/", response_model=list[MedicineResponse])
def get_all_medicine_ep(
    db: Session = Depends(get_db)
):
    return get_all_medicine_service(db)


@router.put("/{medicine_id}", response_model=MedicineResponse)
def update_medicine_ep(
    medicine_id: int,
    data: MedicineUpdate,
    db: Session = Depends(get_db)
):
    return update_medicine_service(db, medicine_id, data)


@router.delete("/{medicine_id}")
def delete_medicine_ep(
    medicine_id: int,
    db: Session = Depends(get_db)
):
    return delete_medicine_service(db, medicine_id)
