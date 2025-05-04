# TP Remise à niveau en Python

Dans ce TP, on s'intéresse à l'écriture de programmes simples en Python. Les compétences travaillées durant cette activité sont les suivantes :

- Ecrire et exécuter un programme python
- Ecrire des conditions en python
- Ecrire des boucles en python
- Manipuler des chaînes de caractères en python

## Partie I : Affectations

1. Ecrire en une ligne Python l'affectation de la valeur $3x²+5x-7$ à une variable `y`.

2. Ecrire en une ligne Python l'affectation de la valeur $\frac{2x-6}{4}$ à une variable `z`.

3. Affecter à la variable `resultat` la formule correspondant à l'application de l'algorithme suivant à un nombre `x`.

   - Prendre un nombre et le multiplier par 2.
   - Soustraire 6 à ce produit et lui additionner le nombre de départ.
   - Diviser cette somme par 3 et donner le résultat ainsi obtenu.

4. Eloïse a choisi un nombre secret `n` puis elle a appliqué l'algorithme suivant :

   - J'ai soustrait 5 à mon nombre
   - J'ai ensuite multiplié le total par 4
   - Et pour finir, j'ai soustrait mon nombre au résultat

   Elle a noté x le résultat obtenu.

   Ecrire la formule permettant de retrouver le nombre secret `n` à partir de `x`.

## Partie II : Premières fonctions

1. Complétez la fonction suivante, sachant qu'elle traduit l'expression mathématique $f(x)=7x-3$.

   ```python
   def f(x):
       y =          # ligne à compléter
       return y
   ```

2. Ecrire un fonction python qui traduit l'expression mathématique $f(x,y)=3x^2 - 2y +5$

3. Ecrire une fonction python qui calcule et renvoie l'aire d'un trapèze. Elle a pour paramètres : `B`, `b`, `h` qui représentent respectivement la grande base, la petite base et la hauteur.

4. Un parc d'attractions affiche les tarifs suivants :

   - 8,50 € par enfant
   - 12,00 € par adulte

   Ecrire une fonction `prix(n, p)` qui renvoie le prix total à payer, à partir du nombre `n` d'enfants et du nombre `p` d'adultes.

## Partie III : Conditions

1. Complétez le programme pour qu'il affecte à la variable `maximum` le plus grand de deux nombres `a` et `b`, prélablement rentrés par l'utilisateur.

   ```python
   a = int(input("Entrez le nombre a : "))
   b = int(input("Entrez le nombre b : "))

   if ...:
       ....
   else:
       ...

   print("Le maximum est", maximum)
   ```

1. Ecrire un programme qui demande à l'utilisateur d'entrer deux valeurs décimales, les affecte aux variables `longueur` et `largeur` puis écrit `"Le rectangle est un carré."` ou `"Le rectangle n'est pas un carré."` selon le cas.

1. Ecrire un programme qui demande à l'utilisateur d'entrer un nombre entier et affiche `"12 est un nombre pair."` ou `"21 est un nombre impair."` selon le cas (12 et 21 sont pris pour exemples).

1. Écrire un programme qui demande à l’utilisateur deux nombres n1 et n2 et lui indique ensuite si le produit de ces deux nombres est positif ou négatif. On prévoit dans le programme le cas où le produit peut être nul.

1. Un magasin offre à ses clients 25% de réduction sur les montants d’achat supérieurs à 500 €. Ecrire un programme qui demande à l'utilisateur d’entrer le prix total hors TVA et de calculer le montant TTC en tenant compte de la remise et du fait que la TVA est égale à 10%.

   - Modifier et améliorer votre programme en créant une fonction `calcul_montant_ttc(prix, tva, remise)` qui fait ce calcul

1. Le service de photocopie de votre université facture 0,50 € pour les 10 premières photocopies, 0,45 € pour les 20 suivantes et 0,30 € au-delà de 30 photocopies. Ecrivez un programme qui demande à l'utilisateur le nombre de photocopies réalisées et affiche la facture correspondante.

