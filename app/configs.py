import enum


SIMULATION_SPACE_ROWS = 10
SIMULATION_SPACE_COLUMNS = 10


class DirectionEnum(enum.Enum):
    UP = "up"
    DOWN = "down"
    RIGHT = "right"
    LEFT = "left"

class PlayerEnum(enum.Enum):
    DINOSAUR = "Dinosaur"
    ROBOT = "Robot"

    @classmethod
    def has_value(cls, value) -> bool:
        return value in cls._value2member_map_

    @classmethod
    def is_static(cls, player: str) -> bool:
        return cls.has_value(player) and player == cls.DINOSAUR.value
