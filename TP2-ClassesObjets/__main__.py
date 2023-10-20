

liste1 = [11, 40, 18, 5, 56]

# ajouter l’élément 12 à la liste et afficher la liste

liste1.append(12)

print(liste1)

#trier et afficher la liste

liste1.sort()

print(liste1)

#renverser et afficher la liste
liste1.sort(reverse = True)
print(liste1)

#afficher l’indice de l’élément 18

print(liste1.index(18))

#enlever l'élément 40 et afficher la liste

liste1.remove(40)
print(liste1)

#afficher la sous-liste du 2e au 3e élément

print(liste1[1:2])

#afficher la sous-liste du début au 4e élément

print(liste1[:3])

#afficher la sous-liste du 3e élément à la fin de la liste 

print(liste1[2:])

#afficher le dernier élément en utilisant l’indiçage négatif.

print(liste1[-1])

#Utiliser la fonction `range()` pour créer :la liste des entiers de 0 à 14 

liste2= list(range(14))

#la liste des entiers de 11 à 17

liste3= list(range(11,17))

#la liste des entiers de 3 à 120 par pas de 3.

liste4 = list(range(3,120,3))

#Utiliser la fonction `range()` et / ou une liste en compréhension pour: ajouter 3 à chaque élément de la liste `[5, 8, 10]`.

liste5 = [5,8,10]

liste6 = [x+3 for x in liste5]

print(liste6)

#ajouter 3 à chaque élément d'une liste de 0 à 10, mais seulement si l'élément est supérieur ou égal à 3. 

liste7 = [x for x in range(11)]
liste8 = [x+3 if x>2  else x for x in liste7]

print(liste8)

#définir la liste des nombres flottants compris entre -1 et 1 avec un décalage de 0.01.

liste9= [x/100 for x in range(-100,101)]
print(liste9)

#créer la liste `['pt', 'ph', 'py', 'ot', 'oh', 'oy']` à partir des chaînes `'po'` et `'thy'`. 

po="po"
thy="thy"
liste10=[]
for i in range(len(po)):
    for j in range(len(thy)):
        liste10.append(po[i]+thy[j])

print(liste10)

#Définir deux ensembles A={3,7,8,10} et B={2,7,10}, puis affichez les résultats suivants :le test d'appartenance de 8 à l'ensemble A 
A={3,7,8,10}
B={2,7,10}

print(8 in A)
#le test d'appartenance de 3 à l'ensemble B 
print(3 in B)

#les ensembles $A - B$ et $B-A$ 

print(A.difference(B))
print(B.difference(A))

#l'ensemble $A \cup B$ (l'union)

print(A.union(B))

#l'ensemble $A \cap B$ (l'intersection) 

print(A.intersection(B))

#le test d'inclusion du sous-ensemble $\{8, 10\}$ dans l'ensemble A

print({8,10}.issubset(A)) #ou <

#Définir les dictionnaires suivants `shape1 = {'shape': 'circle', 'position': {'x': 10, 'y': 10}, 'radius': 4}`, puis effectuer les actions suivantes: afficher toutes les clés du dictionnaire

shape1 = {'shape': 'circle', 'position': {'x': 10, 'y': 10}, 'radius': 4}

print(shape1.keys())

# que `'position'` est une clé du dictionnaire

print("position" in shape1.keys())

#vérifier que `'circle'` est une valeur du dictionnaire 

print("circle" in shape1.values())

#supprimer la donnée associée dont la clé est `'radius'`

shape1.pop("radius")
print(shape1)

#modifier la valeur de la clé `'shape'` en `'square'` 

shape1['square'] = shape1.pop('shape')
print(shape1)

#ajouter le couple  clé='side' et valeur=4 au dictionnaire

shape1["side"]=4
print(shape1)

#Utiliser un dictionnaire en compréhension pour:créer un dictionnaire `dict_pow` dont les clés sont les entiers allant de -5 à 5 et les valeurs sont ces même entiers mis au carré. 

dict_pow: dict[int,int]={x:x*x for x in range(-5,6)}

print(dict_pow)

#soit la liste `['POO', 'Python', 'Travaux Pratiques']`. Créer un dictionnaire `dict_len` dont les clés sont ces chaînes de caractères et les valeurs sont le nombre de lettres dans chacune de ces chaînes.
dic=['POO', 'Python', 'Travaux Pratiques']

dict_len : dict[str,int] = {x :len(x) for x in dic}
print(dict_len)

#Fusionner les deux précédents dictionnaires de deux manière différentes:        - 1ère méthode : utiliser l'opérateur union `d1 | d2`        - 2ème méthode : mettre à plat le contenu des dictionnaires existants dans un dictionnaire en cours de construction grâce à l'opérateur de mise à plat `**d`

print({**dict_len,**dict_pow})
print(dict_len | dict_pow)