from Shape2D import Shape2D
from ShellDisplayer import ShellDisplayer

class CombinedShape2D(Shape2D):

    def __init__(self, forme : list[Shape2D]) -> None:
        
        self._area = 0
        self._x = 0
        self._y = 0
        self._formes = forme
        print(forme)
        for i in forme:
            print(i)
            self._area += i.area()
            self._x += i.get_xy()[0]
            self._y += i.get_xy()[1]

        self._x = self._x/len(forme)
        self._y = self._y/len(forme)
    
    def draw(self,afficheur):
        
        for shape in self._formes:
            print(shape)
            shape.draw(afficheur) 
        

    def area(self):
        return self._area
    
    def get_xy(self):
        return [self._x,self._y]
    
    def move(self,deltaX : int,deltaY : int) -> None:
        self._x += deltaX
        self._y += deltaY

    def add(self, forme: Shape2D) -> None:
        self._formes.append(forme)
        self._area += forme.area()
        self._x += forme.get_xy()[0]
        self._y += forme.get_xy()[1]

    def remove(self, forme: Shape2D) -> None:
        if forme in self._formes:
            self._formes.remove(forme)
            self._area -= forme.area()
            self._x -= forme.get_xy()[0]
            self._y -= forme.get_xy()[1]


