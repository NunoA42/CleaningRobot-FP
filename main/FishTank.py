from graphics import *

class FishTank:

    def __init__(self, ancora, size, hb):#define um aquario e junta as componentes numa lista
        self.ancora = ancora
        self.size = size
        self.mesa = Rectangle (Point(ancora.getX() - (size) ,ancora.getY() - (size* 1.4)), Point(ancora.getX() + (size), ancora.getY() + (size*1.4)))
        self.tanque = Rectangle (Point(ancora.getX() - (size*0.8) ,ancora.getY() - (size*1.2)), Point(ancora.getX() + (size*0.8), ancora.getY() + (size*1.2)))
        self.lagosta = Polygon (Point(ancora.getX() - ((size*0.07)), ancora.getY() - (size*1.1)), Point(ancora.getX() + ((size*0.07)), ancora.getY() - (size*1.1)), Point(ancora.getX() + ((size*0.2)), ancora.getY() - (size*0.7)), Point(ancora.getX() + ((size*0.07)), ancora.getY() - (size*0.3)), Point(ancora.getX() - ((size*0.07)), ancora.getY() - (size*0.3)), Point(ancora.getX() - ((size*0.2)), ancora.getY() - (size*0.7)))
        self.braço1 = Polygon (Point(ancora.getX() - (size*0.1), ancora.getY() - (size*0.5)), Point(ancora.getX() - (size*0.15), ancora.getY() - (size*0.6)), Point(ancora.getX() - (size*0.4), ancora.getY() - (size*0.4)), Point(ancora.getX() - (size*0.15), ancora.getY()), Point(ancora.getX() - (size*0.02), ancora.getY() - (size*0.1)), Point(ancora.getX() - (size*0.15), ancora.getY() - (size*0.2)), Point(ancora.getX() - (size*0.25), ancora.getY() - (size*0.4)))
        self.braço2 = Polygon (Point(ancora.getX() + (size*0.1), ancora.getY() - (size*0.5)), Point(ancora.getX() + (size*0.15), ancora.getY() - (size*0.6)), Point(ancora.getX() + (size*0.4), ancora.getY() - (size*0.4)), Point(ancora.getX() + (size*0.15), ancora.getY()), Point(ancora.getX() + (size*0.02), ancora.getY() - (size*0.1)), Point(ancora.getX() + (size*0.15), ancora.getY() - (size*0.2)), Point(ancora.getX() + (size*0.25), ancora.getY() - (size*0.4)))
        self.antena1 = Line(Point(ancora.getX(), ancora.getY() - (size*0.3)), Point(ancora.getX() + (size*0.07), ancora.getY() - (size*0.16)))
        self.antena2 = Line(Point(ancora.getX(), ancora.getY() - (size*0.3)), Point(ancora.getX() - (size*0.07), ancora.getY() - (size*0.16)))
        self.peixe = Oval(Point(ancora.getX() + (size*0.4), ancora.getY() + (size*0.8)), Point(ancora.getX() + (size*0.1), ancora.getY() + (size)))
        self.cauda = Polygon(Point(ancora.getX() + (size*0.1), ancora.getY() + (size*0.9)), Point(ancora.getX() - (size*0.07), ancora.getY() + (size)), Point(ancora.getX(), ancora.getY() + (size*0.9)), Point(ancora.getX() - (size*0.07), ancora.getY() + (size*0.8)))
        self.bolha1 = Oval(Point(ancora.getX() - (size*0.4), ancora.getY() + (size*0.6)), Point(ancora.getX() - (size*0.5), ancora.getY() + (size*0.7)))
        self.bolha2 = Oval(Point(ancora.getX() - (size*0.5), ancora.getY() + (size*0.4)), Point(ancora.getX() - (size*0.6), ancora.getY() + (size*0.5)))
        self.bolha3 = Oval(Point(ancora.getX() - (size*0.35), ancora.getY() + (size*0.45)), Point(ancora.getX() - (size*0.3), ancora.getY() + (size*0.5)))
        self.mesa.setFill("white")
        self.tanque.setFill(color_rgb(202,225,255))
        self.lagosta.setFill("brown2")
        self.braço1.setFill("brown2")
        self.braço2.setFill("brown2")
        self.peixe.setFill("darkorange")
        self.cauda.setFill("darkorange")
        self.bolha1.setFill("lavender")
        self.bolha2.setFill("lavender")
        self.bolha3.setFill("lavender")
        
        self.xmax = ancora.getX() + self.size + hb
        self.xmin = ancora.getX() - self.size - hb
        self.ymax = ancora.getY() + (self.size*1.4) + hb
        self.ymin = ancora.getY() - (self.size*1.4) - hb
        self.xmed = (self.xmax + self.xmin)/2
        self.ymed = (self.ymax + self.ymin)/2

        self.hitbox = Rectangle(Point(self.xmin , self.ymin ), Point(self.xmax , self.ymax))
        
        self.aq = []
        self.aquario = [self.mesa,self.tanque,self.braço1,self.braço2,self.lagosta,self.antena1,self.antena2,self.peixe,self.cauda,self.bolha1,self.bolha2,self.bolha3]
        self.aq.append(self.aquario)
        
    def cont(self,hX,hY):#define se existe contacto entre o waiter e o aquario
        if (self.xmin  < hX < self.xmax  and self.ymin  < hY < self.ymax):    
            self.contact = True
            return self.contact
        
    def draw(self, win):#desenha o aquario
        for aq in self.aquario:
            aq.draw(win)
        #self.hitbox.draw(win)
        self.ancora = Point(self.retornaAncoraX(), self.retornaAncoraY())

    def undraw(self):#apaga o aquario
        for aqua in self.aquario:
            aqua.undraw()
        
    def retornaAncoraX(self):
        return self.ancora.getX() 
                    
    def retornaAncoraY(self):
        return self.ancora.getY()

         
