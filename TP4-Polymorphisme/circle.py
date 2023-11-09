from Shape2D import Shape2D
from math import pi
class circle(Shape2D):

    def __init__(self, x=0, y=0, color={255, 255, 255}, radius=10) -> None:
        super().__init__(x, y, color)
        self._radius = radius



    def area(self) -> float:
        return pi * (self._radius ** 2)
    
    def draw(self,afficheur):
        afficheur.draw_circle()
        
    

    
