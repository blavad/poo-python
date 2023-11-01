class LIFO:
    def __init__(self,liste=[]):
        self._stack = list(liste)


    def empile(self,nombre):
        self._stack.append(nombre)
    
    def depile(self): 
        if len(self._stack) > 0:
            self._stack.pop()
        else:
            print("On ne peut enlever un élement d'une liste vide")
    
    def __str__(self):
        return f"LIFO({self._stack})"