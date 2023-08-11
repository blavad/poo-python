# Python - les basiques

Dans ce TP, on s'intéresse aux fondements du langage python et de la programmation orientée objet dans ce langage. Les compétences travaillées durant cette activité sont les suivantes : 

- Comprendre et utiliser l'interpréteur Python
- Créer un package et des modules python
- Utiliser un environnement virtuel python
- Comprendre et utiliser le gestionnaire de paquets `pip`
- Savoir différencier les paradigmes de programmation
- Comprendre les avantages de la POO
- Comprendre la notion d'objet en python

## Partie 0 : Mise en place
- Clonez ce repo : `git clone <repo>`
- Ouvrez un terminal à l'emplacement `poo-python/TP1-Fondamentaux`

Ce dossier est le votre pendant tout le TP. Toutes les manipulations doivent être faites à l'intérieur. Il contient déjà certains fichiers qui seront à lire et/ou compléter durant le TP.  

## Partie 1 : Interpréteur et package (30 min)

**Pour commencer**

1. Vérifiez que python est bien installé (version >= 3.5)
1. Quelle est sa version par défaut ?
   - S'il s'agit de la version 2, vérifiez que `python3` est également installée
   - Nous n'utiliserons **désormais plus que la version 3**
     
**Interpréteur et premiers modules**
3. Le dossier `tp1` est notre **package**
1. Dans le dossier `tp1` créez un autre dossier nommé `tp1` et naviguez dedans (ce dossier le code source de notre package)
1. Dans le dossier `tp1/tp1` créez le fichier `main.py` avec le contenu:
      ```python
       print("> ------------------------------")
       print("> Module main")
       print("> ------------------------------")
      ```
1. Exécutez ce fichier grâce àen utilisant l'interpréteur.
1. Exécutez le module `tp1.main`. Que ce passe-t-il ? 🚩
   > on utilisera pour cela la commande `python -m tp1.main`.
1. Exécutez la commande `python -m tp1`. Que ce passe-t-il ? 🚩
1. Renommez le fichier `main.py` en `__main__.py` et réessayez. Conclure. 🚩
1. Dans le dossier `tp1/tp1/math` créez le module `addition.py` avec le contenu:
      ```python
      def addition(a, b):
         return a + b
      
      print("Hey, 3 + 2 = ", addition(3, 2))
      ```
   
1. Exécutez ce module.

**Plus de modules**

On souhaite désormais utiliser la fonction `addition` dans notre programme `__main__.py`.

14. Importez la fonction `addition` dans le fichier `__main__.py` et changez la ligne `print("> Module 'main'")` par `print(addition(8,8))`. Qu'observe-t-on ? 🚩

1. Corrigez ce problème. 🚩
   > 💡 on pourra utiliser la variable build-in `__name__`

1. Dans le dossier `tp1/tp1/math` créez le fichier `__init__.py` avec le contenu:
   ```python
   from .addition import addition
   ```
   Changez en conséquence l'importation de la fonction `addition` dans `__main__.py` 
   ```python
   from tp1.math import addition
   ```
1. Ajoutez une fonction `np_addition` au module `tp1.math`

   Cette fonction prend deux listes en entrée, les transforme en array numpy et calcule leur somme. 

1. (Optionnel) Ajoutez une fonction `np_addition` au module `tp1.math`.

   Cette fonction calcule l'aire d'un cercle en fonction de son rayon.
      - $aire = \pi r^2$
      - On utilisera la constante [`pi`](https://docs.python.org/3/library/math.html#math.pi) du paquet [`math`](https://docs.python.org/3/library/math.html#math.pi)
1. *(Optionnel)* Dans `tp1`, créez le module `tp1.argv` qui affiche le nombre et la liste des arguments passés en paramètre.

## Partie 2 : La gestion de paquets (30min)

**Environnement virtuel**
1. Revenez dans le dossier `TP1-Fondamentaux`
1. Créez un environnement virtuel python avec le nom `.env`.
1. Analysez le contenu du dossier `.env`. Que contient-il ?
1. Activez cet environnement virtuel.
1. Affichez la liste des paquets installés dans l'environnement virtuel.
1. Comparez à la liste des paquets python installés sur votre machine. 
1. Installez les paquets nécessaires au bon fonctionnement du module `tp1` (numpy).
   > On pourra valider que la commande `python -m tp1.tp1` s'exécute bien.
1. Créez le fichier `requirements.txt` qui contient les dépendances de notre package.
**Installer et utiliser notre module**
8. Sortez de l'environnement virtuel `.env`, créez-en un second nommé `.tp1-env`.
1. Dans ce second environnement virtuel, installez tous les requirements du fichier `requirements.txt` en une ligne.
1. Installez également votre package `tp1`.
1. Vérifiez son installaton en exécutant le fichier `tests/test-tp1-install.py`

## Partie 3 : Comprendre la notion d'objet en python (30min)

1. Vérifiez que vous êtes bien dans l'environnement virtuel
2. Lancez l'interpréteur python en mode interactif

## Partie 3 : Création de modules 




