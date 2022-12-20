class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class OccupiedSlot(CustomException):
    def __init__(self, message: str | None = None):
        self.message = message or "Slot is already occupied"


class EmptySlot(CustomException):
    def __init__(self, message: str | None = None):
        self.message = message or "Slot is empty"


class WrongSlot(CustomException):
    def __init__(self, message: str | None = None):
        self.message = message or "Slot indexes are out of space ranges"


class BadPlayerObject(CustomException):
    def __init__(self, message: str | None = None):
        self.message = message or "Only player type objects can fill simulation space slots"
