# TP n°1 : Les fondamentaux en Python

Dans ce TP, on s'intéresse aux fondements du langage python et de la programmation orientée objet dans ce langage. Les compétences travaillées durant cette activité sont les suivantes :

- Comprendre et utiliser l'interpréteur Python
- Créer un package et des modules python
- Utiliser un environnement virtuel python
- Comprendre et utiliser le gestionnaire de paquets `pip`
- Comprendre la notion d'objet en python

## Partie I : Interpréteur Python

15min

**Pour commencer**

1. Vérifier que python est bien installé (version >= 3.10)
2. Quelle est sa version par défaut ?
   - S'il s'agit de la version 2, vérifier que `python3` est également installé
   - Nous n'utiliserons **désormais plus que la version 3**
3. Lancer l'interpréteur en mode interactif pour calculer $3.5^{12}$.
4. Fermer l'interpréteur en mode interactif.

## Partie II : Modules et packages

1h00

**Premiers modules**

1. Le dossier `tp1` est notre **package**
2. Dans le dossier `tp1` créer un autre dossier nommé `tp1` et naviguer dedans (ce dossier contient le code source de notre package)
3. Dans le dossier `tp1/tp1` créer le fichier `main.py` avec le contenu:
   ```python
    print("> ------------------------------")
    print("> Module main")
    print("> ------------------------------")
   ```
4. Exécuter ce fichier en utilisant l'interpréteur. Indiquer la commande utilisé dans le compte-rendu.
5. Exécuter le module `tp1.main`. Que ce passe-t-il ?
   > on utilisera pour cela la commande `python -m tp1.main`.
6. Exécuter la commande `python -m tp1`. Que ce passe-t-il ?
7. Renommer le fichier `main.py` en `__main__.py` et réessayer. Conclure.
8. Dans le dossier `tp1/tp1/math` créer le module `addition.py` avec le contenu:

   ```python
   def addition(a, b):
      return a + b

   print("Hey, 3 + 2 = ", addition(3, 2))
   ```

9. Exécuter ce module. Indiquer la commande utilisé dans le compte-rendu.

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

## Partie III : Gestionnaire de paquets et environnements virtuels

30min

**Environnement virtuel**

<!-- 1. Créer un dossier `TP1-Python` et ouvrir un terminal à cet emplacement -->

1. Créer un environnement virtuel python avec le nom `.venv`.
1. Analyser le contenu du dossier `.venv`. Que contient-il ?
1. Activer cet environnement virtuel.
1. Afficher la liste des paquets installés dans l'environnement virtuel.
1. Comparer à la liste des paquets python installés sur votre machine
1. Installer les paquets `numpy` et `plotly`.
1. Afficher de nouveau la liste des paquets installés dans l'environnement virtuel.
1. Créer le fichier `requirements.txt` qui contient les dépendances de notre package.
1. Quelle commande devra être lancée par un autre développeur qui souhaiterait installer les dépendances du `requirements.txt`.

**Installer et utiliser notre module**

1. Sortir de l'environnement virtuel `.venv` et en créer un second nommé `.tp1-env`.
2. Dans ce second environnement virtuel, installer tous les requirements du fichier `requirements.txt` en une ligne. Indiquer la commande utilisé dans le compte-rendu.
3. Installer également votre package `tp1`.

   Dans le dossier `tp1/` où se situe le fichier `setup.py`, exécuter `pip install .`

4. Vérifier son installaton en exécutant le fichier `tests/test-tp1-install.py`

## Déjà terminé ?

Vous pouvez dès à présent commencer [le TP n°2 sur les objets et classes python](../TP2-ClassesObjets/README.md).
