from sqlalchemy.orm import Session
from datetime import datetime

from models.orders import OrderDB, OrderItemDB
from schemas.orders import OrderCreate, OrderUpdate
from schemas.order_item import OrderItemCreate, OrderItemUpdate


# ------------------ CREATE ------------------

def create_order(db: Session, user_id: int, data: OrderCreate):
    try:
        order = OrderDB(
            user_id=user_id,
            status=data.status,
            created_at=datetime.utcnow(),
        )

        db.add(order)
        db.commit()
        db.refresh(order)

        return order

    except Exception as e:
        print(str(e))
        db.rollback()


def create_order_item(db: Session, order_id: int, data: OrderItemCreate):
    try:
        item = OrderItemDB(
            order_id=order_id,
            medicine_id=data.medicine_id,
            quantity=data.quantity,
            price=data.price,
        )

        db.add(item)
        db.commit()
        db.refresh(item)

        return item

    except Exception as e:
        print(str(e))
        db.rollback()


# ------------------ READ ------------------

def get_order_by_id(db: Session, order_id: int):
    try:
        return db.query(OrderDB).filter(OrderDB.id == order_id).first()
    except Exception as e:
        print(str(e))


def get_orders_by_user(db: Session, user_id: int):
    try:
        return db.query(OrderDB).filter(OrderDB.user_id == user_id).all()
    except Exception as e:
        print(str(e))


def get_items_by_order(db: Session, order_id: int):
    try:
        return db.query(OrderItemDB).filter(OrderItemDB.order_id == order_id).all()
    except Exception as e:
        print(str(e))


# ------------------ UPDATE ------------------

def update_order(db: Session, order_id: int, data: OrderUpdate):
    try:
        order = db.query(OrderDB).filter(OrderDB.id == order_id).first()

        if not order:
            return None

        update_data = data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(order, key, value)

        db.commit()
        db.refresh(order)

        return order

    except Exception as e:
        print(str(e))
        db.rollback()


def update_order_item(db: Session, item_id: int, data: OrderItemUpdate):
    try:
        item = db.query(OrderItemDB).filter(OrderItemDB.id == item_id).first()

        if not item:
            return None

        update_data = data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(item, key, value)

        db.commit()
        db.refresh(item)

        return item

    except Exception as e:
        print(str(e))
        db.rollback()


# ------------------ DELETE ------------------

def delete_order(db: Session, order_id: int):
    try:
        order = db.query(OrderDB).filter(OrderDB.id == order_id).first()

        if not order:
            return None

        db.delete(order)
        db.commit()

        return {"message": "Order deleted successfully"}

    except Exception as e:
        print(str(e))
        db.rollback()


def delete_order_item(db: Session, item_id: int):
    try:
        item = db.query(OrderItemDB).filter(OrderItemDB.id == item_id).first()

        if not item:
            return None

        db.delete(item)
        db.commit()

        return {"message": "Order item deleted successfully"}

    except Exception as e:
        print(str(e))
        db.rollback()