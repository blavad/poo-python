# TP n°3 : Classes, objets, encapsulation

Dans ce TP, on s'intéresse à l'implémentation de classes et l'utilisation des instances de classes (les objets) en python. Nous aborderons également la notion d'encapsulation et d'héritage. Les compétences travaillées durant cette activité sont les suivantes : 
- Implémenter des classes et instancier des objets
- Implémenter un constructeur 
- Utiliser des attributs et méthodes d'instance 
- Comprendre le concept d'encapsulation et savoir l'utiliser convenablement
- Utiliser les bonnes pratiques de codage python

## Partie I : Pokémon
45min

Les Pokémon sont certes de très mignonnes créatures, mais ils sont également un bon exemple pour illustrer l’héritage. 

Commencez par créer une classe Pokemon qui contient (entre autres) :
- un attribut `nom` qui contient le nom du Pokémon.
- un attribut `hp` (pour Health Points) qui représente les points de vie du Pokémon.
- un attribut `atk` qui représente la force de base de l’attaque du Pokémon.
- un `constructeur` pour instancier des Pokémon adéquatement.
- des `getters` (accesseurs) qui permettent de consulter les attributs (name et hp) du Pokémon.
- une méthode `estMort()` qui retourne un boolean pour indiquer si un Pokémon est mort (hp == 0) ou non.
- une méthode `attaquer(self, p: Pokemon) -> None` qui permet au Pokémon appelant d’attaquer le Pokémon passé en paramètre. L’attaque déduit `atk` points de la vie `hp` du Pokémon attaqué `p`.
- une redéfinition de la méthode `__str__` qui renvoie une chaîne de caractères permettant d'afficher les informations du Pokémon (ex: `Pokemon(nom=Bulbizarre, hp=20, atk=5)`).

En plus des Pokémon normaux (décrits à travers la classe Pokemon) on recense trois types de Pokémon. Les Pokémon de type Feu, les Pokémon de type Eau et les Pokémon de type Plante :
- les Pokémon de type Feu sont super efficaces contre les Pokémon de type *Plante* et leur infligent deux fois plus de dégâts `(2*atk)`. Par contre, ils sont très peu efficaces contre les Pokémon de type Eau ou de type Feu et ne leur infligent que la moitié des dégâts `(0.5*atk)`. Ils infligent des dégâts normaux aux Pokémon de type Normal.
- les Pokémon de type Eau sont super efficaces contre les Pokémon de type Feu et leur infligent deux fois plus de dégâts `(2*atk)`. Par contre, ils sont très peu efficaces contre les Pokémon de type Eau ou de type Plante et ne leur
infligent que la moitié des dégâts `(0.5*atk)`. Ils infligent des dégâts normaux
aux Pokémon de type Normal.
- enfin, les Pokémon de type Plante sont super efficaces contre les Pokémon de type Eau et leur infligent deux fois plus de dégâts `(2*atk)`. Par contre, ils sont très peu efficaces contre les Pokémon de type Plante ou de type Feu et ne leur
infligent que la moitié des dégâts `(0.5*atk)`. Ils infligent des dégâts normaux aux Pokémon de type Normal.


Créez trois classes `PokemonFeu`, `PokemonEau` et `PokemonPlante` qui héritent de la classe Pokemon et qui représentent les trois types de Pokémon mentionnés ci-dessus. Ensuite, amusez-vous à faire des combats de Pokémon.

⚠️ **Remarque :** Afin de reconnaître le type d'un Pokemon, nous pourrons utiliser la fonction python `isinstance`. 

```python
# Exemple d'utilisation de "isinstance"

pokemon = PokemonFeu("Salamèche", 60, 10)

print(isinstance(pokemon, PokemonFeu)) # True
print(isinstance(pokemon, PokemonEau)) # False

```

## Partie II : Les piles
30min

Dans la suite des exercices, on prendra soin de respecter les règles suivantes :
- le nom des variables est clair et explicite 
- un fichier différent par classe et programme principal
- les types sont définis de manière explicite (normes PEP 483)
- la nomenclature python des attributs public, protégés et privés est respectée

**Les piles**

1. Implémentez une pile LIFO (**L**ast **I**n **F**irst **O**ut) avec une liste. Pour cela, créer une classe `LIFO` dans un fichier `lifo.py` et définir trois fonctions :
    - `__init__` : qui construit une pile à partir d’une liste variable d’éléments passés en paramètres
    - `empile` : empile un élément en haut de la pile
    - `depile` : dépile un élément du haut de la pile
    - `__str__` : renvoie une chaîne de caractère représentant la pile (exemple : `"LIFO([0, 5, 12])"`)

