from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from crud import order_crud, medicine_crud, user_crud
from schemas.orders import OrderCreate, OrderUpdate
from schemas.order_item import OrderItemCreate, OrderItemUpdate
from custom_exception.user import UserNotFoundException
from custom_exception.orders import OrderNotFoundException,OrderItemNotFoundException
from custom_exception.medicine import MedicineNotFoundException


# ------------------ ORDER SERVICES ------------------

def create_order_service(db: Session, user_id: int, data: OrderCreate):
    # Validate user exists
    user = user_crud.get_user_by_id(db, user_id)
    if not user:
        raise UserNotFoundException

    return order_crud.create_order(db, user_id, data)


def get_order_service(db: Session, order_id: int):
    order = order_crud.get_order_by_id(db, order_id)

    if not order:
        raise OrderNotFoundException()

    return order


def get_user_orders_service(db: Session, user_id: int):
    # Optional but recommended
    user = user_crud.get_user_by_id(db, user_id)
    if not user:
        raise UserNotFoundException()

    return order_crud.get_orders_by_user(db, user_id)


def update_order_service(db: Session, order_id: int, data: OrderUpdate):
    order = order_crud.update_order(db, order_id, data)

    if not order:
        raise OrderNotFoundException()

    return order


def delete_order_service(db: Session, order_id: int):
    result = order_crud.delete_order(db, order_id)

    if not result:
        raise OrderNotFoundException()

    return result


# ------------------ ORDER ITEM SERVICES ------------------

def create_order_item_service(db: Session, order_id: int, data: OrderItemCreate):
    # Validate order exists
    order = order_crud.get_order_by_id(db, order_id)
    if not order:
        raise OrderNotFoundException()

    # Validate medicine exists
    medicine = medicine_crud.get_medicine_by_id(db, data.medicine_id)
    if not medicine:
        raise MedicineNotFoundException()

    # Business rule: stock check
    if medicine.stock < data.quantity:
        raise HTTPException(
            status_code=400,
            detail="Insufficient stock"
        )

    # Business rule: price integrity (avoid trusting client)
    data.price = medicine.price

    return order_crud.create_order_item(db, order_id, data)


def get_order_items_service(db: Session, order_id: int):
    order = order_crud.get_order_by_id(db, order_id)
    if not order:
        raise OrderNotFoundException()

    return order_crud.get_items_by_order(db, order_id)


def update_order_item_service(db: Session, item_id: int, data: OrderItemUpdate):
    item = order_crud.update_order_item(db, item_id, data)

    if not item:
        raise OrderItemNotFoundException()

    return item


def delete_order_item_service(db: Session, item_id: int):
    result = order_crud.delete_order_item(db, item_id)

    if not result:
        raise OrderItemNotFoundException()

    return result