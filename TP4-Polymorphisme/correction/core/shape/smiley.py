from . import CombinedShape2D, Circle, Rectangle, Shape2D
from ..color import Color, BLACK, WHITE, RED, BLUE, GREEN


class Smiley(CombinedShape2D):
    def __init__(self, x: int, y: int, size: int, color: Color = (253, 216, 85)) -> None:
        radius = size / 2
        smiley = [
            self.create_head(x, y, radius, color),
            self.create_left_eye(x, y, radius),
            self.create_right_eye(x, y, radius),
            self.create_noize(x, y, radius),
            self.create_mouse(x, y, radius),
        ]
        super().__init__(x, y, smiley)

    def create_head(self, x: int, y: int, size: int, color: Color) -> Shape2D:
        head = Circle(x + size / 100 * 100, y + size / 100 * 100, size, color)
        return head

    def create_left_eye(self, x: int, y: int, size: int) -> Shape2D:
        left_eye = CombinedShape2D(
            0,
            0,
            [
                Circle(x + size / 100 * 50, y + size / 100 * 75, 0.3 * size, WHITE),
                Circle(x + size / 100 * 65, y + size / 100 * 85, 0.1 * size, GREEN),
            ],
        )
        return left_eye

    def create_right_eye(self, x: int, y: int, size: int) -> Shape2D:
        right_eye = CombinedShape2D(
            0,
            0,
            [
                Circle(x + size / 100 * 150, y + size / 100 * 75, 0.2 * size, WHITE),
                Circle(x + size / 100 * 145, y + size / 100 * 80, 0.1 * size, BLUE),
            ],
        )
        return right_eye

    def create_noize(self, x: int, y: int, size: int) -> Shape2D:
        noize = CombinedShape2D(
            0,
            0,
            [
                Rectangle(x + size / 100 * 85, y + size / 100 * 120, 0.1 * size, 0.03 * size, BLACK),
                Rectangle(x + size / 100 * 100, y + size / 100 * 120, 0.1 * size, 0.03 * size, BLACK),
            ],
        )
        return noize

    def create_mouse(self, x: int, y: int, size: int) -> Shape2D:
        mouse = CombinedShape2D(
            0,
            0,
            [
                Rectangle(x + size / 100 * 100, y + size / 100 * 150, 0.3 * size, 0.3 * size, RED),
                Rectangle(x + size / 100 * 40, y + size / 100 * 140, size, 0.1 * size, BLACK),
            ],
        )
        return mouse
