# Correction TP n°2 : Classes et objets

## Partie II : Instancier et manipuler des objets usuels 
1h30

Dans cette partie : 🚩 = commande + résultat

**Manipuler des listes**

1. Définir la liste  `liste1 = [11, 40, 18, 5, 56]`, puis effectuer les actions suivantes :
    - ajouter l’élément 12 à la liste et afficher la liste 🚩
    - trier et afficher la liste
    - renverser et afficher la liste
    - afficher l’indice de l’élément 18 🚩
    - enlever l'élément 40 et afficher la liste 
    - afficher la sous-liste du 2e au 3e élément 🚩 
    - afficher la sous-liste du début au 4e élément
    - afficher la sous-liste du 3e élément à la fin de la liste 
    - afficher le dernier élément en utilisant l’indiçage négatif. 🚩

```python
liste1 = [11, 40, 18, 5, 56]
liste1.append(12)
print(liste1)
liste1.reverse()
print(liste1)
print(liste1.index(18))
liste1.remove(40)
print(liste1[1:3])
print(liste1[:4])
print(liste1[3:])
print(liste1[-1])
```


1. Utiliser la fonction `range()` pour créer :
    - la liste des entiers de 0 à 14 🚩
    - la liste des entiers de 11 à 17
    - la liste des entiers de 3 à 120 par pas de 3. 🚩

    
```python
l1 = list(range(15))
l2 = list(range(11, 18))
l3 = list(range(3, 121, 3))
```

1. Utiliser la fonction `range()` et / ou une liste en compréhension pour:
    - ajouter 3 à chaque élément de la liste `[5, 8, 10]`. 🚩
    - ajouter 3 à chaque élément d'une liste de 0 à 10, mais seulement si l'élément est supérieur ou égal à 3. 🚩
    - définir la liste des nombres flottants compris entre -1 et 1 avec un décalage de 0.01.
    - créer la liste `['pt', 'ph', 'py', 'ot', 'oh', 'oy']` à partir des chaînes `'po'` et `'thy'`. 
        
        ***Aide*** : on pourra utiliser deux boucles for imbriquées.


```python
l1 = [x + 3 for x in [5, 8, 10]]
l2 = [x + 3 for x in range(11) if x >= 3]
l3 = [x / 100 for x in range(-100, 101)]
l4 = [x + y for x in "po" for y in "thy"]
```

**Manipuler des ensembles**

Définir deux ensembles $A = \{3, 7, 8, 10\}$ et $B = \{2, 7, 10\}$, puis affichez les résultats suivants :
- le test d'appartenance de 8 à l'ensemble A 🚩
- le test d'appartenance de 3 à l'ensemble B 
- les ensembles $A - B$ et $B-A$ 
- l'ensemble $A \cup B$ (l'union) 🚩
- l'ensemble $A \cap B$ (l'intersection) 🚩
- le test d'inclusion du sous-ensemble $\{8, 10\}$ dans l'ensemble A


***Aide*** : on pourra afficher toutes les méthodes de la classe `set` grâce à la méthode built-in `__dir__` 


```python
A = {3, 7, 8, 10}
B = {2, 7, 10}

print(8 in A)
print(3 in B)
print(A - B)
print(B - A)
print(A.union(B))
print(A.intersection(B))
print({8, 10}.issubset(A))
```

**Manipuler des dictionnaires**

1. Définir les dictionnaires suivants `shape1 = {'shape': 'circle', 'position': {'x': 10, 'y': 10}, 'radius': 4}`, puis effectuer les actions suivantes:
    - afficher toutes les clés du dictionnaire 🚩
    - vérifier que `'position'` est une clé du dictionnaire  🚩
    - vérifier que `'circle'` est une valeur du dictionnaire 
    - supprimer la donnée associée dont la clé est `'radius'`
    - modifier la valeur de la clé `'shape'` en `'square'` 🚩
    - ajouter le couple  clé='side' et valeur=4 au dictionnaire 🚩

```python
print(shape1.keys())
print('position' in shape1)
print('circle' in shape1.values())
del shape1['radius']
shape1['shape'] = 'square'
shape1['side'] = 4
```

2. Utiliser un dictionnaire en compréhension pour:
    - créer un dictionnaire `dict_pow` dont les clés sont les entiers allant de -5 à 5 et les valeurs sont ces même entiers mis au carré. 🚩
    
        **Note :** donner de façon explicite le type de ce dernier

    - soit la liste `['POO', 'Python', 'Travaux Pratiques']`. Créer un dictionnaire `dict_len` dont les clés sont ces chaînes de caractères et les valeurs sont le nombre de lettres dans chacune de ces chaînes.  🚩
    
        **Note :** donner de façon explicite le type de ce dernier

    - Fusionner les deux précédents dictionnaires de deux manière différentes:
        - 1ère méthode : utiliser l'opérateur union `d1 | d2`
        - 2ème méthode : mettre à plat le contenu des dictionnaires existants dans un dictionnaire en cours de construction grâce à l'opérateur de mise à plat `**d`. 

```python
dict_pow : dict[int, int] = { x: x**2 for x in range(-5, 6)}

dict_len : dict[string, int] = { x : len(x) for x in ['POO', 'Python', 'Travaux Pratiques']}

dict_fusion_1 = dict_pow | dict_len
dict_fusion_2 = {**dict_pow, **dict_len}
```
