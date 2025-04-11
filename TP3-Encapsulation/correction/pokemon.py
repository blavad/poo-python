class Pokemon:
    def __init__(self, nom_pokemon, hp_pokemon, atk_pokemon):
        self.nom = nom_pokemon
        self.hp = hp_pokemon
        self.atk = atk_pokemon

    def get_nom(self):
        return self.nom

    def is_dead(self):
        return self.hp == 0

    def attack(self, adversaire):
        if not adversaire.is_dead():
            adversaire.hp = adversaire.hp - self.atk
            if adversaire.hp < 0:
                adversaire.hp = 0

    def __str__(self):
        return f"Pokemon(nom={self.nom}, hp={self.hp}, atk={self.atk}))."


bulbi = Pokemon("Bulbizarre", 60, 20)
salameche = Pokemon("Salameche", 80, 10)
grolem = Pokemon("Grolem", 100, 10)

print(grolem.nom)

bulbi.attack(grolem)
bulbi.attack(grolem)
bulbi.attack(grolem)

print(grolem)

print(salameche.__str__())
print(bulbi)
