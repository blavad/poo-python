# TP n°1 : Travailler avec python et ses outils

Dans ce TP, on s'intéresse aux fondements du langage python. Les compétences travaillées durant cette activité sont les suivantes :

- Comprendre et utiliser l'interpréteur python
- Lancer et utiliser l'interpréteur interactif
- Utiliser un environnement virtuel python
- Comprendre et utiliser le gestionnaire de paquets `pip`
- Créer un package et des modules python

## Partie I : Interpréteur Python

15min

**Pour commencer**

1. Vérifier que python est bien installé (version >= 3.10)
2. Quelle est sa version par défaut ?
   - S'il s'agit de la version 2, vérifier que `python3` est également installé
   - Nous n'utiliserons **désormais plus que la version 3**
3. Lancer l'interpréteur en mode interactif
4. Exécuter la suite d'instructions

   ```python
   # Déclarer une variable
   phrase = "Introduction à la programmation orientée objet"

   # Calculer la longueur d'une variable
   longueur = len(phrase)

   # Afficher la longueur
   print(longueur)

   # Compter le nombre de 'o'
   count_o = phrase.count('o')

   # Afficher le nombre de 'o'
   print(longueur)

   # Afficher le résultat d'un calcul compliqué
   print(3.5**24)
   ```

5. Fermer l'interpréteur en mode interactif.

## Partie II : Gestionnaire de paquets et environnements virtuels

30min

**Environnement virtuel**

1. Créer un dossier `TP1-Python` et ouvrir un terminal à cet emplacement
1. Créer un environnement virtuel python avec le nom `.venv`.
1. Analyser le contenu du dossier `.venv`. Que contient-il ?
1. Activer cet environnement virtuel.
1. Afficher la liste des paquets installés dans l'environnement virtuel.
1. Comparer à la liste des paquets python installés sur votre machine
1. Installer les paquets `numpy` et `plotly`.
1. Afficher de nouveau la liste des paquets installés dans l'environnement virtuel.
1. Créer le fichier `requirements.txt` qui contient les dépendances de notre package.
1. Quelle commande devra être lancée par un autre développeur qui souhaiterait installer les dépendances du `requirements.txt`.

## Partie III : Modules et packages

1h00

**Définitions**

Voici les définitions de module et de package.

<i>Définition 1 : Module</i>

```
En Python, un module est un fichier contenant des définitions de fonctions, de classes et de variables, ainsi que des instructions exécutables. En d'autres termes, c'est une manière d'organiser le code de manière logique et cohérente. Le nom du module est dérivé du nom du fichier (sans l'extension .py).
```

<i>Définition 2 : Package</i>

```
Un package est simplement un répertoire contenant un ou plusieurs modules et un fichier spécial __init__.py.
```

**Premiers modules**

1. Le dossier `TP1-Python` est notre dossier de travail.
2. Dans le dossier `TP1-Python`, créer un fichier `main.py` avec le contenu:
   ```python
    print("> ------------------------------")
    print("> Module main")
    print("> ------------------------------")
   ```
3. Exécuter ce fichier en utilisant l'interpréteur.
4. Exécuter le module `main`. Que se passe-t-il ?
   > on utilisera pour cela la commande `python -m main`.
5. Dans le dossier `TP1-Python/math_pkg` (notre package) créer le module `operations` avec le contenu:

   ```python
   def addition(a, b):
      return a + b

   print("Hey, 3 + 2 = ", addition(3, 2))
   ```

6. Exécuter ce module nommé `math_pkg.operations` d'après son chemin d'accès.

**Plus de modules**

On souhaite désormais utiliser la fonction `addition` dans notre programme `main.py`.

1.  Importer la fonction `addition` dans le fichier `main.py` et changer la ligne `print("> Module 'main'")` par `print(addition(8,8))`. Qu'observe-t-on ?

2.  Corriger ce problème.

    > 💡 on pourra utiliser la variable build-in `__name__`

3.  Dans le dossier `TP1-Python/math_pkg` créer le fichier `__init__.py` avec le contenu:
    ```python
    from .operations import addition
    ```
    Changer en conséquence l'importation de la fonction `addition` dans `main.py`
    ```python
    from math_pkg import addition
    ```
4.  Ajouter une fonction `aire` au module `math_pkg`.

    Cette fonction calcule l'aire d'un cercle en fonction de son rayon.

    - $aire = \pi r^2$
    - On utilisera la constante [`pi`](https://docs.python.org/3/library/math.html#math.pi) du paquet [`math`](https://docs.python.org/3/library/math.html#math.pi)

## Déjà terminé ?

Vous pouvez dès à présent commencer [le TP n°2 sur les classes et les objets en python](../TP2-ClassesObjets/README.md).
