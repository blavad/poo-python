class Pokemon:
    def __init__(self, nom_pokemon, hp_pokemon, atk_pokemon):
        self._nom = nom_pokemon
        self._hp = hp_pokemon
        self._atk = atk_pokemon

    def get_nom(self):
        return self._nom

    def get_hp(self):
        return self._hp

    def set_hp(self, new_hp):
        self._hp = new_hp

    def is_dead(self):
        dead = self._hp == 0
        return dead

    def attaquer(self, pokemon_adverse):
        if pokemon_adverse._hp >= self._atk:
            pokemon_adverse._hp = pokemon_adverse._hp - self._atk
        else:
            pokemon_adverse._hp = 0

    def __str__(self):
        return f"Pokemon(nom={self._nom}, hp={self._hp}, atk={self._atk})"


if __name__ == "__main__":
    bulbi = Pokemon("Bulbizarre", 0, 20)
    salameche = Pokemon("Salameche", 70, 10)

    print(salameche)

    bulbi.attaquer(salameche)
    bulbi.attaquer(salameche)
    bulbi.attaquer(salameche)
    bulbi.attaquer(salameche)
    bulbi.attaquer(salameche)
    bulbi.attaquer(salameche)
    bulbi.attaquer(salameche)
    bulbi.attaquer(salameche)
    bulbi.attaquer(salameche)

    print(salameche)
    print(salameche.is_dead())
