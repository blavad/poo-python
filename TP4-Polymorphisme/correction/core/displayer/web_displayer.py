import requests

from .displayer import Displayer
from ..color import Color


class WebDisplayer(Displayer):
    def __init__(self, displayCode, firstDisplay=True, url="http://draw.david-albert.fr") -> None:
        self._url = url
        self._displayCode = displayCode
        self._displayNum = 1 if firstDisplay else 2

    def draw_point(self, x: int, y: int, color: Color) -> None:
        self._print_on_display({"shape": "point", "x": x, "y": y, "color": color})

    def draw_line(self, x1: int, y1: int, x2: int, y2: int, color: Color) -> None:
        self._print_on_display({"shape": "line", "x1": x1, "y1": y1, "x2": x2, "y2": y2, "color": color})

    def draw_circle(self, x: int, y: int, radius: int, color: Color) -> None:
        self._print_on_display({"shape": "circle", "x": x, "y": y, "radius": radius, "color": color})

    def draw_rectangle(self, x: int, y: int, width: int, length: int, color: Color) -> None:
        self._print_on_display(
            {"shape": "rectangle", "x": x, "y": y, "width": width, "height": length, "color": color}
        )

    def draw_square(self, x: int, y: int, cote: int, color: Color) -> None:
        self._print_on_display({"shape": "square", "x": x, "y": y, "cote": cote, "color": color})

    def _print_on_display(self, shape_as_dict: dict):
        requests.post(f"{self._url}/draw/{self._displayCode}/{self._displayNum}", json=shape_as_dict)
