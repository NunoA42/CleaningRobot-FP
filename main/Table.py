from graphics import *

class Table:
    def __init__(self, ancora, size, hb):#define uma mesa e junta as componentes numa lista
        self.ancora = ancora
        self.size = size
        self.mesa = Circle(ancora, size)
        self.guardanapo1 = Polygon(Point(ancora.getX() - size * 0.35, ancora.getY() + size * 0.55), Point(ancora.getX(), ancora.getY() + size * 0.9), Point(ancora.getX() + size * 0.35, ancora.getY() + size * 0.55), Point(ancora.getX(), ancora.getY() + size * 0.2))
        self.prato1 = Circle(Point(ancora.getX(), ancora.getY() + size * 0.55), size * 0.22)
        self.guardanapo2 = Polygon(Point(ancora.getX() - size * 0.35, ancora.getY() - size * 0.55), Point(ancora.getX(), ancora.getY() - size * 0.9), Point(ancora.getX() + size * 0.35, ancora.getY() - size * 0.55), Point(ancora.getX(), ancora.getY() - size * 0.2))
        self.prato2 = Circle(Point(ancora.getX(), ancora.getY() - size * 0.55), size * 0.22)
        self.mesa.setFill("white")
        self.guardanapo1.setFill(color_rgb(169,216,148))
        self.prato1.setFill("white")
        self.guardanapo2.setFill(color_rgb(169,216,148))
        self.prato2.setFill("white")
        
        self.conj = []
        self.conj.append([self.guardanapo1.clone(), self.prato1.clone()])
        
        for i in range(2):#define os pratos e guardanapos usando um loop
            guardanapoclone = self.guardanapo1.clone()
            pratoclone = self.prato1.clone()
            guardanapoclone.move(-0.55 * size + 1.1 * i * size, -0.55 * size + 0.01 * i * size)
            pratoclone.move(-0.55 * size + 1.1 * i * size, -0.55 * size + 0.01 * i * size)
            self.conj.append([guardanapoclone, pratoclone])
        
        
        self.xmax = ancora.getX() + size + hb #definição do x maximo da mesa
        self.xmin = ancora.getX() - size - hb #definição do x minimo da mesa
        self.ymax = ancora.getY() + size + hb #definição do y maximo da mesa
        self.ymin = ancora.getY() - size - hb #definição do x minimo da mesa
        self.xmed = (self.xmax + self.xmin) / 2 #definição do x medio da mesa
        self.ymed = (self.ymax + self.ymin) / 2 #definição do y medio da mesa

        self.hitbox = Rectangle(Point(self.xmin, self.ymin), Point(self.xmax, self.ymax))

    def cont(self, hX, hY):#define se existe contacto entre o waiter e a mesa
        if self.xmin < hX < self.xmax and self.ymin < hY < self.ymax:
            self.contact = True
            return self.contact

    def draw(self, win):#desenha a mesa
        self.mesa.draw(win)
        self.guardanapo2.draw(win)
        self.prato2.draw(win)
        for c in self.conj:
            for obj in c:
                obj.draw(win)
        #self.hitbox.draw(win)

    def undraw(self):#apaga a mesa
        self.mesa.undraw()
        for gra in self.conj:
            for obj in gra:
                obj.undraw()
        self.guardanapo2.undraw()
        self.prato2.undraw()
        
    def retornaAncoraX(self):#devolve a coordenada X do ponto centro
                    return self.ancora.getX() 
                
    def retornaAncoraY(self):#devolve a coordenada Y do ponto centro
                    return self.ancora.getY()
    
    def gettable(self):
                return self.size
