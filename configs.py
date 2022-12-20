import enum

from base import Player, ActivePlayer

SIMULATION_SPACE_ROWS = 10
SIMULATION_SPACE_COLUMNS = 10


class Direction(enum.Enum):
    UP = "up"
    DOWN = "down"
    RIGHT = "right"
    LEFT = "left"


VALID_PLAYER_TYPES = Player | ActivePlayer
