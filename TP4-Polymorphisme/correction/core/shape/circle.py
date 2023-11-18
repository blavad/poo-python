import math
from ..color import Color
from ..displayer import Displayer
from .shape2D import Shape2D


class Circle(Shape2D):
    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        radius: int = 20,
        color: Color = (0, 0, 0),
    ) -> None:
        super().__init__(x, y, color)
        self._radius = radius

    def area(self) -> float:
        return math.pi * self._radius**2

    def draw(self, displayer: Displayer) -> None:
        return displayer.draw_circle(self._xpos, self._ypos, self._radius, self._color)
