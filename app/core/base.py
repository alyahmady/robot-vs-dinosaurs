from abc import ABCMeta, abstractmethod


class Player(metaclass=ABCMeta):
    @abstractmethod
    def _create(self, x: int, y: int):
        raise NotImplementedError(f"Not implemented for {self.__class__.__name__}")


class ActivePlayer(metaclass=ABCMeta):
    @abstractmethod
    def _create(self, x: int, y: int):
        raise NotImplementedError(f"Not implemented for {self.__class__.__name__}")

    @abstractmethod
    def move(self, direction):
        raise NotImplementedError(f"Not implemented for {self.__class__.__name__}")

    @abstractmethod
    def attack(self):
        raise NotImplementedError(f"Not implemented for {self.__class__.__name__}")
