from interface import Ipile,LIFO,FIFO
from typing import TypeVar, Generic
from pile_multiple import PileMultiple
T = TypeVar('T')

def test_pile(pile : Ipile[int]) -> T:

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
    pile_entiers = FIFO[int]()  
    test_pile(pile_entiers)

    pile_entiers = FIFO[int]([1,2,3])  
    test_pile(pile_entiers)

    pile_entiers = LIFO[int]()  
    test_pile(pile_entiers)

    
    pile_multiple_1 = PileMultiple([FIFO[int](),FIFO[int]([1,2,3]),LIFO[int]([1,2,3])])

    
    test_pile(pile_multiple_1)


    