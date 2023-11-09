from abc import ABC, abstractmethod
from typing import TypeVar, Generic


color = tuple[int,int,int]
T = TypeVar('T')

class Displayer(Generic[T],ABC):

    @abstractmethod
    def draw_point(self,x:int,y:int,color:color) -> None:
        pass

    @abstractmethod
    def draw_line(self,x1:int,y1:int,x2:int,y2:int,color:color) -> None:
        pass

    @abstractmethod
    def draw_circle(self,x:int,y:int,radius : int,color:color) -> None:
        pass

    @abstractmethod
    def draw_rectangle(self,x:int,y:int,width : int,length : int,color:color) -> None:
        pass

    @abstractmethod
    def draw_quare(self,x:int,y:int,side : int,color:color) -> None:
        pass







