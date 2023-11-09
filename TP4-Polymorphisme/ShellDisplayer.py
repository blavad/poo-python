from Displayer import Displayer

Color = tuple[int,int,int]

class ShellDisplayer(Displayer):
    
    def draw_point(self, x: int, y: int, color: Color) -> None:
        print(f"point(x={x}, y={y}, color={color}")

    def draw_line(self, x1: int, y1: int, x2: int, y2: int, color: Color) -> None:
        print(f"line(x1={x1}, y1={y1}, x2={x2}, y2={y2}, color={color}")

    def draw_circle(self, x: int, y: int, radius: int, color: Color) -> None:
        print(f"circle(x={x}, y={y}, radius={radius}, color={color}")

    def draw_rectangle(self, x: int, y: int, width: int, length: int, color: Color) -> None:
        print(f"rectangle(x={x}, y={y}, width={width}, length={length}, color={color}")

    def draw_square(self, x: int, y: int, side: int, color: Color) -> None:
         print(f"square(x={x}, y={y}, side={side}, color={color}")


#ShellDisplayer().draw_line(0,0,0,0,{0,0,0})