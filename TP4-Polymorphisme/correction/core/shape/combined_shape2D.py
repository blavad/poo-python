import copy

from ..color import *
from .shape2D import Shape2D
from ..displayer import Displayer


class CombinedShape2D(Shape2D):
    def __init__(self, x: int, y: int, shapes: list[Shape2D]) -> None:
        super().__init__(x, y, WHITE)
        self._shapes = copy.deepcopy(shapes)
        for shape in self._shapes:
            shape.move(x, y)

    def area(self) -> float:
        sum_area: int = 0
        for shape in self._shapes:
            sum_area += shape.area()
        return sum_area

    def move(self, x: int, y: int) -> None:
        for shape in self._shapes:
            shape.move(x, y)

    def draw(self, displayer: Displayer) -> None:
        for shape in self._shapes:
            shape.draw(displayer)
