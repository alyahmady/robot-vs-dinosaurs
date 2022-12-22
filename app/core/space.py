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
