from base import ActivePlayer
from configs import Direction
from dinosaur import Dinosaur
from space import Space


class Robot(ActivePlayer):
    def __init__(self, space: Space, x: int, y: int):
        self.__space: Space = space
        self.__position_x: int = -1
        self.__position_y: int = -1
        self._create(x, y)

    def __str__(self):
        return f"Robot at {self.__position_x},{self.__position_y}"

    def _create(self, x: int, y: int):
        try:
            self.__space.fill_slot(player_object=self, x=x, y=y)
        except:
            raise
        else:
            self.__position_x: int = x
            self.__position_y: int = y

    def move(self, direction: Direction):
        new_x: int = self.__position_x
        new_y: int = self.__position_y
        match direction:
            case Direction.UP:
                new_y -= 1
            case Direction.DOWN:
                new_y += 1
            case Direction.LEFT:
                new_x -= 1
            case Direction.RIGHT:
                new_x += 1

        try:
            self.__space.change_spot(
                current_x=self.__position_x,
                current_y=self.__position_y,
                new_x=new_x,
                new_y=new_y
            )
        except:
            raise
        else:
            self.__position_x: int = new_x
            self.__position_y: int = new_y

    def attack(self):
        # up slot
        self.__space.remove_slot(
            x=self.__position_x,
            y=self.__position_y + 1,
            raise_on_empty=False,
            raise_on_bad_index=False,
            player_type=Dinosaur
        )

        # down slot
        self.__space.remove_slot(
            x=self.__position_x,
            y=self.__position_y - 1,
            raise_on_empty=False,
            raise_on_bad_index=False,
            player_type=Dinosaur
        )

        # right slot
        self.__space.remove_slot(
            x=self.__position_x + 1,
            y=self.__position_y,
            raise_on_empty=False,
            raise_on_bad_index=False,
            player_type=Dinosaur
        )

        # left slot
        self.__space.remove_slot(
            x=self.__position_x - 1,
            y=self.__position_y,
            raise_on_empty=False,
            raise_on_bad_index=False,
            player_type=Dinosaur
        )
