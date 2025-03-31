from abc import ABC, abstractmethod
from ..color import Color
from ..displayer import Displayer


class Shape2D(ABC):
    """
    Représente le concept abstrait de forme 2D. 
    Cette classe contient 3 attributs concrets (xpos, ypos et color), 
    2 méthodes abstraites (area et draw) et 2 méthodes concrètes
    (move et get_xy).
    """
    def __init__(self, x: int, y: int, color: Color) -> None:
        self._xpos = x
        self._ypos = y
        # vérifie que la couleur est valide
        if not self._is_valid_color(color):
            raise ValueError("The color does not match requirements.")

        self._color = color

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def draw(self, displayer: Displayer) -> None:
        pass

    def move(self, deltaX: int, deltaY: int) -> None:
        self._xpos += deltaX
        self._ypos += deltaY

    def get_xy(self) -> tuple[int, int]:
        return self._xpos, self._ypos

    def _is_valid_color(self, color: Color) -> bool:
        is_valid: bool = len(color) == 3
        for i in range(3):
            if color[i] < 0 or color[i] > 255:
                is_valid = False

        return is_valid
