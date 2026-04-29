from custom_exception.base import AppException


class MedicineNotFoundException(AppException):
    def __init__(self):
        super().__init__("medicine not found", 404)


class InvalidPriceException(AppException):
    def __init__(self):
        super().__init__("Price must be greater than 0",422)


class InvalidStockException(AppException):
    def __init__(self):
        super().__init__("Stock cannot be negative",422)


class ManufacturerNotFoundException(AppException):
    def __init__(self):
        super().__init__("manufacturer not found", 404)


class CategoryNotFoundException(AppException):
    def __init__(self):
        super().__init__("Category not found", 404)
