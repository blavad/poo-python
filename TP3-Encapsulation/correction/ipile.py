from typing import TypeVar, Generic
from abc import ABC, abstractmethod

T = TypeVar("T")

class IPile(ABC, Generic[T]):
    @abstractmethod
    def empile(self, value: T) -> None:
        pass

    @abstractmethod
    def depile(self) -> None:
        pass
