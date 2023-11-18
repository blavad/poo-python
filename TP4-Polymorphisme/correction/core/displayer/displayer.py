from abc import ABC, abstractmethod
from ..color import Color


class Displayer(ABC):
    @abstractmethod
    def draw_point(self, x: int, y: int, color: Color) -> None:
        pass

    @abstractmethod
    def draw_line(self, x1: int, y1: int, x2: int, y2: int, color: Color) -> None:
        pass

    @abstractmethod
    def draw_circle(self, x: int, y: int, radius: int, color: Color) -> None:
        pass

    @abstractmethod
    def draw_rectangle(self, x: int, y: int, width: int, length: int, color: Color) -> None:
        pass

    @abstractmethod
    def draw_square(self, x: int, y: int, cote: int, color: Color) -> None:
        pass
