from typing import List, Type, Optional

from app.configs import SIMULATION_SPACE_ROWS, SIMULATION_SPACE_COLUMNS, VALID_PLAYER_TYPES
from app.errors import OccupiedSlot, WrongSlot, BadPlayerObject, EmptySlot


class Space:
    def __init__(self, existing_space: List[List] | None = None):
        if existing_space:
            self.__validate_existing_space(existing_space)
            self.rows_count: int = len(existing_space)
            self.columns_count: int = len(existing_space[0])
            self.simulation_space: List[List] = existing_space
        else:
            self.rows_count: int = SIMULATION_SPACE_ROWS
            self.columns_count: int = SIMULATION_SPACE_COLUMNS
            self.simulation_space: List[List] = [
                [None for _ in range(self.columns_count)] for _ in range(self.rows_count)
            ]

    def __validate_existing_space(self, space: List[List] | None = None):
        if not isinstance(space, list):
            raise BadSpaceGrid

        if len(space) < 2:
            raise BadSpaceGrid("Simulation space grid must have more than 4 cells to work")

        for row in space:
            if not isinstance(row, list):
                raise BadSpaceGrid

            if not len(row) == len(space):
                raise BadSpaceGrid(
                    "Simulation space type is not valid. "
                    "It must be a square shaped grid with same count of rows and columns"
                )

            if not all(item is None or PlayerEnum.has_value(item) for item in row):
                raise BadPlayerObject("Player items in space grid rows are invalid")

    def _direction_coordination(self, x, y, direction: DirectionEnum) -> Tuple[int, int]:
        target_x: int = x
        target_y: int = y

        match direction:
            case DirectionEnum.UP:
                target_y -= 1
            case DirectionEnum.DOWN:
                target_y += 1
            case DirectionEnum.LEFT:
                target_x -= 1
            case DirectionEnum.RIGHT:
                target_x += 1
            case _:
                raise BadDirection()

        return target_x, target_y

    def _remove_slot(
            self,
            x: int,
            y: int,
            only_static: bool = False,
            raise_on_empty: bool = True,
            raise_on_bad_index: bool = True,
            raise_on_bad_player_type: bool = True
    ):
        """
        Remove a player object from a slot of simulation space

        :param x: Coordination of slot on X-axis (column number, 0-based)
        :param y: Coordination of slot on Y-axis (row number, 0-based)
        :param only_static: If True, then slot will be removed, only if it was occupied by a static player type
        :param raise_on_empty: If True, it will raise an error, if the specified slot is empty
        :param raise_on_bad_index: If True, it will raise an error, if the specified slot coordination is out of range
        :return: None
        """

        if raise_on_bad_index:
            if x not in range(self.columns_count) or y not in range(self.rows_count):
                raise WrongSlot

        player = self.simulation_space[y][x]

        if raise_on_empty and player is None:
            raise EmptySlot

        if only_static:
            if player and not PlayerEnum.is_static(player):
                if not raise_on_bad_player_type:
                    return
                raise BadPlayerObject(f"{player} object cannot be removed from simulation space")

        self.simulation_space[y][x] = None
