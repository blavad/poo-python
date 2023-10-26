from ipile import IPile
from fifo import FIFO
from lifo import LIFO
from pile_multiple import PileMultiple

def test_pile(pile: IPile[int]) -> None:
    print(pile)
    pile.empile(5)
    print(pile)
    pile.empile(8)
    print(pile)
    pile.depile()
    print(pile)
    pile.depile()
    print(pile)


def main():
    test_pile(FIFO([]))
    test_pile(FIFO([1, 2, 3]))
    test_pile(LIFO([]))

    pile_multiple1 = PileMultiple([FIFO([]), FIFO([]), LIFO([])])
    pile_multiple2 = PileMultiple([LIFO([]), pile_multiple1])
    test_pile(pile_multiple1)
    test_pile(pile_multiple2)

if __name__ == "__main__":
    main()