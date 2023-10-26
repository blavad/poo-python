class Pokemon:
    _nom: str
    _hp: float
    _atk: float

    def __init__(self, nom: str, hp: float, atk: float) -> None:
        self._nom = nom
        self._hp = hp
        self._atk = atk

    def get_nom(self) -> str:
        return self._nom

    def get_hp(self) -> str:
        return self._hp

    def get_atk(self) -> str:
        return self._atk

    def attaquer(self, pokemon) -> None:
        pokemon._recevoir_degats(self.get_atk())

    def is_dead(self) -> bool:
        return self.get_hp() == 0

    def _recevoir_degats(self, degats: float) -> None:
        self._hp -= degats
        if self._hp < 0:
            self._hp = 0

    def __str__(self) -> str:
        return f"Pokemon(nom={self._nom}, hp={self._hp}, atk={self._atk})"


class PokemonFeu(Pokemon):
    def __init__(self, nom: str, hp: float, atk: float) -> None:
        super().__init__(nom, hp, atk)

    def attaquer(self, pokemon: Pokemon) -> None:
        if isinstance(pokemon, PokemonPlante):
            pokemon._recevoir_degats(2 * self.get_atk())
        elif isinstance(pokemon, PokemonEau) or isinstance(pokemon, PokemonFeu):
            pokemon._recevoir_degats(0.5 * self.get_atk())
        else:
            super().attaquer(pokemon)


class PokemonEau(Pokemon):
    def __init__(self, nom: str, hp: float, atk: float) -> None:
        super().__init__(nom, hp, atk)

    def attaquer(self, pokemon: Pokemon) -> None:
        if isinstance(pokemon, PokemonFeu):
            pokemon._recevoir_degats(2 * self.get_atk())
        elif isinstance(pokemon, PokemonEau) or isinstance(pokemon, PokemonPlante):
            pokemon._recevoir_degats(0.5 * self.get_atk())
        else:
            super().attaquer(pokemon)


class PokemonPlante(Pokemon):
    def __init__(self, nom: str, hp: float, atk: float) -> None:
        super().__init__(nom, hp, atk)

    def attaquer(self, pokemon: Pokemon) -> None:
        if isinstance(pokemon, PokemonEau):
            pokemon._recevoir_degats(2 * self.get_atk())
        elif isinstance(pokemon, PokemonPlante) or isinstance(pokemon, PokemonFeu):
            pokemon._recevoir_degats(0.5 * self.get_atk())
        else:
            super().attaquer(pokemon)
