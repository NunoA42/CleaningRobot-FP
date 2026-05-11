from graphics import *

class Mess:
    
     def __init__(self, ancora, size):#desenho gráfico da sujidade que representa um prato partido
         self.ancora = ancora
         self.plate = Circle(ancora, size)
         self.effect = Polygon (Point(ancora.getX(), ancora.getY() - size), Point(ancora.getX() - size/2 , ancora.getY() - size/2), Point(ancora.getX() - size/3, ancora.getY() - size/3), Point(ancora.getX(), ancora.getY()), Point(ancora.getX() - size/2, ancora.getY() + size/4), Point(ancora.getX(), ancora.getY() + size/2), Point(ancora.getX() - size/4, ancora.getY() + size*0.8), Point(ancora.getX() + size, ancora.getY() + size), Point(ancora.getX() + size, ancora.getY() - size))
         self.broken = Polygon (Point(ancora.getX() + size*0.6, ancora.getY() + size*0.3), Point(ancora.getX() + size*0.25, ancora.getY() + size*0.6), Point(ancora.getX() + size*0.7, ancora.getY() + size*0.7), Point(ancora.getX() + size*0.4, ancora.getY() + size*0.1))
         self.broken2 = Polygon (Point(ancora.getX() + size*0.4, ancora.getY() - size*0.45), Point(ancora.getX() + size*0.05, ancora.getY() - size*0.35), Point(ancora.getX() + size*0.35, ancora.getY() - size*0.7), Point(ancora.getX() + size*0.25, ancora.getY() - size*0.25))
         self.food1 = Oval (Point(ancora.getX() + size*0.4, ancora.getY() + size*0.2), Point(ancora.getX() + size*0.15, ancora.getY() - size*0.15))
         self.pea1 = Oval(Point(ancora.getX() - (size*0.2), ancora.getY() - (size*0.55)), Point(ancora.getX() - (size*0.35), ancora.getY() - (size*0.7)))
         self.pea2 = Oval(Point(ancora.getX() - (size*0.1), ancora.getY() - (size*0.35)), Point(ancora.getX() - (size*0.25), ancora.getY() - (size*0.5)))
         self.pea3 = Oval(Point(ancora.getX()  - (size*0.05), ancora.getY() - (size*0.45)), Point(ancora.getX() + (size*0.1), ancora.getY() - (size*0.6)))
         self.food2 = Polygon(Point(ancora.getX(), ancora.getY() + size*0.2), Point(ancora.getX() - size*0.05, ancora.getY() + size*0.4), Point (ancora.getX()  + size*0.3, ancora.getY() + size*0.6))
         self.plate.setFill("white")
         self.effect.setFill(color_rgb(223, 209, 196))
         self.effect.setOutline(color_rgb(223, 209, 196))
         self.broken.setFill("white")
         self.broken2.setFill("white")
         self.food1.setFill("red")
         self.pea1.setFill("green")
         self.pea2.setFill("green")
         self.pea3.setFill("green")
         self.food2.setFill("yellow")
        
        
     def draw(self, win):#desenha a sujidade e todas as suas componentes
         self.plate.draw(win)
         self.ancora = Point(self.getX(), self.getY())
         self.effect.draw(win)
         self.broken.draw(win)
         self.broken2.draw(win)
         self.food1.draw(win)
         self.food2.draw(win)
         self.pea1.draw(win)
         self.pea2.draw(win)
         self.pea3.draw(win)
         
     def undraw(self):#apaga a sujidade e todas as suas componentes
         self.plate.undraw()
         self.broken.undraw
         self.effect.undraw()
         self.broken.undraw()
         self.broken2.undraw()
         self.food1.undraw()
         self.food2.undraw()
         self.pea1.undraw()
         self.pea2.undraw()
         self.pea3.undraw()
         
     def getX(self):#devolve a coordenada X da sujidade
         return self.ancora.getX() 
             
     def getY(self):#devolve a coordenada Y da sujidade
         return self.ancora.getY()
             
     def getCenter(self):#devolve aa coordenadas do centro da sujidade
         return self.ancora
    
     def centro(self, x, y):#define o a sujidae no ponto introduzido
         self.ancora = Point(x,y)
             
     def move(self,dx, dy):#move a sujidade
         self.plate.move(dx,dy) 
         self.effect.move(dx,dy)
         self.broken.move(dx,dy)
         self.broken2.move(dx,dy)   
         self.food1.move(dx,dy)
         self.pea2.move(dx,dy)
         self.pea1.move(dx,dy)
         self.pea3.move(dx,dy)
         self.food2.move(dx,dy)
             


            
