from ipile import IPile 

class PileMultiple(IPile[int]):
    def __init__(self, piles: list[IPile[int]]):
        self.__piles = piles

    def empile(self, value: int) -> None:
        for pile in self.__piles:
            pile.empile(value) 

    def depile(self) -> None:
        for pile in self.__piles:
            pile.depile() 

    def __str__(self) -> str:
        res = "PileMultiple([ "
        for index, pile  in enumerate(self.__piles):
            res += f"{pile}"
            if (index != len(self.__piles) - 1):
                res += ", "
        res += " ])"
        return  res
    