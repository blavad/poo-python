import sys
import sys
from circle import circle
from rectangle import rectangle
from CombinedShape2D import CombinedShape2D
from ShellDisplayer import ShellDisplayer
from smiley import Smiley
from Webdisplayer import Webdisplayer

def run_question_5() -> None:
    # Décommenter ci-dessous et modifier le code de façon adéquate
    # On n'oubliera pas d'importer les classes Circle et CombinedShape2D
    
    c1 = circle()
    c1.draw(ShellDisplayer)
    c1.move(100, 60)
    c2 = circle()
    c1.move(20, 20)
    c3 = circle()

    three_circles = CombinedShape2D([c1, c2, c3])
    three_circles.draw(ShellDisplayer)
    pass


def run_question_6() -> None:
    # Décommenter ci-dessous après importation de la classe Smiley
    
    smiley = Smiley(10, -100, 100, (20, 20, 20))
    shell_displayer = ShellDisplayer()  
    smiley.draw(shell_displayer)
    shell_displayer = Webdisplayer()
    smiley.draw(shell_displayer)
    pass


def run_question_9() -> None:
    # Demande à l'utilisateur d'indiquer le numéro de l'écran d'affichage
    # puis, en continue, lui demande trois 3 valeurs (x, y et size) et
    # affiche le smiley correspondant. Dès que l'utilisateur entre la
    # chaîne 'q', le programme s'arrête
    pass


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "q5":
        run_question_5()
    if args[0] == "q6":
        run_question_6()
    if args[0] == "q9":
        run_question_9()