1. Créer un programme qui demande à l'utilisateur un mot de passe et vérifie qu'il est sécurisé. Un mot de passe est considéré sécurisé s'il contient:
   - au moins 8 caractères
   - au moins une majuscule
   - au moins un chiffre
   - au moins un caractère spécial (`#$+*&=%`)

## Partie IV : Boucles

1. Ecrire un programme qui utilise une boucle for pour afficher les nombres de 1 à 10.

2. Écrire un algorithme qui affiche 10 fois `Hello` en utilisant une boucle **while**.

3. Ecrire un programme pour calculer

   - 1 + 2 + 3 + .... + n (n est saisi par l'utilisateur)
   - 1 + 4 + 7 + 10 + 13 + .... + 100

4. Ecrire un programme qui s'arrête dès que l'utilisateur saisit le mot `STOP`.

5. Écrire un programme permettant d'entrer un nombre et d'afficher le triangle d'étoiles. En utilisant la boucle POUR imbriqué.

   _Exemple de sortie:_

   ```bash
   Entrez un nombre: 5
       *
      ***
     *****
    *******
   *********
   ```

6. Compléter le programme suivant pour qu'il compte le nombre de fois qu'une lettre apparaît dans une chaîne de caractères (en utilisant une boucle for).

   ```python
   def nbr_apparition(lettre, phrase):
       n = 0
       # à compléter
       return n

   phrase = "Ceci est un exemple"
   lettre = "e"

   n = nbr_apparition(lettre, phrase)
   print(f"Il y a {n} {lettre} dans : {phrase}")
   ```

7. Ecrire un programme qui initialise la liste `l = ["Apparence", "Velouté", "Fraise", "Jinx"]` puis calcul le nombre de lettres totales dans cette liste.

8. Ecrire un programme qui initialise la liste `l2 = [1, 3, 4, 5]` puis itère sur ses éléments pour appliquer le fonction $f(x)=3x^2 + \frac{1}{2}x - 7$ à chaque valeur de la liste puis affiche la liste modifiée

9. Ecrire un programme qui lit des caractères et s’arrête à la lecture d’un point (`"."`). Ce programme compte et affiche le nombre de caractères lus, le nombre de lettres minuscules ainsi que le nombre de chiffres.

   Modifier le programme pour n’autoriser la saisie que de maximum 50 caractères.

## Partie V : Algorithmie

1. Conversion binaire.

   - Ecrire une fonction `entier(bits)` qui renvoie l'entier correspondant à la représentation binaire dans la chaîne de caractères `bits` (sans utiliser la fonction `int()`).

     _Exemple :_ `entier("101011")` renvoie le nombre entier `43`.

   - Ecrire une fonction `bin(entier)` qui renvoie la représentation binaire de l'entier entré en paramètre.

     _Exemple :_ `bin(43)` renvoie le nombre entier `"101011"`.

1. Créer une fonction `separer(chaine)` qui renvoie la chaîne obtenue en séparant les caractères de chaine par des tirets "-".

1. Écrire un algorithme qui place les zéro d'une liste vers la fin de celle-ci, en maintenant l'ordre des éléments.

   _Exemple:_ `[9,0,3,0,1,6,0,0,2,3]` devient `[9,3,1,6,2,3,0,0,0,0]`

1. Arithmétique

   - Définir une fonction `estPremier(n)` qui prend un entier en paramètre et renvoie `true` s'il est premier, sinon renvoie `false`.

     _Rappel :_ 0 et 1 ne sont pas premiers

   - Définir une fonction `pgcd(a, b)` qui prend deux entiers en paramètres et renvoie le PGCD de ces deux nombres grâce à l'algorithme d'Euclide.

   - Définir une fonction `decompoFacteursPremiers(n)` qui prend un entier en paramètre et renvoie un dictionnaire dont les clés sont les facteurs premiers et les valeurs sont les puissances associées à ces facteurs.
