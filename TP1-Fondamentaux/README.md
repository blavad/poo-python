# TP n°1 : Les fondamentaux en Python

Dans ce TP, on s'intéresse aux fondements du langage python et de la programmation orientée objet dans ce langage. Les compétences travaillées durant cette activité sont les suivantes : 

- Comprendre et utiliser l'interpréteur Python
- Créer un package et des modules python
- Utiliser un environnement virtuel python
- Comprendre et utiliser le gestionnaire de paquets `pip`
- Comprendre la notion d'objet en python

## Partie 0 : Mise en place
- Cloner ce repo : `git clone https://github.com/blavad/poo-python.git`
- Ouvrer un terminal à l'emplacement `poo-python/TP1-Fondamentaux`

Ce dossier est le votre pendant tout le TP. Toutes les manipulations doivent être faites à l'intérieur. Il contient déjà certains fichiers qui seront à lire et/ou compléter durant le TP.  

## Partie I : Interpréteur et package 
1h00

**Pour commencer**

1. Vérifier que python est bien installé (version >= 3.5)
1. Quelle est sa version par défaut ?
   - S'il s'agit de la version 2, vérifier que `python3` est également installé
   - Nous n'utiliserons **désormais plus que la version 3**
     
**Interpréteur et premiers modules**

3. Le dossier `tp1` est notre **package**
1. Dans le dossier `tp1` créer un autre dossier nommé `tp1` et naviguer dedans (ce dossier contient le code source de notre package)
1. Dans le dossier `tp1/tp1` créer le fichier `main.py` avec le contenu:
      ```python
       print("> ------------------------------")
       print("> Module main")
       print("> ------------------------------")
      ```
1. Exécuter ce fichier en utilisant l'interpréteur. Indiquer la commande utilisé dans le compte-rendu.  🚩
1. Exécuter le module `tp1.main`. Que ce passe-t-il ? 🚩
   > on utilisera pour cela la commande `python -m tp1.main`.
1. Exécuter la commande `python -m tp1`. Que ce passe-t-il ? 🚩
1. Renommer le fichier `main.py` en `__main__.py` et réessayer. Conclure. 🚩
1. Dans le dossier `tp1/tp1/math` créer le module `addition.py` avec le contenu:
      ```python
      def addition(a, b):
         return a + b
      
      print("Hey, 3 + 2 = ", addition(3, 2))
      ```
   
1. Exécuter ce module. Indiquer la commande utilisé dans le compte-rendu. 🚩

**Plus de modules**

On souhaite désormais utiliser la fonction `addition` dans notre programme `__main__.py`.

12. Importer la fonction `addition` dans le fichier `__main__.py` et changer la ligne `print("> Module 'main'")` par `print(addition(8,8))`. Qu'observe-t-on ? 🚩

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
1. *(Optionnel)* Dans `tp1`, créer le module `tp1.argv` qui affiche le nombre et la liste des arguments passés en paramètre.

## Partie II : Gestionnaire de paquets 
45min

**Environnement virtuel**
1. Revener dans le dossier `TP1-Fondamentaux`
1. Créer un environnement virtuel python avec le nom `.env`.
1. Analyser le contenu du dossier `.env`. Que contient-il ? 🚩
1. Activer cet environnement virtuel.
1. Afficher la liste des paquets installés dans l'environnement virtuel. 
1. Comparer à la liste des paquets python installés sur votre machine. 
1. Installer les paquets nécessaires au bon fonctionnement du module `tp1` (numpy).
   > On pourra valider que la commande `python -m tp1.tp1` s'exécute bien.

1. Créer le fichier `requirements.txt` qui contient les dépendances de notre package.
   
**Installer et utiliser notre module**

9. Sortir de l'environnement virtuel `.env` et en créer un second nommé `.tp1-env`. 
1. Dans ce second environnement virtuel, installer tous les requirements du fichier `requirements.txt` en une ligne. Indiquer la commande utilisé dans le compte-rendu. 🚩
1. Installer également votre package `tp1`.
1. Vérifier son installaton en exécutant le fichier `tests/test-tp1-install.py`

## Déjà terminé ?

Vous pouvez dès à présent commencer [le TP n°2 sur les objets et classes python](../TP2-ClassesObjets/README.md).
