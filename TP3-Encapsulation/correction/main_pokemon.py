from pokemon import *


def main():
    bulbizarre = PokemonPlante("Bulbizarre", 50, 15)
    salameche = PokemonFeu("Salamèche", 50, 20)
    carapuce = PokemonEau("Carapuce", 60, 10)

    print(bulbizarre)
    print(salameche)
    print(carapuce)

    bulbizarre.attaquer(salameche)
    bulbizarre.attaquer(carapuce)
    carapuce.attaquer(bulbizarre)

    print(bulbizarre)
    print(salameche)
    print(carapuce)


if __name__ == "__main__":
    main()
