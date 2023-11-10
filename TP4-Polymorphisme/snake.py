from Webdisplayer import Webdisplayer
from rectangle import rectangle
from CombinedShape2D import CombinedShape2D
import time
class snake(Webdisplayer):
    def __init__(self,rec1):
        self.rec1 = rec1
        self.rec2 = None
        self.shape = CombinedShape2D([rec1])
        self.shape.draw(Webdisplayer())
    
    def move_down(self):
        self.shape.move(0,-10)
        if self.rec2:
            self.rec2.move(0, -10)
    #def add_smt(self,forme):
        #self.shape.add(forme)        

        

i=0    

            
if __name__ == "__main__":
    rec1 = rectangle(50, -20, (255, 0, 0), 70, 10)
    snake = snake(rec1)  # Créez une instance de la classe Snake

    while True:
        snake.move_down()
        print(rec1.get_xy())
        snake.shape.draw(Webdisplayer())  # Redessinez la forme après le déplacement
        time.sleep(0.1)

        if rec1.get_xy()[1] > 400 and not snake.rec2:
            snake.rec2 = rec1  # Associez rec1 à rec2 dans l'objet snake
            snake.shape.add(rec1)  # Ajoutez la forme rec1 au serpent
            snake.rec2.move(0, 50)  # Déplacez la nouvelle forme

        if rec1.get_xy()[1] > 500:
            snake.shape.remove(rec1) 