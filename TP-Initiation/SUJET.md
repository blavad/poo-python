# Python - les basiques

Dans ce TP, on s'intéresse aux fondements du langage python et de la programmation orientée objet dans ce langage. Les compétences travaillées durant cette activité sont les suivantes : 

- Comprendre et utiliser l'interpréteur Python
- Utiliser un environnement virtuel python
- Comprendre et utiliser le gestionnaire de paquets `pip`
- Savoir différencier les paradigmes de programmation
- Comprendre les avantages de la POO
- Comprendre la notion d'objet en python

## Partie 1 : Interpréteur (30 min)
1. Vérifiez que python est bien installé
2. De quelle version s'agit-il ?
   - S'il s'agit de la version 2, vérifiez que `python3` est également installé
   - Nous n'utiliserons **désormais plus que la version 3**
     
3. Interpréteur (mode **interactif**)

   - Assignez à la variable `lesson` la valeur `"poo"`
   - Afficher le contenu de la variable `lesson`
   - Créez un array numpy initilisé avec 10 valeurs de 0
   - Quittez l'interpréteur `Ctrl + D`

5. Interpréteur et création de modules

   - Créez le dossier `tp1` (ce dossier est **notre package**)
   - Dans le dossier `tp1` créez le fichier `main.py` avec le contenu:
   ```python
   # fichier main.py
   print("> Module 'main'")
   ```
   - Exécutez ce fichier grâce à l'interpréteur
   - Exécutez le module `tp1.main`, on utilisera pour cela la commande `python -m tp1.main`. Que ce passe-t-il ? 🚩
   - Exécutez la commande `python -m tp1`. Que ce passe-t-il ? 🚩
   - Renommez le fichier `main.py` en `__main__.py` et réessayez. 🚩
   - Dans le dossier `tp1/math` créez le module `addition.py` avec le contenu:
   ```python
   # fichier addition.py
   def addition(a, b):
      return a + b
   
   print("Hey, 3 + 2 = ", addition(3, 2))
   ``` 
   - Exécutez ce fichier
  


## Partie 4 : Création de modules en python


## Partie 2 : La gestion de paquets (30min)

1. Créez un environnement virtuel python avec le nom `.env` et l'activer.
2. Affichez les paquets installés

   Analysez le contenu du dossier créé automatiquement. Que contient-il ?

2. Activez cet environnement.


## Partie 3 : Comprendre la notion d'objet en python (30min)

1. Vérifiez que vous êtes bien dans l'environnement virtuel
2. Lancez l'interpréteur python en mode interactif

## Partie 3 : Création de modules 




