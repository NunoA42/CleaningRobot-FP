from graphics import *

class Plant:
    
     def __init__(self, ancora, size, hb):#define uma planta e junta as componentes numa lista
         self.ancora = ancora
         self.size = size
         self.vaso1 = Circle(ancora, size)
         self.vaso1.setFill(color_rgb(112,96,71))
         self.vaso2 = Circle(ancora, (size*1.3)) 
         self.vaso2.setFill(color_rgb(217,197,224))
         self.planta1 = Polygon (Point(ancora.getX() - (size*0.35),ancora.getY() + (size*0.35)), Point(ancora.getX(), ancora.getY() + (size*1.2)), Point(ancora.getX() + (size*0.35), ancora.getY() + (size*0.35)), Point(ancora.getX() + (size*1.2), ancora.getY()), Point(ancora.getX() + (size*0.35), ancora.getY() - (size*0.35)),Point(ancora.getX(), ancora.getY() - (size*1.2)), Point(ancora.getX() - (size*0.35), ancora.getY() - (size*0.35)), Point(ancora.getX() - (size*1.2), ancora.getY()))
         self.planta1.setFill("DarkOliveGreen")
         self.planta2 = Polygon (Point(ancora.getX(),ancora.getY() + (size*0.3)), Point(ancora.getX() + (0.9*size), ancora.getY() + (size*0.8)), Point(ancora.getX() + (size*0.3), ancora.getY()), Point(ancora.getX() + (size*0.9), ancora.getY() - (0.8*size)), Point(ancora.getX(), ancora.getY() - (size*0.3)),Point(ancora.getX() - (0.9*size), ancora.getY() - (0.8*size)), Point(ancora.getX() - (size*0.3), ancora.getY()), Point(ancora.getX() - (size*0.9), ancora.getY() + (0.8*size)))
         self.planta2.setFill("OliveDrab")
         self.linha1 = Line(Point(ancora.getX(), ancora.getY() - (size*1.2)), Point(ancora.getX(), ancora.getY() + (size*1.2)))
         self.linha1.setFill("OliveDrab")
         self.linha2 = Line(Point(ancora.getX() - (size*1.2), ancora.getY()), Point(ancora.getX() + (size*1.2), ancora.getY()))
         self.linha2.setFill("OliveDrab")
         self.linha3 = Line(Point(ancora.getX() + (0.9*size), ancora.getY() + (size*0.8)), Point(ancora.getX() - (0.9*size), ancora.getY() - (size*0.8)))
         self.linha3.setFill("DarkOliveGreen")
         self.linha4 = Line(Point(ancora.getX() - (0.9*size), ancora.getY() + (size*0.8)), Point(ancora.getX() + (0.9*size), ancora.getY() - (size*0.8)))
         self.linha4.setFill("DarkOliveGreen")
         self.xmax = ancora.getX() + (self.size*1.3) + hb
         self.xmin = ancora.getX() - (self.size*1.3) - hb
         self.ymax = ancora.getY() + (self.size*1.3) + hb
         self.ymin = ancora.getY() - (self.size*1.3) - hb
         self.xmed = (self.xmax + self.xmin)/2
         self.ymed = (self.ymax + self.ymin)/2
        
         self.hitbox = Rectangle(Point(self.xmin , self.ymin ), Point(self.xmax , self.ymax))
         self.pla = []
         self.planta = [self.vaso2,self.vaso1,self.planta1,self.planta2,self.linha1,self.linha2,self.linha3,self.linha4]
         self.pla.append(self.planta)
        
     def cont(self,hX,hY):#define se existe contacto entre o waiter e a planta
          if (self.xmin  < hX < self.xmax  and self.ymin  < hY < self.ymax):    
              self.contact = True
              return self.contact   
        
     def draw(self, win):#desenha a planta
         for pla in self.planta:
             pla.draw(win)
         #self.hitbox.draw(win)
         self.ancora = Point(self.retornaAncoraX(), self.retornaAncoraY())
         
     def undraw(self):#apaga a planta
         for pla in self.planta:
             pla.undraw()
             
     def retornaAncoraX(self):
                 return self.ancora.getX() 
             
     def retornaAncoraY(self):
                 return self.ancora.getY()

             
