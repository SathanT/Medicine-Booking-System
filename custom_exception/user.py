from custom_exception.base import AppException


class UserNotFoundException(AppException):
    def __init__(self):
        super().__init__("User not found", 404)


class UserAlreadyExistsException(AppException):
    def __init__(self):
        super().__init__("User already exists", 400)



class AddressNotFoundException(AppException):
    def __init__(self):
        super().__init__("Address not found", 404)
