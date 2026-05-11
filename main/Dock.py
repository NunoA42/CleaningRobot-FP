from graphics import *

class Dock:#define as docks 
    
    def __init__(self,ancora,width,height):
        self.ancora = ancora
        self.dock1 = Rectangle(Point(ancora.getX()-width/2,ancora.getY() -\
                                    height/2), Point(ancora.getX()+width/2,ancora.getY() + height/2))
        self.dock1.setFill("lavender")

    def draw(self, win):
        self.dock1.draw(win)
        
    def getX(self):#devolve a coordena X
        return self.ancora.getX()
    
    def getY(self):#devolve a coordena Y
        return self.ancora.getY()

    def getXY(self):#devolve o ponto centro
        return self.ancora
            
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height 
    
 
     
