from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from service.user_service import *
from schemas.user import *
from db.sessions import get_db

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse)
def create_user_ep(user: UserCreate, db: Session = Depends(get_db)):
    return create_user_service(db, user)


@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id_ep(user_id: int, db: Session = Depends(get_db)):
    return get_user_by_id_service(db, user_id)


@router.get("/email/{user_email}", response_model=UserResponse)
def get_user_by_email_ep(user_email: str, db: Session = Depends(get_db)):
    return get_user_by_email_service(db, user_email)


@router.put("/{user_id}", response_model=UserResponse)
def update_user_ep(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return update_user_service(db, user_id, user)


@router.delete("/{user_id}")
def delete_user_ep(user_id: int, db: Session = Depends(get_db)):
    return delete_user_service(db, user_id)
