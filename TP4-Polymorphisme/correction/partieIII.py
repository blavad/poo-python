import sys

from core.shape import Circle, CombinedShape2D, Smiley
from core.displayer import ShellDisplayer, WebDisplayer


def run_question_5() -> None:
    # Décommenter ci-dessous et modifier le code de façon adéquate
    # On n'oubliera pas d'importer les classes Circle et CombinedShape2D
    displayer = ShellDisplayer()
    c1 = Circle()
    c1.move(100, 60)
    c2 = Circle()
    c1.move(20, 20)
    c3 = Circle()
    three_circles = CombinedShape2D(0, 0, [c1, c2, c3])
    three_circles.draw(displayer)


def run_question_6() -> None:
    # Décommenter ci-dessous après importation de la classe Smiley
    displayer = ShellDisplayer()
    smiley = Smiley(100, 50, 45, (20, 20, 20))
    smiley.draw(displayer)


def run_question_9() -> None:
    ask_num = "Quel est le numéro de l'écran ? "
    ask_inputs = "Quels paramètres ? (ex : '100,100,20') : "

    display_num = input(ask_num)
    while not display_num.isnumeric():
        display_num = input(ask_num)

    displayer = WebDisplayer(display_num, url="http://draw.david-albert.fr")

    params = input(ask_inputs)
    while params != "q" and params != "quit":
        try:
            x, y, size = params.split(",")
            smiley = Smiley(int(x), int(y), int(size))
            smiley.draw(displayer)
        except Exception as error:
            print(f"Error. {error}")
        params = input(ask_inputs)


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "q5":
        run_question_5()
    if args[0] == "q6":
        run_question_6()
    if args[0] == "q9":
        run_question_9()
