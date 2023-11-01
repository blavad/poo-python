
from interface import Ipile


# Cette classe hérite de Ipile (n'étant précisé dans l'énnoncé, on n'appliquera pas la norme BEP 483)

class PileMultiple(Ipile):

    def __init__(self, piles):
        self._stack = piles 

    def empile(self, nombre):
        for pile in self._stack:
            pile.empile(nombre)

    def depile(self):
        for pile in self._stack:
            pile.depile()

    def __str__(self):
        return f"PileMultiple({', '.join(str(piles) for piles in self._stack)})"
        
    

