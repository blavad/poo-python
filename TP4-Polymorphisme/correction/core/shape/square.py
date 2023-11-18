from ..color import Color
from ..displayer import Displayer
from .shape2D import Shape2D


class Square(Shape2D):
    def __init__(self, x: int, y: int, side: int, color: Color) -> None:
        super().__init__(x, y, color)
        self._side = side

    def area(self) -> float:
        return self._side * self._side

    def draw(self, displayer: Displayer) -> None:
        return displayer.draw_square(self._xpos, self._ypos, self._side, self._color)
