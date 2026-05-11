from graphics import *

class Chair: 
    def __init__(self, ancora, size, hb):#define uma cadeira e junta as componentes numa lista
        self.ancora = ancora
        self.size = size
        self.cadeira = Rectangle (Point(ancora.getX() - (size/4),ancora.getY() - (size*0.35)), Point(ancora.getX() + (size/4), ancora.getY() + (size*0.45)))
        self.braço1 = Rectangle (Point(ancora.getX() - (size*0.4), ancora.getY() - (size*0.35)), Point(ancora.getX() - ((size/4)), ancora.getY() + (size*0.45)))
        self.braço2 = Rectangle (Point(ancora.getX() + (size*0.4), ancora.getY() - (size*0.35)), Point(ancora.getX() + ((size/4)), ancora.getY() + (size*0.45)))
        self.encosto = Rectangle (Point(ancora.getX() - (size/4),ancora.getY() + (size*35)), Point(ancora.getX() + (size/4), ancora.getY() + (size*30)))
        self.cadeira.setFill(color_rgb(169,216,148))
        self.braço1.setFill(color_rgb(160,197,145))
        self.braço2.setFill(color_rgb(160,197,145))
        self.encosto.setFill(color_rgb(160,197,145))
        self.almofada = Rectangle (Point(ancora.getX() - (size/4),ancora.getY() + (size*0.30)), Point(ancora.getX() + (size/4), ancora.getY()+ size*0.1))
        self.almofada.setFill(color_rgb(217,197,224))
        self.linha = Line(Point(ancora.getX(), ancora.getY() + (size*0.30)), Point(ancora.getX(), ancora.getY() + size*0.1))
        self.efeito1 = Rectangle (Point(ancora.getX() - (size*0.4), ancora.getY() - (size*0.35)), Point(ancora.getX() - ((size/4)), ancora.getY() - (size*0.25)))
        self.efeito2 = Rectangle (Point(ancora.getX() + (size*0.4), ancora.getY() - (size*0.35)), Point(ancora.getX() + ((size/4)), ancora.getY() - (size*0.25)))

        self.xmax = ancora.getX() + (self.size*0.4) + hb#definição do x maximo da cadeira
        self.xmin = ancora.getX() - (self.size*0.4) - hb#definição do x minimo da cadeira
        self.ymax = ancora.getY() + (size*0.45) + hb#definição do y maximo da cadeira
        self.ymin = ancora.getY() - (size*0.35) - hb#definição do y minimo da cadeira
        self.xmed = (self.xmax + self.xmin)/2#definição do x medio da cadeira
        self.ymed = (self.ymax + self.ymin)/2#definição do y medio da cadeira

        self.hitbox = Rectangle(Point(self.xmin , self.ymin ), Point(self.xmax , self.ymax))#definição da hitbox conforme os quatro pontos definidos antes
        self.polt = []
        self.poltrona = [self.cadeira,self.braço1,self.braço2,self.almofada,self.encosto,self.linha,self.efeito1,self.efeito2]
        self.polt.append(self.poltrona)
        
    def cont(self,hX,hY):#define se existe contacto entre o waiter e a cadeira
            if (self.xmin  < hX < self.xmax  and self.ymin  < hY < self.ymax):    
                self.contact = True
                return self.contact
            
    def draw(self, win):#desenha a cadeira
            for polt in self.poltrona:
                polt.draw(win)
            #self.hitbox.draw(win)
            self.ancora = Point(self.retornaAncoraX(), self.retornaAncoraY())
          
            
    def undraw(self):#apaga a cadeira
             for polt in self.poltrona:
                 polt.undraw()
               
    def retornaAncoraX(self):#devolve a coordenada X do ponto centro
                    return self.ancora.getX() 
                
    def retornaAncoraY(self):#devolve a coordenada Y do ponto centro
                    return self.ancora.getY()
 
