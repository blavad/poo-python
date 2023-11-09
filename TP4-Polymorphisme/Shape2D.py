from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from Displayer import Displayer
class InvalidColorError(Exception):
    pass


T = TypeVar('T')
color = tuple[int,int,int]
class Shape2D(Generic[T],ABC):

    
    def __init__(self,x: float,y: float,color: color) -> None:
        if not self.couleurvalide:
            raise InvalidColorError
        self._xpos = x 
        self._ypos = y
        self._color = color
        
    @abstractmethod
    def area(self,element :T) -> float:
        pass

    
    def move(self,deltaX : int,deltaY : int) -> None:
        self._xpos += deltaX
        self._ypos += deltaY

    
    def get_xy(self) -> tuple[int,int]:
        return [self._xpos,self._ypos]

    @abstractmethod
    def draw(self,afficheur):
        
        raise NotImplementedError("Class not implemented")
    
    def couleurvalide(self, color:color) -> bool:
        return all(0 <= value <= 255 for value in color)


