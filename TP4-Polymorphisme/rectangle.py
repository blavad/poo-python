from Shape2D import Shape2D
color = tuple[int,int,int]
class rectangle(Shape2D):

    def __init__(self, x:int, y:int,color : color, width : int, height : int,):
        super().__init__(x, y, color)
        self._height = height
        self._width = width



    def area(self) -> float:
        return self._height * self._width
    
    def draw(self):
        self.draw


