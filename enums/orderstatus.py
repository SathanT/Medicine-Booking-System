from enum import Enum

class Status(Enum):
    PENDING="pending"
    CONFIRMED="confirmed"
    SHIPPED="shipped"
    DELIVERED="delivered"
    CANCELLED="cancelled"