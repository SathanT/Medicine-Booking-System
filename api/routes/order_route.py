from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from db.sessions import get_db

from schemas.orders import OrderCreate, OrderUpdate, OrderResponse
from schemas.order_item import OrderItemCreate, OrderItemUpdate, OrderItemResponse

from service.order_service import *

router = APIRouter(prefix="/orders", tags=["Orders"])


# ================== ORDER ENDPOINTS ==================

# CREATE ORDER
@router.post("/user/{user_id}", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
def create_order_ep(
    user_id: int,
    data: OrderCreate,
    db: Session = Depends(get_db)
):
    return create_order_service(db, user_id, data)


# GET ORDER BY ID
@router.get("/{order_id}", response_model=OrderResponse)
def get_order_ep(
    order_id: int,
    db: Session = Depends(get_db)
):
    return get_order_service(db, order_id)


# GET ALL ORDERS OF A USER
@router.get("/user/{user_id}", response_model=list[OrderResponse])
def get_user_orders_ep(
    user_id: int,
    db: Session = Depends(get_db)
):
    return get_user_orders_service(db, user_id)


# UPDATE ORDER
@router.put("/{order_id}", response_model=OrderResponse)
def update_order_ep(
    order_id: int,
    data: OrderUpdate,
    db: Session = Depends(get_db)
):
    return update_order_service(db, order_id, data)


# DELETE ORDER
@router.delete("/{order_id}")
def delete_order_ep(
    order_id: int,
    db: Session = Depends(get_db)
):
    return delete_order_service(db, order_id)


# ================== ORDER ITEM ENDPOINTS ==================

# ADD ITEM TO ORDER
@router.post("/{order_id}/items", response_model=OrderItemResponse, status_code=status.HTTP_201_CREATED)
def create_order_item_ep(
    order_id: int,
    data: OrderItemCreate,
    db: Session = Depends(get_db)
):
    return create_order_item_service(db, order_id, data)


# GET ALL ITEMS IN AN ORDER
@router.get("/{order_id}/items", response_model=list[OrderItemResponse])
def get_order_items_ep(
    order_id: int,
    db: Session = Depends(get_db)
):
    return get_order_items_service(db, order_id)


# UPDATE ORDER ITEM
@router.put("/items/{item_id}", response_model=OrderItemResponse)
def update_order_item_ep(
    item_id: int,
    data: OrderItemUpdate,
    db: Session = Depends(get_db)
):
    return update_order_item_service(db, item_id, data)


# DELETE ORDER ITEM
@router.delete("/items/{item_id}")
def delete_order_item_ep(
    item_id: int,
    db: Session = Depends(get_db)
):
    return delete_order_item_service(db, item_id)