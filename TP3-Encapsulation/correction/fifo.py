from ipile import IPile
from typing import TypeVar

T = TypeVar("T")


class FIFO(IPile[T]):
    """
    La pile FIFO (First In First Out) est une pile dans lesquels
    les premiers éléments empilés seront les premiers dépilés.
    """

    def __init__(self, values: list[T]) -> None:
        self.__pile = values

    def empile(self, value: T) -> None:
        self.__pile.append(value)

    def depile(self) -> None:
        if len(self.__pile) > 0:
            del self.__pile[0]

    def __str__(self) -> None:
        return f"FIFO({self.__pile})"
