# TP n°2 : Classes et objets

Dans ce TP, on s'intéresse  à l'utilisation d'objets usuels python. Les compétences travaillées durant cette activité sont les suivantes : 
- Comprendre le typage dynamique
- Manipuler des listes en python
- Manipuler des ensembles en python
- Manipuler des disctionnaires en python 
- Instancier des objets


## Partie I : Comprendre la notion d'objet et de typage dynamique en python 
45min

**Manipuler nos premiers objets**
1. Commencer par regarder cette [vidéo sur les notions de variables, objets et typage dynamique en python](https://www.youtube.com/watch?v=vSsTKNCSKnU).
1. Lancer l'interpréteur python en mode interactif

Dans les versions récentes de python, tout est objet. En effet, les types intégrés à python héritent tous de la même classe parente `object`. C'est le cas notamment de `bool`, `int`, `float`, `str`, `list`, `dict`, `set`, etc.


3. Exécuter les instructions suivantes:
   
   Instancier la classe objet:
   ```python
   obj = object()
   ```

   Afficher son type: 
   ```python
   print(type(obj))
   ```

   Afficher ses attributs et méthodes:
   ```python
   print(dir(obj))
   ```
   
   ***Note :*** On distingue les méthodes built-in des autres par leur notation particulière `__method__`
   
   Afficher le résultat de l'appel de quelques-unes de ces méthodes:
   ```python
   # Exemple appel méthode __str__
   print(obj.__str__())

   # OU 
    
   print(str(obj))
   ```
   A quoi servent les méthodes `__eq__`, `__dir__`, `__ge__`, `__str__`, `__repr__`, `__sizeof__`, `__getattribute__` et `__hash__` ?  🚩

1. Réaliser les mêmes opérations appliquées à une chaîne de caracètes.

   A quoi servents les méthodes `upper`, `lower`, `find`, `split` et `join` ? 🚩



## Partie II : Instancier et manipuler des objets usuels 
1h00

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


1. Utiliser la fonction `range()` pour créer :
    - la liste des entiers de 0 à 14 🚩
    - la liste des entiers de 11 à 17
    - la liste des entiers de 3 à 120 par pas de 3. 🚩

1. Utiliser une liste en compréhension pour:
    - ajouter 3 à chaque élément de la liste `[5, 8, 10]`. 🚩
    - ajouter 3 à chaque élément d'une liste de 0 à 10, mais seulement si l'élément est supérieur ou égal à 3. 🚩
    - définir la liste des nombres flottants compris entre -1 et 1 avec un décalage de 0.01.
    - créer la liste `['pt', 'ph', 'py', 'ot', 'oh', 'oy']` à partir des chaînes `'po'` et `'thy'`. 
        
        ***Aide*** : on pourra utiliser deux boucles for imbriquées.

<!-- 

**Manipuler des ensembles**

Définir deux ensembles $A = \{3, 7, 8, 10\}$ et $B = \{2, 7, 10\}$, puis affichez les résultats suivants :
- le test d'appartenance de 8 à l'ensemble A 🚩
- le test d'appartenance de 3 à l'ensemble B 
- les ensembles $A - B$ et $B-A$ 
- l'ensemble $A \cup B$ (l'union) 🚩
- l'ensemble $A \cap B$ (l'intersection) 🚩
- le test d'inclusion du sous-ensemble $\{8, 10\}$ dans l'ensemble A -->


***Aide*** : on pourra afficher toutes les méthodes de la classe `set` grâce à la méthode built-in `__dir__` 

## Partie III : Créer des fonctions et des modules 
45min

1. Ecrire un programme qui lit un nombre et affiche "+", "0", "-" selon que le nombre est positif, nul ou négatif.
1. Ecrire un programme qui calcule et affiche les carrés des 10 premiers entiers :
    - d'abord avec une boucle **while**
    - puis en utilisant une boucle **for**
1. Ecrire une fonction `sum` qui calcule la somme des éléments d’une liste.
1. Ecrire une fonction `moyenne` qui calcule la moyenne des éléments d’une liste.
1. Ecrire un programme qui affiche la table de multiplications (de 1 à 10).


**Manipuler des dictionnaires**

1. Définir les dictionnaires suivants `shape1 = {'shape': 'circle', 'position': {'x': 10, 'y': 10}, 'radius': 4}`, puis effectuer les actions suivantes:
    - afficher toutes les clés du dictionnaire 🚩
    - vérifier que `'position'` est une clé du dictionnaire  🚩
    - vérifier que `'circle'` est une valeur du dictionnaire 
    - supprimer la donnée associée dont la clé est `'radius'`
    - modifier la valeur de la clé `'shape'` en `'square'` 🚩
    - ajouter le couple  clé='side' et valeur=4 au dictionnaire 🚩

1. Utiliser un dictionnaire en compréhension pour:
    - créer un dictionnaire `dict_pow` dont les clés sont les entiers allant de -5 à 5 et les valeurs sont ces même entiers mis au carré. 🚩
    
        **Note :** donner de façon explicite le type de ce dernier

    - soit la liste `['POO', 'Python', 'Travaux Pratiques']`. Créer un dictionnaire `dict_len` dont les clés sont ces chaînes de caractères et les valeurs sont le nombre de lettres dans chacune de ces chaînes.  🚩
    
        **Note :** donner de façon explicite le type de ce dernier

    - Fusionner les deux précédents dictionnaires de deux manière différentes:
        - 1ère méthode : utiliser l'opérateur union `d1 | d2`
        - 2ème méthode : mettre à plat le contenu des dictionnaires existants dans un dictionnaire en cours de construction grâce à l'opérateur de mise à plat `**d`. 

## Déjà terminé ?

Vous pouvez dès à présent commencer [le TP n°3 sur l'encapsulation](../TP3-Encapsulation/README.md).