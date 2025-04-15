class Compte:
    def __init__(self, montant_initial, taux_initial):
        self.montant = montant_initial
        self.taux = taux_initial

    def affiche(self):
        print(f"Compte | montant : {self.montant}€ | taux : {self.taux}%")

    def depot(self, x):
        self.montant = self.montant + x

    def retrait(self, x):
        if self.montant - x < 0:
            print("Transaction impossible, vous n'avez plus assez d'argent.")
        else:
            self.montant = self.montant - x

    def interets(self):
        interets = self.montant * (self.taux / 100)
        self.montant = self.montant + interets


livret_A = Compte(500, 3)
livret_A.affiche()
livret_A.interets()
livret_A.affiche()


livret_jeune = Compte(1200, 10)
livret_jeune.affiche()
livret_jeune.interets()
livret_jeune.affiche()
