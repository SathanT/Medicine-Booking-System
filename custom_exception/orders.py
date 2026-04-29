from custom_exception.base import AppException

class OrderNotFoundException(AppException):
    def __init__(self):
        super().__init__("order not found", 404)

    
class OrderItemNotFoundException(AppException):
    def __init__(self):
        super().__init__("Order Item not found", 404)
