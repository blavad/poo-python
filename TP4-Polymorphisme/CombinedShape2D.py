from Shape2D import Shape2D

class CombinedShape2D(Shape2D):

    def __init__(self, forme : list[Shape2D]) -> None:
        
        self._area = 0
        self._x = 0
        self._y = 0

        for i in forme:
            self._area += i.area()
            self._x += i.get_xy()[0]
            self._y += i.get_xy()[1]

        self._x = self._x/len(forme)
        self._y = self._y/len(forme)
    
    def draw(self):
        self.draw

    def area(self):
        return self._area




