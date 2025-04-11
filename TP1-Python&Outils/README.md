# TP n°1 : Travailler avec python et ses outils

Dans ce TP, on s'intéresse aux fondements du langage python. Les compétences travaillées durant cette activité sont les suivantes :

- Comprendre et utiliser l'interpréteur python
- Utiliser un environnement virtuel python
- Créer un package et des modules python
- Lancer et utiliser l'interpréteur interactif
- Comprendre et utiliser le gestionnaire de paquets `pip`

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

**Premiers modules**

1. Le dossier `TP1-Python` est notre **package**
2. Dans le dossier `TP1-Python` créer un autre dossier nommé `tp1` et naviguer dedans (ce dossier contient le code source de notre package)
3. Dans le dossier `TP1-Python/tp1` créer le fichier `main.py` avec le contenu:
   ```python
    print("> ------------------------------")
    print("> Module main")
    print("> ------------------------------")
   ```
4. Exécuter ce fichier en utilisant l'interpréteur. Indiquer la commande utilisée dans le compte-rendu.
5. Exécuter le module `tp1.main`. Que se passe-t-il ?
   > on utilisera pour cela la commande `python -m tp1.main`.
6. Exécuter la commande `python -m tp1`. Que se passe-t-il ?
7. Renommer le fichier `main.py` en `__main__.py` et réessayer. Conclure.
8. Dans le dossier `TP1-Python/tp1/math` créer le module `addition.py` avec le contenu:

   ```python
   def addition(a, b):
      return a + b

   print("Hey, 3 + 2 = ", addition(3, 2))
   ```

9. Exécuter ce module. Indiquer la commande utilisée dans le compte-rendu.

**Plus de modules**

On souhaite désormais utiliser la fonction `addition` dans notre programme `__main__.py`.

12. Importer la fonction `addition` dans le fichier `__main__.py` et changer la ligne `print("> Module 'main'")` par `print(addition(8,8))`. Qu'observe-t-on ?

1. Corriger ce problème.

   > 💡 on pourra utiliser la variable build-in `__name__`

1. Dans le dossier `tp1/tp1/math` créer le fichier `__init__.py` avec le contenu:
   ```python
   from .addition import addition
   ```
   Changer en conséquence l'importation de la fonction `addition` dans `__main__.py`
   ```python
   from tp1.math import addition
   ```
1. Ajouter une fonction `np_addition` au module `tp1.math`

   Cette fonction prend deux listes en entrée, les transforme en array numpy et calcule leur somme.

1. (Optionnel) Ajouter une fonction `aire` au module `tp1.math`.

   Cette fonction calcule l'aire d'un cercle en fonction de son rayon.

   - $aire = \pi r^2$
   - On utilisera la constante [`pi`](https://docs.python.org/3/library/math.html#math.pi) du paquet [`math`](https://docs.python.org/3/library/math.html#math.pi)

1. _(Optionnel)_ Dans `tp1`, créer le module `tp1.argv` qui affiche le nombre et la liste des arguments passés en paramètre.

## Déjà terminé ?

Vous pouvez dès à présent commencer [le TP n°2 sur les classes et les objets en python](../TP2-ClassesObjets/README.md).
