def exercice2():
    longueur = float(input("Entrez la longueur du rectangle : "))
    largeur = float(input("Entrez la largeur du rectangle : "))

    if longueur == largeur:
        print("Le rectangle est un carré.")
    else:
        print("Le rectangle n'est pas un carré.")


def exercice3():
    mon_entier = int(input("Entrez un entier : "))

    if mon_entier % 2 == 0:
        print(f"{mon_entier} est un nombre pair")
    else:
        print(f"{mon_entier} est un nombre impair")


def exercice4():
    n1 = int(input("Entrez le premier nombre : "))
    n2 = int(input("Entrez le deuxième nombre : "))

    p = n1 * n2

    if p > 0:
        print("Le produit est positif")
    elif p < 0:
        print("Le produit est négatif")
    else:
        print("Le produit est égale à zéro")


# Exercice 5


def calcul_montant_ttc(prix, tva, remise):
    if prix > 500:
        prix = prix - prix * remise

    prix_ttc = prix + tva * prix
    return prix_ttc


def exercice5():
    prix = float(input("Entrez le montant d'achat hors taxes"))
    print(f"Le montant TTC est de {calcul_montant_ttc(1000, 0.15, 0.45)}")


# Exercice 6
def prix_photocopies(nb_photocop):
    prix_total = 0
    if nb_photocop <= 10:
        prix_total = nb_photocop * 0.5
    elif nb_photocop <= 30:
        prix_total = 10 * 0.5 + (nb_photocop - 10) * 0.45
    else:
        prix_total = 10 * 0.5 + 20 * 0.45 + (nb_photocop - 30) * 0.3


nb_photocopies = int(input("Nombre de photocopies : "))
prix_total = prix_photocopies(nb_photocopies)
print("Le prix total est ", prix_total)
