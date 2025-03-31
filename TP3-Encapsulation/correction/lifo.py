from ipile import IPile
from typing import TypeVar

T = TypeVar("T")


class LIFO(IPile[T]):
    """
    La pile LIFO (Last In First Out) est une pile dans lesquels
    les derniers éléments empilés seront les premiers dépilés.
    """

    def __init__(self, values: list[T]) -> None:
        self.__pile = values

    def empile(self, value: T) -> None:
        self.__pile.append(value)

    def depile(self) -> None:
        if len(self.__pile) > 0:
            self.__pile.pop()

    def __str__(self) -> None:
        return f"LIFO({self.__pile})"
