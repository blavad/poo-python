from .displayer import Displayer
from ..color import Color


class ShellDisplayer(Displayer):
    def draw_point(self, x: int, y: int, color: Color) -> None:
        print(f"Point(x={x}, y={y}, color={color})")

    def draw_line(self, x1: int, y1: int, x2: int, y2: int, color: Color) -> None:
        print(f"Line(x1={x1}, y1={y1}, x2={x2}, y2={y2}, color={color})")

    def draw_circle(self, x: int, y: int, radius: int, color: Color) -> None:
        print(f"Circle(x={x}, y={y}, radius={radius}, color={color})")

    def draw_rectangle(self, x: int, y: int, width: int, length: int, color: Color) -> None:
        print(f"Rectangle(x={x}, y={y}, width={width}, length={length}, color={color})")

    def draw_square(self, x: int, y: int, cote: int, color: Color) -> None:
        print(f"Square(x={x}, y={y}, cote={cote}, color={color})")
