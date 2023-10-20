# Compte Rendu TP 2

## Informations
- **Nom :** SEVERINO
- **Prénom :** Hugo


## Partie I

# 


3. A quoi servent les méthodes __eq__, __dir__, __ge__, __str__, __repr__, __sizeof__, __getattribute__ et __hash__ ? 
- La méthode `__eq__` permet de comparer deux objets. C'est la méthode appelé par l'opérateur `==`.
- La méthode `__dir__` retourne toutes les propriétés et méthodes d'un objet, sans les valeurs.

- La méthode `__ge__` est l'équivalent de `__eq__`, mais pour l'opérateur `>=`

- La méthodes `__str__` permet de retourner notre objet sous la forme d'une texte. 

- La méthode `__repr__` retourne une string "lisible" de notre objet. 

- La méthode `__sizeof__` retourne la taille de notre objet en Bytes. 

- La méthode `__getattribute__` retourne la valeur d'un attribut spécifique de ntore classe

- La méthode `__hash__` retourne une valeur int permettant de comparer rapidement des valeurs (par ex 1 et 1.0 seront identiques)

4. A quoi servents les méthodes `__int__`, `__pow__`, `__trunc__` ? (Pour un Float)

- La méthode `__int__` retourne une valeur entière de notre nombre décimal. 

- La méthode `__pow__` permet d'effectuer un calcul de puissance entre deux nombres. 

- La méthode `__trun__` permet d'afficher l'arrondi par défault. 

5. A quoi servents les méthodes `upper`, `lower`, `find`, `split` et `join` ? (Pour un str)

- La méthode `__upper__` renvoie la chaine de caractère en lettre capitales. `__lower__` en minuscule. 

- La méthode `__find__` permet de connaître la position de notre donnée d'entrée dans la chaine de caractère. 

- La méthode `__split__` permet de diviser notre chaîne. 

- La méthode `__join__` permet de joindre plusieurs str. 

6. A quoi servents les méthodes `keys`, `values` et `items` ? (Dict) 

- La méthode `__keys__` permet de retourner les clefs de notre dictionnaire, `__values__` les valeurs et `__items__` les catégories. 


## Partie II

1. Afin d'ajouter la valeur 12 à notre liste, on effectue la commande `liste1.append(12)`

1. Afin d'afficher l'indice de l'élément 18, on effectue la commande `liste1.index(18)`

1. Afin d'afficher la liste du 2 et 3 eme élement on effectue la commande `liste1[1:2]`

1. Pouir afficher le dernier élément, on utilise `liste1[-1]`

1. Pour creer une liste des entiers de 0 à 14, on utilise `liste2= list(range(14))`

1. Pour creer une liste de la liste des entiers de 3 à 120 par pas de 3 on utilise `liste4 = list(range(3,120,3))`

1. Pour ajouter 3 à chaque élément de la liste `[5, 8, 10]`, on utilisera 
```python
liste5 = [5,8,10]

liste6 = [x+3 for x in liste5]
```

1. Pour ajouter 3 à chaque élément d'une liste de 0 à 10, mais seulement si l'élément est supérieur ou égal à 3: 
```python

liste7 = [x for x in range(11)]
liste8 = [x+3 if x>2  else x for x in liste7]
```

1. pour effectuer le test d'appartenance de 8 à l'ensemble A : 
```python
A={3,7,8,10}
B={2,7,10}

print(8 in A)
```

1. Afin d'afficher l'ensemble $A \cup B$ (l'union), on effectue la commande `print(A.union(B))`, pour l'intersection : `print(A.intersection(B))`

1. Afin d'afficher toute les clefs du dictionnaire on utilisera `print(shape1.keys())`

1. afin de vérifier si position est dans notre clef `print("position" in shape1.keys())`

1. Pour modifier la valeur d'une clef : `shape1['square'] = shape1.pop('shape')`

1. Pour ajouter une clef et sa valeur : `shape1["side"]=4`

1. Pour créer un dictionnaire `dict_pow` dont les clés sont les entiers allant de -5 à 5 et les valeurs sont ces même entiers mis au carré : 
```python
dict_pow: dict[int,int]={x:x*x for x in range(-5,6)}
```

1. Poiur : la liste `['POO', 'Python', 'Travaux Pratiques']`. Créer un dictionnaire `dict_len` dont les clés sont ces chaînes de caractères et les valeurs sont le nombre de lettres dans chacune de ces chaînes. `dict_len : dict[str,int] = {x :len(x) for x in dic}`


    



