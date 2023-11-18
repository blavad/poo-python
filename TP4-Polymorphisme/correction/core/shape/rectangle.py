from ..color import Color
from ..displayer import Displayer
from .shape2D import Shape2D


class Rectangle(Shape2D):
    def __init__(self, x: int, y: int, width: int, height: int, color: Color) -> None:
        super().__init__(x, y, color)
        self._width = width
        self._height = height

    def area(self) -> float:
        return self._width * self._height

    def draw(self, displayer: Displayer) -> None:
        return displayer.draw_rectangle(self._xpos, self._ypos, self._width, self._height, self._color)
