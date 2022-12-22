class CustomException(Exception):
    def __init__(self, message: str | None = "Error", code: int = 500):
        super().__init__(message)
        self.message = message
        self.code = code


class OccupiedSlot(CustomException):
    def __init__(self, message: str | None = "Slot is already occupied", code: int = 400):
        super().__init__(message, code)


class EmptySlot(CustomException):
    def __init__(self, message: str | None = "Slot is empty", code: int = 400):
        super().__init__(message, code)

class BadSpaceGrid(CustomException):
    def __init__(self, message: str | None = "Simulation space type is not valid", code: int = 400):
        super().__init__(message, code)


class WrongSlot(CustomException):
    def __init__(self, message: str | None = "Slot indexes are out of space ranges", code: int = 400):
        super().__init__(message, code)


class BadDirection(CustomException):
    def __init__(self, message: str | None = "Direction to move is not valid", code: int = 500):
        super().__init__(message, code)


class BadPlayerObject(CustomException):
    def __init__(
            self,
            message: str | None = "Only player type objects can fill simulation space slots",
            code: int = 400
    ):
        super().__init__(message, code)
