from base import Player
from space import Space


class Dinosaur(Player):
    def __init__(self, space: Space, x: int, y: int):
        self.__space: Space = space
        self.__position_x: int = -1
        self.__position_y: int = -1
        self._create(x, y)

    def __str__(self):
        return f"Dinosaur at {self.__position_x},{self.__position_y}"

    def _create(self, x: int, y: int):
        try:
            self.__space.fill_slot(player_object=self, x=x, y=y)
        except:
            raise
        else:
            self.__position_x: int = x
            self.__position_y: int = y
