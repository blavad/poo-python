from Webdisplayer import Webdisplayer
from rectangle import rectangle
from CombinedShape2D import CombinedShape2D
import time
class snake(Webdisplayer):
    def __init__(self,rec1):
        self.rec1 = rec1
        self.shape = CombinedShape2D([rec1])
        self.shape.draw(Webdisplayer())
    
    def move_down(self):
        self.shape.move(0,-10)
    #def add_smt(self,forme):
        #self.shape.add(forme)        

        

i=0    
if __name__ == "__main__":
    rec1 = rectangle(50, -20, (255, 0, 0), 70, 10)
    snake = snake(rec1)  # Créez une instance de la classe Snake
    rec2 = []
    while True:
        snake.move_down()
        if rec1:

            rec1.move(0, 10)
            print(rec1.get_xy())
        if rec2:
            rec2.move(0, 10) 
            print(rec2.get_xy())
        #print(rec1.get_xy())
        snake.shape.draw(Webdisplayer())  # Redessinez la forme après le déplacement
        time.sleep(0.1)

        if rec1.get_xy()[1] > 400 and not rec2:
            rec2 = rec1 
            snake.shape.add(rec2) # Créez une nouvelle forme
            rec2.move(0, 50)  # Déplacez la nouvelle forme
            
             
        
        if rec1.get_xy()[1] > 500:
            snake.shape.remove(rec1)
            






        

        

