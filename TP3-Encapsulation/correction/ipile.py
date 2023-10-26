from typing import TypeVar, Generic

T = TypeVar("T")


class IPile(Generic[T]):
    def empile(self, value: T) -> None:
        raise NotImplementedError("The method is abstract")

    def depile(self) -> None:
        raise NotImplementedError("The method is abstract")
