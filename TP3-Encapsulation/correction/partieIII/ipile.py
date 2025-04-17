from abc import ABC, abstractmethod


class IPile(ABC):
    @abstractmethod
    def empile(self, valeur):
        pass

    @abstractmethod
    def depile(self):
        pass
