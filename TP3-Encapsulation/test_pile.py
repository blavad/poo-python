from interface import Ipile,LIFO
from typing import TypeVar, Generic

T = TypeVar('T')

def test_pile(pile : Ipile[int]):

    print("Pile initiale:", pile)
    pile.empile(5)
    print("Après empile(5):", pile)
    pile.empile(8)
    print("Après empile(8):", pile)
    pile.depile()
    print("Après depile():", pile)
    pile.depile()
    print("Après depile():", pile)

if __name__ == "__main__":
    pile_entiers = LIFO[int]()  
    test_pile(pile_entiers)