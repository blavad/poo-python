from typing import TypeVar, Generic
    
T = TypeVar('T')
class LogGeneric(Generic[T]):
    def __init__(self, name: str, value: T) -> None:
        self.name = name
        self.value = value

    def set(self, new: T) -> None:
        self.value = new

    def get(self) -> T:
        return self.value

    def log(self) -> None:
        print(f"name={self.name} value={self.value}")

loggerFloat : LogGeneric[float] = LogGeneric("example1", 3.25)
loggerFloat.log() # name=example1 value=3.25

loggerList : LogGeneric[list] = LogGeneric("example2", [1, 2])
loggerList.log() # name=example2 value=[1, 2]
loggerList.set([4, 6, 8, 10, 12])
loggerList.log() # name=example2 value=[4, 6, 8, 10, 12]