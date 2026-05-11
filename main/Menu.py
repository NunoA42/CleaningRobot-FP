from graphics import *
from MenuButton import MenuButton
from Button import Button


class Menu:
    def __init__(self):
        # define a janela e a cor do menu
        self.win = win = GraphWin("Menu", 1000, 600)
        win.setCoords(0, 0, 1000, 600)
        win.setBackground("white")
        
        # Escolhe as coordenadas dos botões
        self.option1 = MenuButton(win, Point(500, 350), 220, 50, "1ª Implementação", color_rgb(217, 197, 224))
        self.option1.activate()
        self.option2 = MenuButton(win, Point(500, 280), 220, 50, "2ª Implementação", color_rgb(217, 197, 224))
        self.option2.activate()
        self.option3 = MenuButton(win, Point(500, 210), 220, 50, "3ª Implementação-Ficheiro", color_rgb(217, 197, 224))
        self.option3.activate()
        self.option4 = MenuButton(win, Point(500, 140), 220, 50, "3ª Implementação-Aleat.ger", color_rgb(217, 197, 224))
        self.option4.activate()
        self.leave = Button(win, Point(500, 70), 200, 50, "Sair", "grey")
        self.leave.activate()
        self.title = Text(Point(500, 470), "Menu")
        self.title.setSize(30)
        self.title.setStyle("bold")
        self.title.setFace("arial")
        self.title.setFill('purple')
        self.title.draw(self.win)

    def clicar(self):
        # Define o que acontece quando os diferentes botões sao clicados
        goal = True
        while goal:
            pt = self.win.getMouse()
            if self.option1.clicked(pt):
                self.win.close()
                return 1
                goal = False
            elif self.option2.clicked(pt):
                self.win.close()
                return 2
                goal = False
            elif self.option3.clicked(pt):
                self.win.close()
                return 3 
                goal = False
            elif self.option4.clicked(pt):
                self.win.close()
                return 4  
                goal = False
            elif self.leave.clicked(pt):
                self.win.close()
                goal = False


def main():
    menu1 = Menu()
    menu1.clicar()



