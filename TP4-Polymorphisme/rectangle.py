from Shape2D import Shape2D
from ShellDisplayer import ShellDisplayer

color = tuple[int,int,int]
class rectangle(Shape2D):

    def __init__(self, x:int, y:int,color : color, width : int, height : int,):
        super().__init__(x, y, color)
        self._height = height
        self._width = width



    def area(self) -> float:
        return self._height * self._width
    
    def draw(self,afficheur):
        shell_displayer = afficheur
        return shell_displayer.draw_rectangle(self._xpos, self._ypos, self._height, self._width, self._color)
    


if __name__ == "__main__":
    b = rectangle(5,5,{0,0,0},10,10)
    b.draw(ShellDisplayer)


