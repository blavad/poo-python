class Pokemon:
    def __init__(self, nom_pokemon, hp_pokemon, atk_pokemon):
        self.nom = nom_pokemon
        self.hp = hp_pokemon
        self.atk = atk_pokemon

    def get_nom(self):
        return self.nom

    def is_dead(self):
        return self.hp == 0


bulbi = Pokemon("Bulbizarre", 60, 20)
salameche = Pokemon("Salameche", 80, 10)

print(salameche.get_nom())
print(bulbi.get_nom())
