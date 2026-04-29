from custom_exception.base import AppException


class DatabaseException(AppException):
    def __init__(self):
        super().__init__("Internal server error", 500)
