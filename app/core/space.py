from typing import List, Type, Optional

from app.configs import SIMULATION_SPACE_ROWS, SIMULATION_SPACE_COLUMNS, VALID_PLAYER_TYPES
from app.errors import OccupiedSlot, WrongSlot, BadPlayerObject, EmptySlot


class Space:
    def __init__(self):
        self.simulation_space: List[List] = [
            [None for _ in range(SIMULATION_SPACE_COLUMNS)] for _ in range(SIMULATION_SPACE_ROWS)
        ]

    def fill_slot(self, player_object: VALID_PLAYER_TYPES, x: int, y: int):
        if x not in range(SIMULATION_SPACE_COLUMNS) or y not in range(SIMULATION_SPACE_ROWS):
            raise WrongSlot

        if self.simulation_space[y][x] is not None:
            raise OccupiedSlot

        if not isinstance(player_object, VALID_PLAYER_TYPES):
            raise BadPlayerObject

        self.simulation_space[y][x] = player_object

    def change_spot(self, current_x: int, current_y: int, new_x: int, new_y: int):
        for idx in (current_x, new_x):
            if idx not in range(SIMULATION_SPACE_COLUMNS):
                raise WrongSlot

        for idx in (current_y, new_y):
            if idx not in range(SIMULATION_SPACE_ROWS):
                raise WrongSlot

        if self.simulation_space[current_y][current_x] is None:
            raise EmptySlot("No player is in the source slot")

        if self.simulation_space[new_y][new_x] is not None:
            raise OccupiedSlot("Target slot is already occupied")

        self.simulation_space[new_y][new_x] = self.simulation_space[current_y][current_x]
        self.simulation_space[current_y][current_x] = None

    def remove_slot(
            self,
            x: int,
            y: int,
            raise_on_empty: bool = True,
            raise_on_bad_index: bool = True,
            player_type: Optional[Type[VALID_PLAYER_TYPES]] = None
    ):
        """
        Remove a player object from a slot of simulation space

        :param x: Coordination of slot on X-axis (column number, 0-based)
        :param y: Coordination of slot on Y-axis (row number, 0-based)
        :param raise_on_empty: If True, it will raise an error, if the specified slot is empty
        :param raise_on_bad_index: If True, it will raise an error, if the specified slot coordination is out of range
        :param player_type: If not None, then slot will be removed, only if it was occupied by the specified player type
        :return: None
        """

        if raise_on_bad_index:
            if x not in range(SIMULATION_SPACE_COLUMNS) or y not in range(SIMULATION_SPACE_ROWS):
                raise WrongSlot

        player_object = self.simulation_space[y][x]

        if raise_on_empty and player_object is None:
            raise EmptySlot

        if player_type:
            if player_object and not isinstance(player_object, player_type):
                raise BadPlayerObject(f"{type(player_object).__name__} object cannot be removed from simulation space")

        self.simulation_space[y][x] = None
