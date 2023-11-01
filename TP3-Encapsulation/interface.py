from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')

class Ipile(Generic[T],ABC):
    @abstractmethod
    def empile(self,element :T) -> None:
        pass

    @abstractmethod 
    def depile(self) ->T:
        pass

class LIFO(Generic[T],Ipile[T]):
    def __init__(self,liste=[]):
        self._stack = list(liste)


    def empile(self,nombre :T):
        self._stack.append(nombre)
    
    def depile(self) -> T: 
        if len(self._stack) > 0:
            self._stack.pop()
        else:
            print("On ne peut enlever un élement d'une liste vide")
    
    def __str__(self):
        return f"LIFO({self._stack})"
    
class FIFO(Generic[T],Ipile[T]):
    def __init__(self,liste=[]):
        self._stack = list(liste)


    def empile(self,nombre :T):
        self._stack.append(nombre)
    
    def depile(self) -> T: 
        if len(self._stack) > 0:
            self._stack.pop(0)
        else:
            print("On ne peut enlever un élement d'une liste vide")
    
    def __str__(self):
        return f"LIFO({self._stack})"