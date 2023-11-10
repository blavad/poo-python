from Shape2D import Shape2D
from math import pi
from ShellDisplayer import ShellDisplayer
class circle(Shape2D):

    def __init__(self, x=0, y=0, radius=10, color=[255, 255, 255]) -> None:
        super().__init__(x, y, color)
        self._radius = radius
        self._color = color



    def area(self) -> float:
        return pi * (self._radius ** 2)
    
    def draw(self,afficheur) -> None:
        shell_displayer = afficheur
        return shell_displayer.draw_circle(self._xpos, self._ypos, self._radius, self._color)
        
if __name__ == "__main__":
    b = circle(5,5,{0,0,0}, 30)
    b.draw(ShellDisplayer)


    
