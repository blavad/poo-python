from pokemon import Pokemon


class PokemonPlante(Pokemon):
    def attaquer(self, pokemon_adverse):
        if isinstance(pokemon_adverse, PokemonEau):
            pokemon_adverse._hp = pokemon_adverse._hp - 2 * self._atk
        elif isinstance(pokemon_adverse, PokemonFeu):
            pokemon_adverse._hp = pokemon_adverse._hp - 0.5 * self._atk
        else:
            pokemon_adverse._hp = pokemon_adverse._hp - self._atk

    def __str__(self):
        return f"PokemonPlante(nom={self._nom}, hp={self._hp}, atk={self._atk})"


class PokemonEau(Pokemon):
    def attaquer(self, pokemon_adverse):
        if isinstance(pokemon_adverse, PokemonFeu):
            pokemon_adverse._hp = pokemon_adverse._hp - 2 * self._atk
        elif isinstance(pokemon_adverse, PokemonPlante):
            pokemon_adverse._hp = pokemon_adverse._hp - 0.5 * self._atk
        else:
            pokemon_adverse._hp = pokemon_adverse._hp - self._atk

    def __str__(self):
        return f"PokemonEau(nom={self._nom}, hp={self._hp}, atk={self._atk})"


class PokemonFeu(Pokemon):
    def attaquer(self, pokemon_adverse):
        if isinstance(pokemon_adverse, PokemonPlante):
            pokemon_adverse._hp = pokemon_adverse._hp - 2 * self._atk
        elif isinstance(pokemon_adverse, PokemonEau):
            pokemon_adverse._hp = pokemon_adverse._hp - 0.5 * self._atk
        else:
            pokemon_adverse._hp = pokemon_adverse._hp - self._atk

    def __str__(self):
        return f"PokemonFeu(nom={self._nom}, hp={self._hp}, atk={self._atk})"


if __name__ == "__main__":
    salameche = PokemonFeu("Salameche", 100, 30)
    bulbi = PokemonPlante("Bulbizarre", 80, 20)

    print(bulbi)
    salameche.attaquer(bulbi)
    print(bulbi)
