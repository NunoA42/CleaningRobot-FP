from graphics import *
from time import *
import math 

class Waiter:
    
    def __init__(self, centro, raio, win):
        
        
        self.circle = Circle(centro, raio)#define o robo composto por 3 circulos
        self.circle2 = Circle(centro,raio*0.8)
        self.circle3 = Circle(centro,raio*0.5)
        self.circle.setFill('white')
        self.circle2.setFill(color_rgb(217,197,224))
        self.circle3.setFill('white')
        
        self.batteryline = Rectangle(Point(centro.getX() - raio*0.4, centro.getY() - raio*0.1),Point(centro.getX() + raio*0.4, centro.getY() + raio*0.1 ))
        self.batterym = []
        for i in range(4):#faz um loop que cria 4 separadores de bateria e adiciona-os a uma lista
            self.batterym.append(Rectangle(Point(centro.getX() - raio * 0.4 + raio * 0.2 * i, centro.getY() - raio * 0.1), Point(centro.getX() - raio * 0.2 + raio * 0.2 * i,centro.getY() + raio * 0.1)))
        for b in self.batterym:
            b.setFill("green")

        self.batOn = False#até ser dito o contrario a bateria não esta ativada e po isso não desenhada nem contabilizada 
        
    def move(self, dx, dy):
        self.circle.move(dx, dy)#move as diferente partes do robo 
        self.circle2.move(dx, dy)
        self.circle3.move(dx, dy)
        self.batteryline.move(dx, dy)
        
        if self.batOn:#se a bateria tiver sido ativada a cada passo que robo da as coordenadas que ele andou são descontadas da bateria
            self.battery = self.battery - abs(dx) - abs(dy)
            
            for b in self.batterym:#verifica o nivel da bateria e pinta os separadores conforme ele esteja
             if self.battery == self.capacity:  
                 b.setFill("green")
            
             elif  round(self.battery) == 0.75*self.capacity:
                 b.setFill("orange")
                 self.batterym[3].setFill("white")
                
             elif round(self.battery) == 0.50*self.capacity:
                 b.setFill("white")
                 self.batterym[1].setFill("yellow")
                 self.batterym[0].setFill("yellow")
                 
                
             elif round(self.battery) == 0.15*self.capacity:
                 b.setFill("white")
                 self.batterym[0].setFill("red")
    
        for b in self.batterym:
            b.move(dx, dy)

    def getX(self):#devolve a coordenada X do robo
        return self.circle.getCenter().getX()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
   
    def getY(self):#devolve a coordenada Y do robo
        return self.circle.getCenter().getY()
    
    def getCenter(self):#devolve o ponto centro do robo
        return self.circle.getCenter()

    def draw(self,win):#desenha o robo
        self.circle.draw(win)
        self.circle2.draw(win)
        self.circle3.draw(win)
            
    def undraw(self):#apaga o robo
        self.circle.undraw()
        self.circle2.undraw()
        self.circle3.undraw()
        
    def drawbattery(self,win):#desenha a bateria
       self.batteryline.draw(win) 
       for b in self.batterym:
          b.draw(win)

    def undrawbattery(self):#apaga a bateria
       self.batteryline.undraw()
       for b in self.batterym:
          b.undraw()              

    def capacity(self,capacity):#define a capacidade total da bateria do robo
        self.capacity = capacity
        
    def battery(self,charge):#define a bateria atual do robo e caso esta método tenha sido chamado ativa a bateria
        self.batOn = True
        self.battery = charge 
       

    def batteryanimation(self, charge):#animação de carregamento do robo quando fica sem bateria
            for c in range(4):
                for b in self.batterym:
                    b.setFill("red")
                    self.batterym[3].setFill("white")
                    self.batterym[2].setFill("white")
                    self.batterym[1].setFill("white") 
                    
                sleep(0.3)
                
                for b in self.batterym:
                    b.setFill("yellow")
                    self.batterym[3].setFill("white")
                    self.batterym[2].setFill("white")
                    
                sleep(0.3)
                
                for b in self.batterym:    
                    b.setFill("orange")
                    self.batterym[3].setFill("white")
                    
                sleep(0.3)
                
                for b in self.batterym:    
                    b.setFill("green")
                    
                sleep(0.3)
                    
            self.battery = charge#a bateria volta a ser o difinido no inicio

    def checkbat(self):#verifica a bateria e delvolve True se estiver abaixo de 15%
        if self.battery <= 0.15*self.capacity:
            return True

