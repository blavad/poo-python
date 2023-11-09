class Pokemon:
    def __init__(self,nom,hp,atk):
        self._nom= nom
        self._hp = hp
        self._atk = atk 
    def get_nom(self):
        return self._nom
    
    def get_hp(self):
        return self._hp
    
    def is_dead(self):
        if self._hp<=0:
            return True
        else:
            return False
    
    def attaquer(self,autre_pokemon):
        autre_pokemon.subirattaque(self._atk)

    def subirattaque(self,degats):
        self._hp -= degats

    def __str__(self):
        return f"Pokemon(nom={self._nom}, hp={self._hp}, atk={self._atk})"
    


class PokemonFeu(Pokemon):
    def attaquer(self, autre_pokemon):
        if isinstance(autre_pokemon, PokemonPlante):
            degats = 2 * self._atk
        elif isinstance(autre_pokemon, PokemonEau):
            degats = 0.5 * self._atk
        else:
            degats = self._atk
        autre_pokemon.subirattaque(degats)

class PokemonEau(Pokemon):
    def attaquer(self, autre_pokemon):
        if isinstance(autre_pokemon, PokemonPlante):
            degats = 2 * self._atk
        elif isinstance(autre_pokemon, PokemonEau):
            degats = 0.5 * self._atk
        else:
            degats = self._atk
        autre_pokemon.subirattaque(degats)

class PokemonPlante(Pokemon):
    def attaquer(self, autre_pokemon):
        if isinstance(autre_pokemon, PokemonPlante):
            degats = 2 * self._atk
        elif isinstance(autre_pokemon, PokemonEau):
            degats = 0.5 * self._atk
        else:
            degats = self._atk
        autre_pokemon.subirattaque(degats)

Salameche = PokemonFeu("Salamèche", 60, 10)

Carapuce = PokemonEau("carapuce", 80, 20)

print(Salameche,Carapuce)
Salameche.attaquer(Carapuce)
print(Salameche,Carapuce)