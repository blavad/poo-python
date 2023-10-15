# Compte Rendu TP 1

## Informations
- **Nom :** SEVERINO
- **Prénom :** Hugo

## Partie I

### I.6. 
Se trouvant dans "TP1-Fondamentaux" on éxécute la commande suivante : 

```python
python tp1/tp1/main.py
```
### I.7. 
Afin d'éxécuter le module tp1.main, on doit se positionner dans le bon répertoire. On éxécute donc la commande suivante :

```
cd tp1
```

On éxécute ensuite le module : 
```
python -m tp1.main
```

Et on obtient bien l'éxécution de main.py : 

```
> ------------------------------
> Module main
> ------------------------------
```
### I.8. 
En éxécutant ```python -m tp1``` on obtient le message d'erreur suivant : 

<code style="color : red">C:\Users\Hugo\anaconda3\python.exe: No module named tp1.__main__; 'tp1' is a package and cannot be directly executed</code>

### I.9. 
En renommant le fichier en ```__main__.py```, la commande ```python -m tp1``` fonctionne et éxécute bien notre code.
### I.11. 
Afin d'éxécuter notre fonction, on utilise la commande suivante : ```python tp1/math/addition.py```
### I.12. 

Quand on importe la fonction `addition` dans le fichier `__main__.py` et change la ligne `print("> Module 'main'")` par `print(addition(8,8))`, on obtient le résultat suivant : 

```python 
Hey, 3 + 2 =  5
> ------------------------------
16
> ------------------------------
```

On a donc bien pu évaluer notre addition, mais on a éxécuté toute notre fonction addition, et on affiche donc le "print". 

Afin de n'importer que notre fonction addition sans éxécuter tout le code, on pourra ajouter le code suivant dans notre fichier addition.py : 
```python 
if __name__== '__main__':
  print("Hey, 3 + 2 = ", addition(3, 2))
```

Ainsi, le contenu du print ne sera éxécuter seulement lorsque notre fonction est éxécuté directement et non importé.
## Partie II

### II.3. 
Le dossier `.env` contient un fichier de configuration `pyenv.cfg` avec le chemin d'execution de python sur la machine et sa version. On retrouve également les librairies de notre environnement virtuel (Actuelement seuelement pip, pkg_resources et setuptools).
### II.10. 
Afin d'importer les requirements dans notre environnement virtuel tp1-env, une fois activé on éxécute la fonction suivante : `pip install -r requirements.txt`. Pour installer notre environnement local `tp1`, on éxécute la commande suivante : `pip install -e tp1`
## Partie III

### III.4. 

### III.5.  

### III.6. 

### III.7. 
