from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from db.sessions import get_db
from schemas.catogory import CatogoryCreate, CatogoryUpdate, CatogoryResponse
from service.medicine_service import *

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post("/medicine/{medicine_id}", response_model=CatogoryResponse, status_code=status.HTTP_201_CREATED)
def create_category_ep(
    medicine_id: int,
    data: CatogoryCreate,
    db: Session = Depends(get_db)
):
    return create_category_service(db, medicine_id, data)


@router.get("/medicine/{medicine_id}", response_model=list[CatogoryResponse])
def get_categories_by_medicine_ep(
    medicine_id: int,
    db: Session = Depends(get_db)
):
    return get_categories_by_medicine_service(db, medicine_id)


@router.put("/{category_id}", response_model=CatogoryResponse)
def update_category_ep(
    category_id: int,
    data: CatogoryUpdate,
    db: Session = Depends(get_db)
):
    return update_category_service(db, category_id, data)


@router.delete("/{category_id}")
def delete_category_ep(
    category_id: int,
    db: Session = Depends(get_db)
):
    return delete_category_service(db, category_id)
