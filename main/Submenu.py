from graphics import*
from MenuButton import MenuButton
from Button import Button



class SubMenu:
    def __init__(self):
        #definir o tamanho da janela e a cor do menu
        self.win = win = GraphWin("Menu", 1000, 600)
        win.setCoords(0,0,1000, 600)
        win.setBackground("white")
        
        #escolher as coordenadas dos butões e respetivos nomes
        self.op1 = MenuButton(win, Point(500,350), 200, 50, "Limpeza-Ficheiro", color_rgb(217,197,224))
        self.op1.activate()
        self.op2 = MenuButton(win, Point(500,280), 200, 50, "Limpeza-Cliques",color_rgb(217,197,224))
        self.op2.activate()
        self.sair = Button(win, Point(500,70), 200, 50, "Sair", "red")
        self.sair.activate()
        self.title = Text(Point(500,470), "Escolha o método de limpeza")
        self.title.setSize(30)
        self.title.setStyle("bold")
        self.title.setFace("arial")
        self.title.setFill('purple')
        self.title.draw(self.win)
        clickmethod = False
        filemethod = False
        
    def clicar(self):
        #definir o que mostrar quando se clica nos botões
        while True:
            pt = self.win.getMouse()
            if self.op1.clicked(pt):
                self.win.close()
                clickmethod = False
                filemethod = True
                break
            elif self.op2.clicked(pt):
                self.win.close()
                clickmethod = True
                filemethod = False
                break
            elif self.sair.clicked(pt):
                self.win.close()
                break   
            
        return [clickmethod,filemethod]     
    
  
              
    
    
    
def main():
    menu2 = SubMenu()
    menu2.clicar()

