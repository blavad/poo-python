import sys


def run_question_5() -> None:
    # Décommenter ci-dessous et modifier le code de façon adéquate
    # On n'oubliera pas d'importer les classes Circle et CombinedShape2D

    # c1 = Circle()
    # c1.move(100, 60)
    # c2 = Circle()
    # c1.move(20, 20)
    # c3 = Circle()
    # three_circles = CombinedShape2D(0, 0, [c1, c2, c3])
    pass


def run_question_6() -> None:
    # Décommenter ci-dessous après importation de la classe Smiley

    # smiley = Smiley(100, 50, 45, (20, 20, 20))
    # smiley.draw()
    pass


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "q5":
        run_question_5()
    if args[0] == "q6":
        run_question_6()
