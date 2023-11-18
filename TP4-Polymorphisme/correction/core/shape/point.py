from ..color import Color
from ..displayer import Displayer
from .shape2D import Shape2D


class Point(Shape2D):
    def __init__(self, x: int, y: int, color: Color) -> None:
        super().__init__(x, y, color)

    def area(self) -> float:
        return 0

    def draw(self, displayer: Displayer) -> None:
        return displayer.draw_circle(self._xpos, self._ypos, 5, self._color)
