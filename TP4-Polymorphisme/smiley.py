from CombinedShape2D import CombinedShape2D
from circle import circle
from rectangle import rectangle

class Smiley(CombinedShape2D):

    def __init__(self, x=0, y=0, size=10, color=(255, 255, 255)):
        face = circle(x, y, size, (0, 255, 255))  # Face
        left_eye = circle(x - size / 3, y + size / 3, size / 8, (0,0,0))  # Left Eye
        right_eye = circle(x + size / 3, y + size / 3, size / 8,(0,0,0))  # Right Eye
        nose = rectangle(x, y, (125,125,125), size / 12,size / 12)  # Nose
        mouth = rectangle(x, y - size / 4, (125,125,0), size / 2, size / 8)  # Mouth
        shapes = [face, left_eye, right_eye, nose, mouth]
        super().__init__(shapes)

    