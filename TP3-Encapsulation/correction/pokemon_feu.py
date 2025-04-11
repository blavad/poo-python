from pokemon import Pokemon


class PokemonPlante(Pokemon):
    pass


class PokemonEau(Pokemon):
    pass


class PokemonFeu(Pokemon):

    def attack(self, adversaire):
        current_atk = self.atk
        if isinstance(adversaire, PokemonPlante):
            current_atk = 2 * self.atk
        elif isinstance(adversaire, PokemonEau):
            current_atk = 0.5 * self.atk

        adversaire.hp = adversaire.hp - current_atk
        if adversaire.hp < 0:
            adversaire.hp = 0


bulbi = PokemonPlante("Bulbizarre", 60, 20)
salameche = PokemonFeu("Salameche", 80, 30)

print("---AVANT----")
print(salameche)
print(bulbi)


salameche.attack(bulbi)

print("\n---APRES----")
print(salameche)
print(bulbi)
