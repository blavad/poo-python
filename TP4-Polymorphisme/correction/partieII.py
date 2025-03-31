import sys
from core.shape import Circle, Rectangle, CombinedShape2D
from core.color import GREEN, BLUE, RED, WHITE, BLACK


def run_question_4() -> None:
    c = Circle()
    print(c.area())
    r = Rectangle(10, 10, 30, 10, (100, 100, 200))
    r.move(15, 20)
    print(f"x, y = {r.get_xy()}")


def run_question_6() -> None:
    circle1 = Circle(50, 50, 50, color=(100, 200, 100)) 
    circle2 = Circle(150, 50, 50, color=(100, 200, 100)) 
    rectangle = Rectangle(20, 150, 200, 50, color=(200, 100, 100))
    
    combined = CombinedShape2D(100, 100, shapes=[circle1, circle2, rectangle])
    
    print(combined.area())
    print(combined.get_xy())
    combined.move(200, 80)
    print(combined.get_xy())

if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "q4":
        run_question_4()
    if args[0] == "q6":
        run_question_6()