1. Exécuter le programme `test_lifo.py` pour vérifiez que votre code est correcte. Faire les modifications si ce n'est pas le cas. 

1. De la même manière, implémentez une pile FIFO (**F**irst **I**n **F**irst **O**ut) avec une liste. Pour cela,  créer une classe `FIFO` dans un fichier `fifo.py` et définir trois fonctions :
    - `__init__` : qui construit une pile à partir d’une liste variable d’éléments passés en paramètres
    - `empile` : empile un élément en haut de la pile
    - `depile` : dépile un élément du bas de la pile
    - `__str__` : renvoie une chaîne de caractère représentant la pile (exemple : `"FIFO([0, 5, 12])"`)

1. Exécuter le programme `test_fifo.py` pour vérifiez que votre code est correcte. Faire les modifications si ce n'est pas le cas.


## Partie III : Interfaces de programmation
15min

1. Créer une interface de programmation `IPile` contenant les méthodes `empile` et `dépile`. 

1. Faire hériter les classes `LIFO` et `FIFO` de `IPile`.

1. Selon vous, à quoi peut service la création d'interfaces ? 🚩

## Partie IV : Généricité et héritage
1h00

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

1. Dans un fichier `test_pile.py`, créer une fonction `test_pile` qui prend en argument une pile quelconque d'entiers (c.à.d une pile qui vérifie l'interface `IPile[int]`) et qui réalise les opérations suivantes:
    - affiche la pile, empile 5; affiche la pile; empile 8; affiche la pile; dépile; affiche la pile; dépile; 

    ***Note :*** On veillera à bien déclarer les types de retour et des arguments de la fonction.

1. Créer dans ce même fichier un programme principal exécutant cette fonction sur une pile FIFO vide, sur une FIFO initialisée avec le liste `[1, 2, 3]` et sur une pile LIFO vide. Tester ce programme.  

1. Dans un fichier `pile_multiple.py`, créer un classe `PileMultiple` qui n'est autre qu'une pile composée de plusieurs piles d'entiers. Définir trois fonctions :
    - `__init__` : qui construit une pile à partir d’une liste variable de piles passées en paramètres
    - `empile` : empile un entier dans chacune des sous-piles
    - `depile` : dépile un entier dans chacune des sous-piles
    - `__str__` : renvoie une chaîne de caractère représentant la pile (exemple : `"PileMultiple([ LIFO([0, 5, 12]), FIFO([1, 2, 3]) ])"`)

    De quoi hérite cette classe ? Déclarer cette héritage dans votre code. 🚩

1. Dans le programme principal du fichier `test_pile.py`

    - créer une pile multiple constituée de deux piles FIFO et d'une pile LIFO 
    - créer une pile multiple constituée d'une pile LIFO et de la pile multiple précédente 

    Appliquer la fonction `test_pile` à ces deux piles multiples. Tester ce programme et vérifier que le résultat est cohérent.
    
## Déjà terminé ?

Vous pouvez reprendre la **Partie I: Pokemon** et aller plus loin dans la conception du jeu vidéo Pokemon. On pourra par exemple introduire les notions suivantes :
- `Dresseur` : C'est quelqu'un qui a attrapé un ou plusieurs Pokémons et qui fait des combats de Pokémons contre d'autres dresseurs. Il se charge de l'éducation de ses créatures et de leur entraînement.
- `Equipe` : L'équipe de Pokémon que le dresseur a sur lui. Il ne peut porter que 6 Pokémon au maximum sur lui, il est interdit par la loi d'en avoir plus.
- `Pokedex` : Objet qui permet de recenser les nombreuses espèces de Pokémon. C'est une encyclopédie électronique qui enregistre le poids, la taille, et même l'empreinte du Pokémon, et qui donne une description et les caractéristique du monstre rencontré. 
- `Pokeball` : Objet rond, rouge et blanc, qui permet d'attraper les Pokémon. Lorsque le Pokémon sauvage est affaibli, le dresseur lance une Poké Ball vierge dessus. Elle aspirera la créature et l'enfermera dedans si le Pokémon est trop faible pour y échapper. Elle sert ensuite de maison au Pokémon apprivoisé : le Pokémon y passe le plus clair de son temps et en sort pour combattre ou se restaurer.

Les définitions des termes ci-dessus sont tirés du site [Pokebip](https://www.pokebip.com/page/general/lexique).