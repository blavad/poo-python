# TP n°2 : Classes, objets et encapsulation

Dans ce TP, on s'intéresse à ... Les compétences travaillées durant cette activité sont les suivantes : 
- Définir des classes et instancier des objets
- Utiliser des constructeurs
- Comprendre le concept d'encapsulation et savoir l'utiliser convenablement
- Utiliser les bonnes pratiques de déclaration des attributs et méthodes d'une classe

## Partie I : Instancier et manipuler des objets usuels 
40 min

**Manipuler des listes**

1. Définir la liste  `liste1 = [11, 40,18,5,56]`, puis effectuer les actions suivantes :
    - ajouter l’élément 12 à la liste et afficher la liste
    - trier et afficher la liste
    - renverser et afficher la liste
    - afficher l’indice de l’élément 18
    - enlever lélément 40 et afficher la liste 
    - afficher la sous-liste du 2e au 3e élément
    - afficher la sous-liste du début au 4e élément
    - afficher la sous-liste du 3e élément à la fin de la liste 
    - afficher le dernier élément en utilisant l’indiçage négatif.


1. Utiliser la fonction `range()` pour créer :
    - la liste des entiers de 0 à 14
    - la liste des entiers de 11 à 17
    - la liste des entiers de 3 à 120 par pas de 3.
    - la liste des entiers de 3 à 120 par pas de 3.

1. Utiliser la fonction `range()` et / ou une liste en compréhension pour:
    - ajouter 3 à chaque élément de la liste `[5, 8, 10]`.
    - ajouter 3 à chaque élément d'une liste de 0 à 10, mais seulement si l'élément est supérieur ou égal à 3.
    - définir la liste des nombres flottants compris entre -1 et 1 avec un décalage de 0.01.
    - créer la liste `['pt', 'ph', 'py', 'ot', 'oh', 'oy']` à partir des chaînes `'po'` et `'thy'`. 
        
        ***Aide*** : on pourra utiliser deux boucles for imbriquées.

**Manipuler des ensembles**

Définir deux ensembles $A = \{3, 7, 8, 10\}$ et $B = \{2, 7, 10\}$, puis affichez les résultats suivants :
- le test d'appartenance de 8 à l'ensemble A
- le test d'appartenance de 3 à l'ensemble B
- les ensembles $A - B$ et $B-A$
- l'ensemble $A \cup B$ (l'union)
- l'ensemble $A \cap B$ (l'intersection)
- le test d'inclusion du sous-ensemble $\{8, 10\}$ dans l'ensemble A


***Aide*** : on pourra afficher toutes les méthodes de la classe `set` grâce à la méthode built-in `__dir__` 

**Manipuler des dictionnaires**

1. Définir les dictionnaires suivants `shape1 = {'shape': 'circle', 'position': {'x': 10, 'y': 10}, 'radius': 4}`, puis effectuer les actions suivantes:
    - afficher toutes les clés du dictionnaire
    - vérifier que `'position'` est une clé du dictionnaire 
    - vérifier que `'circle'` est une valeur du dictionnaire 
    - supprimer la donnée associée dont la clé est `'radius'`
    - modifier la valeur de la clé `'shape'` en `'square'`
    - ajouter le couple  clé='side' et valeur=4 au dictionnaire

1. Utiliser un dictionnaire en compréhension pour:
    - créer un dictionnaire `dict_pow` dont les clés sont les entiers allant de -5 à 5 et les valeurs sont ces même entiers mis au carré. 
    
        **Note :** donner de façon explicite le type de ce dernier

    - soit la liste `['POO', 'Python', 'Travaux Pratiques']`. Créer un dictionnaire `dict_len` dont les clés sont ces chaînes de caractères et les valeurs sont le nombre de lettres dans chacune de ces chaînes.  
    
        **Note :** donner de façon explicite le type de ce dernier

    - Fusionner les deux précédents dictionnaires de deux manière différentes:
        - 1ère méthode : utiliser l'opérateur union `d1 | d2`
        - 2ème méthode : mettre à plat le contenu des dictionnaires existants dans un dictionnaire en cours de construction grâce à l'opérateur de mise à plat `**d`. 



## Partie II : Créer nos premiers objets
1h00

Dans la suite des exercices, on prendra soin de respecter les règles suivantes :
- le nom des variables est clair et explicite 
- un fichier différent par classe et programme principal
- les types sont définis de manière explicite (normes PEP 483)
- la nomenclature python des attributs public, protégés et privés est respectée

**Création de piles**
1. Implémentez une pile LIFO (**L**ast **I**n **F**irst **O**ut) avec une liste. Pour cela, définir trois fonctions :
    - `__init__` : qui construit une pile à partir d’une liste variable d’éléments passés en paramètres
    - `empile` : empile un élément en haut de la pile
    - `depile` : dépile un élément du haut de la pile
    - `__str__` : renvoie une chaîne de caractère représentant la pile (exemple : `"LIFO([0, 5, 12])"`)

1. Exécuter le programme `test_lifo.py` pour vérifiez que votre code est correcte. Faire les modifications si ce n'est pas le cas. 

1. De la même manière, implémentez une pile FIFO (**F**irst **I**n **F**irst **O**ut) avec une liste. Pour cela, définir trois fonctions :
    - `__init__` : qui construit une pile à partir d’une liste variable d’éléments passés en paramètres
    - `empile` : empile un élément en haut de la pile
    - `depile` : dépile un élément du bas de la pile
    - `__str__` : renvoie une chaîne de caractère représentant la pile (exemple : `"FIFO([0, 5, 12])"`)

1. Exécuter le programme `test_fifo.py` pour vérifiez que votre code est correcte. Faire les modifications si ce n'est pas le cas.

1. Créer une interface de programmation `IPile` contenant les méthodes `empile` et `dépile`. 

1. Faire hériter les classes `LIFO` et `FIFO` de `IPile`.


1. Modifier l'interface `IPile` pour qu'elle manipule des types d'objets explicitement spécifiés par l'utilisateur. Nous pourrons nous aider de l'exemple de la classe `LogGeneric` ci-dessous.

    Exemple de définition d'une classe générique en python.

    ```python
    from typing import TypeVar, Generic
    
    T = TypeVar('T')

    class LogGeneric(Generic[T]):
        def __init__(self, name: str, value: T) -> None:
            self._name = name
            self._value = value

        def set(self, new: T) -> None:
            self._value = new

        def get(self) -> T:
            return self._value

        def log(self) -> None:
            print(f"name={self._name} value={self._value}")
    ```
    Exemple d'utilisation d'une classe générique en python.
    ```python
    loggerFloat : LogGeneric[float] = LogGeneric("example1", 3.25)
    loggerList.log() # name=example1 value=3.25

    loggerList : LogGeneric[list] = LogGeneric("example2", [1, 2])
    loggerList.log() # name=example2 value=[1, 2]
    loggerList.set([4, 6, 8, 10, 12])
    loggerList.log() # name=example2 value=[4, 6, 8, 10, 12]
    ```
1. Changer les classes `LIFO` et `FIFO` en conséquence.

1. Créer une classe `PilePile` dont l'usage est tel

```python
lifo1 = LIFO()
lifo2 = LIFO()
lifo3 = FIFO()

pile = PileManager()
pile.empile(lifo1)
pile.empile(lifo2)
pile.empile(lifo3)
```