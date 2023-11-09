import sys
from circle import circle
from rectangle import rectangle
from CombinedShape2D import CombinedShape2D


def run_question_4() -> None:
    a= circle()
    print(a.area())

    b=rectangle(30,10,{255, 255, 255},10,10)

    b.move(5,10)

    print(b.get_xy())

    pass


def run_question_6() -> None:
    a = circle()
    b = circle(5,5,{0,0,0}, 30)
    c = rectangle(30,10,{255, 255, 255},10,10)
    d=CombinedShape2D([a,b,c])
    print(d.area())
    print(d.get_xy())
    d.move(1,1)
    print(d.get_xy())
    pass


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "q4":
        run_question_4()
    if args[0] == "q6":
        run_question_6()
