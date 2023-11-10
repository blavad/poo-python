from Displayer import Displayer
import requests
import json
from circle import circle
url = "http://draw.david-albert.fr/draw/773314/1"
Color = tuple[int,int,int]

class Webdisplayer(Displayer):

    def draw_circle(self, x: int, y: int, radius: int, color: Color) -> None:
       
       
       data = {"shape": "circle", "x": x, "y": y, "radius": radius, "color": color}
       x = requests.post(url, json = data)

    

    def draw_line(self, x1: int, y1: int, x2: int, y2: int, color: Color) -> None:
        print(f"line(x1={x1}, y1={y1}, x2={x2}, y2={y2}, color={color})")

    

    def draw_rectangle(self, x: int, y: int, width: int, length: int, color: Color) -> None:
       

        data = {"shape": "rectangle", "x": x, "y": y, "width": width, "height": length, "color": color}

        x = requests.post(url, json = data)

    def draw_square(self, x: int, y: int, side: int, color: Color) -> None:
         print(f"square(x={x}, y={y}, side={side}, color={color})")

    def draw_point(self, x: int, y: int, side: int, color: Color) -> None:
         print(f"square(x={x}, y={y}, side={side}, color={color})")
    
    

Webdisplayer().draw_circle(5,5,30,[0,0,0])