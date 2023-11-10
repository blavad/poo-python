from Shape2D import Shape2D
from ShellDisplayer import ShellDisplayer

class point(Shape2D):

    def __init__(self, x : int, y : int, color={255, 255, 255}):
        super().__init__(x, y, color)
        



    def area(self) -> float:
        return 0
    
    def draw(self,afficheur):
        shell_displayer = afficheur()
        return shell_displayer.draw_point(self._xpos, self._ypos, self._color)
    

if __name__ == "__main__":
    b = point(5,5,{0,0,0})
    b.draw(ShellDisplayer)