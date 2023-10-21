# Compte Rendu TP 1

## Informations
- **Nom :** *à remplacer par votre nom*
- **Prénom :** *à remplacer par votre nom*

## Partie I

### I.6. 
Depuis le dossier `poo-python/TP1-Fondamentaux/tp1/`,

`python tp1/main.py` ou `python3 tp1/main.py`

### I.7. 

Le fichier s'exécute et renvoie 

```bash
> ------------------------------
> Module main
> ------------------------------
```

### I.8. et  I.9.

On obtient l'erreur `No module named tp1.__main__`. 

En effet, le dossier TP1 est un dossier et ne peut pas être exécuté directement en tant que module. 

-> A moins qu'un fichier `__main__.py` existe dans le dossier (c'est un standard python au même titre que les fichiers `__init__.py`)

### I.11. 

`python3 -m tp1.math.addition`

### I.12. 

On remarque que les instructions du fichier `addition.py` s'exécutent en plus de celui du fichier `__main__.py`. Ce comportement est indésirable. 

Pour pallier à cela, nous modifions le fichier `addition.py` pour que le code ne s'exécute que lorsque c'est le fichier principal.

Fichier *addition.py*
```python
def addition(a, b):
    return a + b

if __name__ == "__main__":
    print("Hey, 3 + 2 = ", addition(3, 2))
```

## Partie II

### II.3. 

Sous UNIX, il contient : 

- un fichier de configuration virtualenv nommé `pyvenv.cfg` 
- l'interpréteur python et le module pip dans un dossier `bin`
- les fichiers d'activation de l'environnement virtuel dans le dossier `bin`
- les paquets python installés dans le dossier `lib/python3.10/site-packages/`

### II.10. 

`pip install -r requirements.txt`

ou

`python -m pip install -r requirements.txt`

## Partie III

### III.4. 

### III.5.  

### III.6. 

### III.7. 
