from graphics import *
from time import *
from math import *
from random import *
from Menu import Menu
from Submenu import SubMenu
from Button import Button
from Waiter import Waiter
from Mess import Mess
from Dock import Dock
from Table import Table
from FishTank import FishTank
from Chair import Chair
from Plant import Plant

#Primeiramente definimos as funções usadas em todas, ou em quase todas, implementações, ou usadas no menu.

def vetor(aX,aY,bX,bY): #definição de um vetor que vai do ponto b para o a
    dX = float(aX-bX) #componente X desse vetor
    dY = float(aY-bY) #componente Y desse vetor
    nv = sqrt(dX**2 + dY**2) #calculo da norma do veotr
    vetoruni = [dX/nv,dY/nv,nv] #lista com: componente x do vetor unitário como a mesma direção e sentido, y desse vetor unitário, norma do vetor
  
    return vetoruni
             
def invalidlocal(obstacles, clique, wradius, width, height): #função que dita se o clique feito pelo usuário foi válido ou não   
    for obj in obstacles: 
        if (obj.xmin - wradius<clique.getX()<obj.xmax + wradius and obj.ymin - wradius<clique.getY()<obj.ymax+ wradius):
            return True #não será válido o clique se estiver a menos de duas vezes o raio de distãncia em relação aos obstáculos
        
        if (wradius*2>clique.getX() or wradius * 2>clique.getY()) or (clique.getX()>width - 2 * wradius or clique.getY()>height - 2 * wradius):
            return True #não será válido o clique se estiver a menos de duas vezes o raio de distãncia em relação ao limite da sala

        
def choosedock(waiter,dock1,dock2): #escolhe a dock mais perto e devolve as coordenadas do centro dela
    v1 =  vetor(dock1.getX(),dock1.getY(),waiter.getX(),waiter.getY()) #vetor entre o waiter e a dock1
    v2 =  vetor(dock2.getX(),dock2.getY(),waiter.getX(),waiter.getY()) #vetor entre o waiter e a dock2
  
    if v1[2] <= v2[2]:  #comparaçãos das normas dos dois vetores
        p = dock1.getXY()
    else:
        p = dock2.getXY()
  
    return p

def Limpeza(waiter, wradius, l, speed, move):#função que dita a limpeza à volta da sujidade, quando o robo a atinge,
                                             # fazendo um quadrado à volta dela com lado igual a duas vezes o raio do robo              
    while waiter.getY() < l.getY() + wradius:
        waiter.move(0, move)
        update(speed)

    while waiter.getX() < l.getX() + wradius:
        waiter.move(move, 0)
        update(speed)

    while waiter.getY() > l.getY() - wradius:
        waiter.move(0, -move)
        update(speed)

    while waiter.getX() > l.getX() - wradius:
        waiter.move(-move, 0)
        update(speed)

    while waiter.getY() < l.getY() + wradius:
        waiter.move(0, move)
        update(speed)

    while waiter.getX() < l.getX():
        waiter.move(move, 0)
        update(speed)

    while waiter.getY() > l.getY():
        waiter.move(0, -move)
        update(speed)     
        
def gocharge(dock1,dock2,waiter,speed,charge,traject,move):#função para quando o robo fica sem bateria
    if waiter.checkbat():# caso a bateria esteja a menos de 15% do total a função acontece
    
        if abs(waiter.getX()-dock1.getX())<=1.5:#caso o robo esteja com X aproximadamente igual à dock 1 direje-se até ela, descendo
            while dock1.getY() < waiter.getY():
                waiter.move(0,-move)
                update(speed)
            waiter.batteryanimation(charge)#animação de carregamento
            while traject > waiter.getY():#volta à posição em que estava antes de carregar
                waiter.move(0,move)
                update(speed)
                
        if abs(waiter.getX()-dock2.getX())<=1.5:#caso o robo esteja com X aproximadamente igual à dock 2 direje-se até ela
            while dock2.getY() > waiter.getY():
                waiter.move(0,move)
                update(speed)
            waiter.batteryanimation(charge) #animação de carregamento  
            while traject < waiter.getY():#volta à posição em que estava antes de carregar
                waiter.move(0,-move)
                update(speed)
            
def searchmess(sujidades, waiter, traject, reach, wradius, obstaculos, update, move):#função que procura as sujidades
    a = len(sujidades)
    for j in range(0,a,1):#loop que acontece o mesmo numero de vezes que o numero de sujidades que há
    
        x = sujidades[j].getX()#coordenada x da sujidade
        y = sujidades[j].getY()#coordenada y da sujidade
        l = sujidades[j].getCenter()#ponto centro da sujidade
        
        if abs(x-waiter.getX())<=move and abs(y-waiter.getY())<=reach:#caso o x da sujidade seja aproximadamente igual ao do waiter e
                                                                      #o y estiver dentro do intervalo antes definido como reach                                                                   
            vl = vetor( x, y, waiter.getX(),  waiter.getY())#vetor entre a sujidade e o waiter
            while vl[2] >= 1:#enquanto a norma desse vetor for maior que 1 o robo move-se segundo esse vetor
                waiter.move(vl[0]*move,vl[1]*move)
                vl = vetor( x, y, waiter.getX(),  waiter.getY())#atualiza o vetor
                
            Limpeza(waiter, wradius, l, update, move)#faz o movimento de limpeza
            sujidades[j].undraw()#apaga a sujidade
            sujidades[j].centro(-20,-20)#coloca o ponto da sujidade fora da janela para não interferir com o movimeno do robo
            
            #volta do waiter para o trajeto de limpeza da sala, se este entrar em contacto com um obstaculos é quebrado este loop
            while waiter.getY() < traject:#se o robo estiver abaixo do trajeto em que estava antes
                  waiter.move(0,move)
                  if obstaculos[0].cont(waiter.getX(), waiter.getY()) or obstaculos[1].cont(waiter.getX(), waiter.getY()) or obstaculos[2].cont(waiter.getX(), waiter.getY()) \
                      or obstaculos[3].cont(waiter.getX(), waiter.getY()) or obstaculos[4].cont(waiter.getX(), waiter.getY()):
                          break
                      
            while waiter.getY() > traject:#se o robo estiver acima do trajeto em que estava antes
                  waiter.move(0,-move)
                  if obstaculos[0].cont(waiter.getX(), waiter.getY()) or obstaculos[1].cont(waiter.getX(), waiter.getY()) or obstaculos[2].cont(waiter.getX(), waiter.getY()) \
                      or obstaculos[3].cont(waiter.getX(), waiter.getY()) or obstaculos[4].cont(waiter.getX(), waiter.getY()):
                          break
       
def exitbutton(win,ancora, width, height): #função que define o botão que permite sair das implementações    
     exitButton =  Button (win, ancora, width, height , "Quit", "red") #usa classe Button para criar o botão
     exitButton.activate() 
     
     return exitButton
     
def exitclicked(exitButton, p, win):#se o botão para sair for premido volta ao menu
     if exitButton.clicked(p):
             win.close()
             menu()
                
def menu():#definição do menu, usando a classe com o mesmo nome
        
        menu1 = Menu()
        option = menu1.clicar()
        if option == 1:
            Imp1()
        if option == 2:
            Imp2()
        if option == 3:
            filemenu()
        if option == 4:
            aleatmenu()

def filemenu():#submenu para a 3º implementação quando as coordenadas do obtáculos são retiradas dum ficheiro  
    menu2 = SubMenu()
    [op1, op2] = menu2.clicar()
    Imp3File(op1 ,op2)

def aleatmenu():#submenu para a 3º implementação quando as coordenadas do obtáculos são aleatórias
    menu2 = SubMenu()
    [op1, op2] = menu2.clicar()
    Aleatger(op1 ,op2)
    
def aleatpoint(win, wradius, width, height, buttonwidth, buttonheight):# Atribuição de coordenadas aleatórias aos obstáculos
    listobs = []
    
    while len(listobs) != 5:  # Definimos 5 obstáculos
        #escolhe uma coordenada x e y de maneira a que os obstáculos estejam a uma distância que o robot 
        #consiga passar entre eles e entre eles e  a parede
        randomx = randrange(2*wradius + 60 + wradius, width - 2*wradius - 60 -wradius, 2*60 + 2*wradius + 7)  
        randomy = randrange(2*wradius + 60 + wradius, height - 2*wradius - 60, 2*wradius + 2*60 + 2*wradius)
        
        if [randomx, randomy] in listobs:
            continue
       
        listobs.append([randomx, randomy])
    
    formas = []
    
    for coordinates in listobs:
        x, y = coordinates
        
        # Escolha aleatória do tipo de forma
        forma_type = choice(["fishtank", "table", "chair", "plant"])
        
        if forma_type == "fishtank":
            forma = FishTank(Point(x, y), 40, wradius)
        elif forma_type == "table":
            forma = Table(Point(x, y), 60, wradius)
        elif forma_type == "chair":
            forma = Chair(Point(x, y), 70, wradius)
        elif forma_type == "plant":
            forma = Plant(Point(x, y), 25, wradius)
        
        formas.append(forma)
    
    return formas

def Imp1():
    #Cria um robo, waiter, omnidirecional que se desloca até às sujidades, definidas pelo utilizador com um clique do rato,
    # quando lá chega limpa-as fazendo um movimento que cobra cerca do dobro da àrea do robo. Por fim volta à dock que esteja mais perto.
    #Tem também de desviar-se do obstáculo, que é uma mesa.
    
    width = 1000  # Largura da janela
    height = 600  # Altura da janela
    
    #Definição da janela gráfica
    win = GraphWin("Projeto", width, height)
    win.setBackground(color_rgb(223, 209, 196))
    win.setCoords(0, 0, 1000, 600) 

    #definição e desenho da docks
    dock1 = Dock(Point(45, 45), 90, 90)
    dock2 = Dock(Point(955, 555), 90, 90)
    docks = [dock1.getXY(), dock2.getXY()]
    dock1.draw(win)
    dock2.draw(win)

    #Definição do robô
    wradius = 35 #raio do robo
    waiter = Waiter(Point(45, 45), wradius , win) 
    
    #Definição da mesa
    table = Table( Point(500, 300), 80, wradius)
    table.draw(win)
    waiter.draw(win)

    #Definição da mensagem que aparece quando clica-se num ponto inválido
    errorbox = Rectangle( Point(width/2 - width/10, 0), Point( width/2 + width/10, 50))
    errorbox.setWidth(4)
    errorbox.setFill("Red")
    errorbox.setOutline("White")
    errortext = Text(Point(width/2, 25), "Invalid point, try again")
    errortext.setFill("White")

    #botão para voltar ao menu
    exitButton = exitbutton(win, Point(940, 40), 100,60 )

    pointchosen = False 
    started = True
    #lista com os obstáculos
    obstacles = []
    obstacles.append(table)


    while started:
        errormsg = True
        if pointchosen == False:
            
            p = win.getMouse()
            exitclicked(exitButton, p, win)

            while invalidlocal(obstacles, p, wradius, width, height ):#se o clique for inválido pede para clicar outra vez até ele ser válido
                if errormsg == True:
                    errorbox.draw(win)
                    errortext.draw(win)
                    
                p = win.getMouse()
                errormsg = False
                
            mess = Mess(p,30)#define a sujidade no ponto clicado
            mess.draw(win)#desenha a sujidade
            
            waiter.undraw()#apaga e desenho o waiter para assegurar que fica acima da sujidade
            waiter.draw(win)
            
            errorbox.undraw()#apaga a mensagem
            errortext.undraw()

            pointchosen = True

        if pointchosen == True:
            vl = vetor(p.getX(), p.getY(), waiter.getX(), waiter.getY())#vetor entre o robo e a sujidade
            while vl[2] > 1:#enquanto a norma do vetor for maior que 1 o robo segue esse vetor
                #condição para quando há contacto entre o robo e a hitbox do objeto
                if (waiter.getX()  < table.xmin  and p.getY() < table.ymed) or (waiter.getX() > table.xmax  and p.getY() < table.ymed):
                    dx = 0
                    dy = -1
                elif (waiter.getX() > table.xmax  and p.getY() > table.ymed) or (waiter.getX() < table.xmin  and p.getY() > table.ymed):
                    dx = 0
                    dy = 1
                elif (waiter.getY() > table.ymax  and p.getX() > table.xmed) or (waiter.getY() < table.ymin  and p.getX() > table.xmed):
                    dx = 1
                    dy = 0
                elif (waiter.getY() > table.ymax  and p.getX() < table.xmed) or (waiter.getY() < table.ymin  and p.getX() < table.xmed):
                    dx = -1
                    dy = 0 
    
                if table.cont(waiter.getX(), waiter.getY()):#caso acha contacto obedece às condições definidas antes
                    waiter.move(dx, dy)
                    update(700)
                    
                else:
                    vl = vetor(p.getX(), p.getY(), waiter.getX(), waiter.getY())#se não houver contacto segue o vetor vl e vai atualizando-o
                    waiter.move( vl[0], vl[1])
                    update(700)

            Limpeza(waiter, wradius, p, 600, 1)#faz o movimento de Limpeza
            mess.undraw()
            p = choosedock(waiter, dock1, dock2)#escolhe a dock mais perto
            pointchosen = False
            sleep(0.5)

        vd = vetor(p.getX(), p.getY(), waiter.getX(), waiter.getY())#calcula o vetor entre o robo e a dock mais perto
        while vd[2] > 1:#enquanto a norma do vetor for maior que 1 o robo segue esse vetor
            vd = vetor(p.getX(), p.getY(), waiter.getX(), waiter.getY())
            waiter.move( vd[0], vd[1])
                        
            update(700)
            
def Imp2():
    #Na segunda implementação adicionamos mais 4 obstáculos e a bateria que obriga o robo a ir carregar a uma das docks caso já não tenha,
    #o movimento nesta implementação será difente no sentido que o waiter terá de limpar toda a sala e ao passar por pontos de sujidade
    # definidos pelo utilizador deverá limpa-los
    
    width = 1000  # Largura da janela
    height = 600  # Altura da janela
    buttonwidth = 100 # Largura dos botões
    buttonheight = 50 # Altura dos botões
    speed = 600 # Numero que será introduzido nos updates para o movimento
    
    #Definição da janela
    win = GraphWin("Projeto", width, height)
    win.setBackground(color_rgb(223, 209, 196))
    win.setCoords(0, 0, 1000, 600) 

    #Definição das docks
    dock1 = Dock(Point(37.5, 37.5), 75, 75)
    dock2 = Dock(Point(962.5, 562.5), 75, 75)
    docks = [dock1.getXY(), dock2.getXY()]
    dock1.draw(win)
    dock2.draw(win)

    #definição do robo
    wradius = 35 #raio do robo  
    waiter = Waiter(Point(37.5, 37.5), wradius , win)
    waiter.draw(win)
    waiter.drawbattery(win) #desenha a bateria
    charge = (1000*7 + 600)*2 #bateria do robo, corresponde a duas vezes a àrea de navegação
    waiter.capacity(charge) #define a capacidade máxima da bateria do robo
    waiter.battery(charge) #define a bateria atual do robo

    sujidades = []#lista que irá conter as sujidades

    #definição da mensagem de erro
    errorbox = Rectangle(Point(width/2 - width/10,0), Point(width/2 + width/10,50))
    errorbox.setWidth(4)
    errorbox.setFill("Red")
    errorbox.setOutline("White")
    errortext = Text(Point(width/2, 25), "Invalid point, try again")
    errortext.setFill("White")
    
    #define o botão que inicia o movimento
    startbutton = Button(win, Point(width - buttonwidth/2 - 10, 3 * (buttonheight/2) + 10*2) , buttonwidth, buttonheight, "Start", "Green")
    startbutton.activate() 
    #define o botão para voltar ao menu 
    exitButton = exitbutton(win, Point(width - buttonwidth/2 - 10, buttonheight/2 + 10), buttonwidth,buttonheight )
    
    #Definição e desenho dos obstáculos
    table = Table(Point(800,400), 80, wradius)
    table.draw(win)
    plant = Plant(Point(300,200), 30, wradius)
    plant.draw(win)
    fishtank = FishTank(Point(500,400), 40, wradius)
    fishtank.draw(win)
    chair1 = Chair(Point(200,400), 80, wradius)
    chair1.draw(win)   
    chair2 = Chair(Point(600,150), 80, wradius)
    chair2.draw(win) 
    
    #variaveis que ditam o acontecimento dos diferentes loops
    goal = False
    pointchosen = False
    started = True
    
    group = []#cria uma lista com os obstáculos
    for g in [table,fishtank,chair1,chair2,plant]:
        group.append(g)
        
    while started:
      errormsg = True

      if pointchosen == False:#primeiro loop antes dos pontos estarem escolhidos
          
         p = win.getMouse()#obtém as coordenadas do clique do utilizador
         exitclicked(exitButton, p, win)
        
         if startbutton.clicked(p) and len(sujidades)>0:#se o utilizador clicar no start e houver mais de uma sujidade inicia o movimento
             waiter.undraw()#apaga e desenha o robo e bateria para garantir que ficam por cima das sujidades
             waiter.undrawbattery()
             waiter.draw(win)
             waiter.drawbattery(win)
             pointchosen = True# alteraçao das variaveis para mudar de loop
             goal=True
             continue
           
         if startbutton.clicked(p) and len(sujidades)==0:#assegura se ao clicar no start sem haver sujidades não desenha uma em cima do botão
             continue
            
         while invalidlocal(group, p, wradius, width, height ):#se o clique introduzido não for válido desenha a mensagem de erro
             if errormsg == True:
                    errorbox.draw(win)
                    errortext.draw(win)
             p = win.getMouse()
             errormsg = False
             
         #caso passe por todas as condições anteriores utiliza o clique como coordenadas para a sujidade e adiciona-a a uma lista   
         sujidades.append(Mess(p,30))
         sujidades[len(sujidades)-1].draw(win)
         errorbox.undraw()#apaga a mensagem de erro se tiver desenhada
         errortext.undraw() 

      if pointchosen == True:#inicia-se o loop do movimento
          
          gocharge(dock1,dock2,waiter,speed,charge,waiter.getY(),1)#caso não tenha bateria carrega
          
          while goal == True:
            #movimento quando o robo começa na dock de baixo e acaba na de cima
            if abs(waiter.getX()-37.5)<=1 and abs(waiter.getY()-37.5)<=1 and goal == True:#verifica as coordenadas do robo     
            
                for i in range(3):#executa este loop 3 vezes e usa o i para fazer o calculo do y em que o robo deverá estar em cada ciclo                     
                    while waiter.getX() <= 962.5:#movimento para a direita
                    
                        for g in group:#condições que ditam o movimento quando o robo entra em contacto com um dos objetos
                        
                            if (g.xmin - 3 < waiter.getX() < g.xmin or g.xmax + 3 > waiter.getX() > g.xmax) and \
                                g.ymin <= waiter.getY() <= g.ymax:
                                if g.ymax - waiter.getY() < waiter.getY()- g.ymin:
                                        dx, dy = 0, 1
                                elif g.ymax - waiter.getY() > waiter.getY()- g.ymin:
                                        dx, dy = 0, -1
             
                        while table.cont(waiter.getX(), waiter.getY()) or fishtank.cont(waiter.getX(), waiter.getY()) or chair1.cont(waiter.getX(), waiter.getY())\
                                or chair2.cont(waiter.getX(), waiter.getY()) or plant.cont(waiter.getX(), waiter.getY()):
                                waiter.move(dx, dy)#se entrar em contacto segue as condições ditadas antes
                                
                        #volta para o trajeto ao fim de se desviar dos obstáculos        
                        for g in group:
                            if( g.xmax + 5 > waiter.getX() > g.xmax  ) and (g.ymin > waiter.getY() > g.ymin - 5 ):
                                while waiter.getY() < 37.5 + (87.5 * ((i-1) * 2 + 2)):
                                    waiter.move(0,1)
                                    
                            if( g.xmax + 5 > waiter.getX() > g.xmax ) and(g.ymax + 5 > waiter.getY() > g.ymax):
                                while waiter.getY() > 37.5 + (87.5 * ((i-1) * 2 + 2)):
                                    waiter.move(0,-1)

                        #executa a função que procura por sujidades                  
                        searchmess(sujidades, waiter, 37.5 + (87.5 * ((i-1) * 2 + 2)), 47.5 , wradius , group, 600, 1)
                  
                        waiter.move(1, 0)
                        update(600)
                            
                    while waiter.getY() <= 37.5 + (87.5 * (i * 2 + 1)):#anda para cima até atingir o y do trajeto de maneira limpar a sala toda
                        waiter.move(0, 1)
                        update(600)
                        
                    #executa a função que verifica se precisa de ir limpar        
                    gocharge(dock1,dock2,waiter,speed,charge,37.5 + (87.5 * (i * 2 + 1)),1)
                
                    while waiter.getX() >= 37.5:#movimento para a esquerda
                        
                        for g in group:#condições que ditam o movimento quando o robo entra em contacto com um dos objetos
                            if (g.xmin - 3 < waiter.getX() < g.xmin  or g.xmax + 3 > waiter.getX() > g.xmax ) and \
                                g.ymin <= waiter.getY() <= g.ymax:
                                if g.ymax - waiter.getY() < waiter.getY()- g.ymin:
                                    dx, dy = 0, 1
                                elif g.ymax - waiter.getY() > waiter.getY()- g.ymin:
                                    dx, dy = 0, -1        
                        
                        while  table.cont(waiter.getX(), waiter.getY()) or fishtank.cont(waiter.getX(), waiter.getY()) or chair1.cont(waiter.getX(), waiter.getY()) \
                                or chair2.cont(waiter.getX(), waiter.getY()) or plant.cont(waiter.getX(), waiter.getY()):
                                waiter.move(dx, dy)#se entrar em contacto segue as condições ditadas antes
   
                        #volta para o trajeto ao fim de se desviar dos obstáculos          
                        for g in group:                       
                                if( g.xmin  > waiter.getX() > g.xmin - 3 ) and (g.ymin > waiter.getY() > g.ymin - 3 ):
                                     while waiter.getY() < 37.5 + (87.5 * (i * 2 + 1)):
                                       waiter.move(0,1)

                                if( g.xmin > waiter.getX() > g.xmin - 3 ) and (g.ymax + 3 > waiter.getY() > g.ymax):
                                     while waiter.getY() > 37.5 + (87.5 * (i * 2 + 1)):
                                       waiter.move(0,-1)

                        #executa a função que procura por sujidades               
                        searchmess(sujidades, waiter, 37.5 + (87.5 * (i * 2 + 1)), 47.5 , wradius, group, 600, 1)#
                                       
                        waiter.move(-1, 0)
                        update(600)
                            
                    while waiter.getY() <= 37.5 + 87.5 * (i * 2 + 2):#anda para cima até atingir o y do trajeto de maneira limpar a sala toda
                        waiter.move(0, 1)
                        update(600)
                        
                    #executa a função que verifica se precisa de ir limpar    
                    gocharge(dock1,dock2,waiter,speed,charge,37.5 + 87.5 * (i * 2 + 2),1)
                                            
                while waiter.getX() <= 962.5:#anda para a direita até atingir a dock de cima, verificando se não sujidades
                        searchmess(sujidades, waiter, 562.5, 47.5 , wradius, group, 600, 1)                  
                        waiter.move(1, 0)
                        update(600)
                        
                        
                if abs(waiter.getX() - 962.5) <= 1 and abs(waiter.getY() - 562.5) <= 1:#verifica as coordenadas do robo quando até ser atingida a dock de cima
                        sujidades = [] #esvazia a lista das sujidades
                        goal = False #muda as variaveis de maneira a sair do loop do movimento
                        pointchosen = False

########################################################################################################################################################################
            
            #movimento oposto ao anterior, quando o robo começa na dock de cima e acaba na de baixo                  
            if abs(waiter.getX() - 962.5) <= 1 and abs(waiter.getY() - 562.5) <= 1 and goal == True: #verifica as coordenadas do robo
            
                for i in range(3):#executa este loop 3 vezes e usa o i para fazer o calculo do y em que o robo deverá estar em cada ciclo 
                    
                    while waiter.getX() >= 37.5:#movimento para a esquerda
                        for g in group:#condições que ditam o movimento quando o robo entra em contacto com um dos objetos
                            if (g.xmin - 3 < waiter.getX() < g.xmin  or g.xmax + 3 > waiter.getX() > g.xmax) and \
                                        g.ymin <= waiter.getY() <= g.ymax:
                                if g.ymax - waiter.getY() < waiter.getY()- g.ymin:
                                        dx, dy = 0, 1
                                elif g.ymax - waiter.getY() > waiter.getY()- g.ymin:
                                        dx, dy = 0, -1
        
                        
                        while  table.cont(waiter.getX(), waiter.getY()) or fishtank.cont(waiter.getX(), waiter.getY()) or chair1.cont(waiter.getX(), waiter.getY()) \
                        or chair2.cont(waiter.getX(), waiter.getY()) or plant.cont(waiter.getX(), waiter.getY()):
                            waiter.move(dx, dy)#se entrar em contacto segue as condições ditadas antes
                            
                        #volta para o trajeto ao fim de se desviar dos obstáculos        
                        for g in group:                       
                            if( g.xmin > waiter.getX() > g.xmin - 4 ) and (g.ymin > waiter.getY() > g.ymin - 4 ):
                                while waiter.getY() < 562.5 - (87.5 * ((i-1) * 2 + 2)):
                                    waiter.move(0,1)
                            if( g.xmin > waiter.getX() > g.xmin - 4 ) and (g.ymax + 4 > waiter.getY() > g.ymax ):
                                while waiter.getY() > 562.5 - (87.5 * ((i-1) * 2 + 2)):
                                    waiter.move(0,-1)
                        
                        #executa a função que procura por sujidades     
                        searchmess(sujidades, waiter, 562.5 - (87.5 * ((i-1) * 2 + 2)), 47.5 , wradius, group, 600, 1)
                            
                        waiter.move(-1, 0)
                        update(600)
                        
                    #executa a função que verifica se precisa de ir limpar           
                    gocharge(dock1,dock2,waiter,speed,charge,562.5 - (87.5 * (i * 2 + 1)),1)   
                            
                    while waiter.getY() >= 562.5 - (87.5 * (i * 2 + 1)):#anda para baixo até atingir o y do trajeto de maneira limpar a sala toda
                        waiter.move(0, -1)
                        update(600)
                                
                    while waiter.getX() <= 962.5:#movimento para a direita
                    
                            for g in group:#condições que ditam o movimento quando o robo entra em contacto com um dos objetos
                                if (g.xmin - 3 < waiter.getX() < g.xmin or g.xmax + 3 > waiter.getX() > g.xmax) and \
                                        g.ymin <= waiter.getY() <= g.ymax:
                                    if g.ymax - waiter.getY() < waiter.getY()- g.ymin:
                                        dx, dy = 0, 1
                                    elif g.ymax - waiter.getY() > waiter.getY()- g.ymin:
                                        dx, dy = 0, -1
             
                            while  table.cont(waiter.getX(), waiter.getY()) or fishtank.cont(waiter.getX(), waiter.getY()) or chair1.cont(waiter.getX(), waiter.getY()) \
                                or chair2.cont(waiter.getX(), waiter.getY()) or plant.cont(waiter.getX(), waiter.getY()):
                                waiter.move(dx, dy)#se entrar em contacto segue as condições ditadas antes
                            
                            #volta para o trajeto ao fim de se desviar dos obstáculos     
                            for g in group:
                                if( g.xmax + 3 > waiter.getX() > g.xmax ) and (g.ymin > waiter.getY() > g.ymin - 3 ):
                                    while waiter.getY() < 562.5 - (87.5 * (i * 2 + 1)):
                                          waiter.move(0,1)
                                if( g.xmax + 3 > waiter.getX() > g.xmax ) and(g.ymax + 3 > waiter.getY() > g.ymax ):
                                    while waiter.getY() > 562.5 - (87.5 * (i * 2 + 1)):
                                          waiter.move(0,-1)
                            
                            #executa a função que procura por sujidades 
                            searchmess(sujidades, waiter, 562.5 - (87.5 * (i * 2 + 1)), 47.5 , wradius, group, 600, 1)
                            
                            waiter.move(1, 0) 
                                                
                    #executa a função que verifica se precisa de ir limpar    
                    gocharge(dock1,dock2,waiter,speed,charge, 562.5 - (87.5 * (i * 2 + 2)),1)      
                        
                    while waiter.getY() >= 562.5 - (87.5 * (i * 2 + 2)):
                            waiter.move(0, -1)
                                        
                        
                while waiter.getX() >= 37.5:#anda para a esquerda até atingir a dock de baixo
                
                      searchmess(sujidades, waiter, 37.5, 47.5 , wradius, group, 600, 1)  
                      waiter.move(-1, 0)
                      update(600)
                    
                if abs(waiter.getX() - 37.5) <= 1 and abs(waiter.getY() - 37.5) <= 1:#verifica as coordenadas do robo quando até ser atingida a dock de baixo
                      sujidades = [] #esvazia a lista das sujidades
                      goal = False #muda as variaveis de maneira a sair do loop do movimento
                      pointchosen = False
                      
#Na terceira implementação a prinicipal diferença é que os obstaculos eram retirados dum ficheiro e as sujidades ou eram introduzidas pelo
#clique do utilizador ou também eram retiradas dum ficheiro. Decidimos dividir esta implementação em duas funções                         

def Imp3File(click,file):
#Nesta as coordenadas dos obstáculos eram retiradas dum ficheiro 
    
    #Abre o ficheiro sala.txt e cria uma lista com as diferentes coordenadas e valores
    arquivo1 = open("main/Sala.txt", "r")
    posiçoes = arquivo1.readlines()
    arquivo1.close()

    # Extrair as dimensões da janela do arquivo
    width = int(posiçoes[1].split()[0])
    height = int(posiçoes[1].split()[1])
    buttonwidth = 10
    buttonheight = 5
    speed = 600
    
    #Define a janela gráfica
    win = GraphWin("Projeto", width, height)
    win.setBackground(color_rgb(223, 209, 196))
    win.setCoords(0, 0, 100, 100)
    
    #Define as docks
    dock1 = Dock(eval(posiçoes[5]), 10, 10)
    dock2 = Dock(eval(posiçoes[6]), 10, 10) 
    docks = [dock1.getX(), dock1.getY(), dock2.getX(), dock2.getY()]
    dock1.draw(win)
    dock2.draw(win)
    
    #Define o robo
    wradius = 4.5
    waiter = Waiter(Point(5, 5), wradius , win)
    
    #Define a mensagem que aparece quando é introduzido um clique inválido
    errorbox = Rectangle(Point(width/15 - width/65,0), Point(width/15 + width/65,8))
    errorbox.setWidth(4)
    errorbox.setFill("Red")
    errorbox.setOutline("White")
    errortext = Text(Point(width/15, 4), "Invalid point, try again")
    errortext.setFill("White")
    
    #Define e ativa o botão que inicia o movimento
    startbutton = Button(win, Point(width/8.5 + buttonwidth/2 , 3 * (buttonheight/2) + 1*2) , buttonwidth, buttonheight, "Start", "Green")
    startbutton.activate() 
    
    #Define o botão para voltar ao menu
    exitButton = exitbutton(win, Point(width/8.5 + buttonwidth/2 , buttonheight/2 + 1), buttonwidth,buttonheight )
    
    #Definição e desenho dos diferentes obstáculos
    table = Table(eval(posiçoes[7].split(":")[1]), 9, wradius)
    table.draw(win)
    chair2 = Chair(eval(posiçoes[8].split(":")[1]), 12, wradius)
    chair2.draw(win)
    chair1 = Chair(eval(posiçoes[9].split(":")[1]), 12, wradius)
    chair1.draw(win)
    table2 = Table(eval(posiçoes[10].split(":")[1]), 9, wradius)
    table2.draw(win)
    plant = Plant(eval(posiçoes[11].split(":")[1]), 3.5, wradius)
    plant.draw(win)
    
    #Desenha o robo
    waiter.draw(win)
    waiter.drawbattery(win)
    charge = (100 * 9 + 100)*2#bateria do robo, corresponde a duas vezes a àrea de navegação
    waiter.capacity(charge) #define a capacidade máxima da bateria do robo
    waiter.battery(charge) #define a bateria atual do robo
    
    #abre o ficheiro limpeza.txt e  guarda as coordenadas para uma lista chamda de localização
    arquivo2 = open("main/Limpeza.txt", "r")
    localizaçao = arquivo2.readlines()
    arquivo2.close()
    sujidades = []
    
    #variaveis que ditam o acontecimento dos diferentes loops
    goal = False
    pointchosen = False
    started = True
    
    #lista com os obstáculos
    group = []
    for g in [table,chair2,chair1, table2, plant]:
        group.append(g)
                
    while started:
     
      errormsg = True

      if pointchosen == False:
          
         if click:#se os pontos ainda não estiverem escolhidos e o utilizador tiver selecionado o click method esxecuta este loop
             
             p = win.getMouse()#recebe as coordenadas do clique do utilizador
             exitclicked(exitButton, p, win)
            
             if startbutton.clicked(p) and len(sujidades)>0:#se o utilizador clicar no start e houver mais de uma sujidade inicia o movimento
                 waiter.undraw()#apaga e desenha o robo e bateria para garantir que ficam por cima das sujidades
                 waiter.undrawbattery()
                 waiter.draw(win) 
                 waiter.drawbattery(win)
                 pointchosen = True
                 goal=True
                 continue
             
             if startbutton.clicked(p) and len(sujidades)==0:#assegura se ao clicar no start sem haver sujidades não desenha uma em cima do botão  
                 continue
                
             while invalidlocal(group, p, wradius, width/7.5, height/7.5 ):#se o clique introduzido não for válido desenha a mensagem de erro
                 if errormsg == True:
                     errorbox.draw(win)
                     errortext.draw(win)
                 p = win.getMouse()
                 errormsg = False
                 
             #caso passe por todas as condições anteriores utiliza o clique como coordenadas para a sujidade e adiciona-a a uma lista       
             sujidades.append(Mess(p,4))
             sujidades[len(sujidades)-1].draw(win)
             errorbox.undraw()#apaga a mensagem de erro se tiver desenhada
             errortext.undraw()     
      
             
         if file:#se os pontos ainda não estiverem escolhidos e o utilizador tiver selecionado o file method esxecuta este loop
             p = win.getMouse()
             exitclicked(exitButton, p, win)

             if startbutton.clicked(p):#Quando o utilizador clicar no start desenha as sujidades e adiciona-as a uma lista
                 for line in range(len(localizaçao) - 1):#loop que retira as coordenadas das sujidades da lista localizações
                     dirt = Point(eval(localizaçao[line + 1].split("-")[0]),eval(localizaçao[line + 1].split("-")[1]))
                     sujidades.append(Mess(dirt,4))#adiciona as sujidades à lista
                
                 a = len(sujidades)#conta quantidade de sujidades que há no ficheiro
                 for i in range(a):#loop que é executado até serem desenhadas todas as sujidades
                     sujidades[i].draw(win)
                 
                 #Apaga e desenha o robo para assegurar que ele fica em cima das sujidades
                 waiter.undraw()
                 waiter.undrawbattery()
                 waiter.draw(win)
                 waiter.drawbattery(win)
                 
                 pointchosen = True# alteraçao das variaveis para mudar de loop
                 goal=True
                 continue
             
  

      if pointchosen == True:
          
          gocharge(dock1,dock2,waiter,speed,charge,waiter.getY(),0.2)
          
          while goal == True:
          #Estes ciclos abaixo são identicos aos da  segunda implementação com a excepçao de que os valores são diferente pois a janela tamém o é  
              
            if abs(waiter.getX()-5)<=1 and abs(waiter.getY()-5)<=1 and goal == True:
                
                for i in range(4): 
                        while waiter.getX() < 95:
                            for g in group:
                                if (g.xmin - 0.2 < waiter.getX() < g.xmin  or g.xmax + 0.2 > waiter.getX() > g.xmax ) and \
                                        g.ymin <= waiter.getY() <= g.ymax:
                                    if g.ymax - waiter.getY() < waiter.getY()- g.ymin:
                                        dx, dy = 0, 0.2
                                    elif g.ymax - waiter.getY() > waiter.getY()- g.ymin:
                                        dx, dy = 0, -0.2
             
                                while table.cont(waiter.getX(), waiter.getY()) or chair2.cont(waiter.getX(), waiter.getY()) or chair1.cont(waiter.getX(), waiter.getY()) \
                                    or table2.cont(waiter.getX(), waiter.getY()) or plant.cont(waiter.getX(), waiter.getY()):
                                    waiter.move(dx, dy)
                                
                                
                            for g in group:
                                if( g.xmax + 0.6 > waiter.getX() > g.xmax ) and (g.ymin > waiter.getY() > g.ymin - 1.2 ):
                                    while waiter.getY() < 5 + (11.25 * ((i-1) * 2 + 2)):
                                          waiter.move(0,0.2)
                                if( g.xmax + 0.3 > waiter.getX() > g.xmax ) and(g.ymax + 1.2 > waiter.getY() > g.ymax):
                                    while waiter.getY() > 5 + (11.25 * ((i-1) * 2 + 2)):
                                          waiter.move(0,-0.2)
                                          
                            searchmess(sujidades, waiter, 5 + (11.25 * ((i-1) * 2 + 2)), 5.625 , wradius , group, 600, 0.2)
                  
                            waiter.move(0.2, 0)
                            update(600)
                            
                        while waiter.getY() <= 5 + (11.25 * (i * 2 + 1)):
                            waiter.move(0, 0.2)
                            update(600)
                            
                        gocharge(dock1,dock2,waiter,100,charge,5 + (11.25 * (i * 2 + 1)),0.2)
                
                        while waiter.getX() > 5:
                            for g in group:
                                if (g.xmin - 0.2 < waiter.getX() < g.xmin  or g.xmax + 0.2 > waiter.getX() > g.xmax ) and \
                                        g.ymin <= waiter.getY() <= g.ymax:
                                    if g.ymax - waiter.getY() < waiter.getY()- g.ymin:
                                        dx, dy = 0, 0.2
                                    elif g.ymax - waiter.getY() > waiter.getY()- g.ymin:
                                        dx, dy = 0, -0.2
        
                        
                                while  table.cont(waiter.getX(), waiter.getY()) or chair2.cont(waiter.getX(), waiter.getY()) or chair1.cont(waiter.getX(), waiter.getY()) \
                                    or table2.cont(waiter.getX(), waiter.getY()) or plant.cont(waiter.getX(), waiter.getY()):
                                    waiter.move(dx, dy)
                                
                            for g in group:                       
                                if( g.xmin  > waiter.getX() > g.xmin - 0.6 ) and (g.ymin > waiter.getY() > g.ymin - 1.2 ):
                                     while waiter.getY() < 5 + (11.25 * (i * 2 + 1)):
                                       waiter.move(0,0.2)

                                if( g.xmin > waiter.getX() > g.xmin - 0.6 ) and (g.ymax + 1 > waiter.getY() > g.ymax -1.2):
                                     while waiter.getY() > 5 + (11.25 * (i * 2 + 1)):
                                       waiter.move(0,-0.2)

                                       
                            searchmess(sujidades, waiter, 5 + (11.25 * (i * 2 + 1)), 5.625 , wradius, group, 600, 0.2)
                                       
                            waiter.move(-0.2, 0)
                            update(600)
                            
                        while waiter.getY() <= 5 + 11.25 * (i * 2 + 2):
                            searchmess(sujidades, waiter, 95, 5.625 , wradius, group, 600, 0.2)
                            waiter.move(0, 0.2)
                            update(600)
                        
                        gocharge(dock1,dock2,waiter,speed,charge,5 + 11.25 * (i * 2 + 2),0.2)
                                            
                while waiter.getX() < 95:
                        waiter.move(0.2, 0)
                        update(600)
                        
                if abs(waiter.getX() - 95) <= 1 and abs(waiter.getY() - 95) <= 1:
                        sujidades = []
                        goal = False
                        pointchosen = False

########################################################################################################################################################################
            
                       
            if abs(waiter.getX() - 95) <= 1 and abs(waiter.getY() - 95) <= 1 and goal == True:
                
                for i in range(4):

                    while waiter.getX() > 5:
                        for g in group:
                            if (g.xmin - 0.2 < waiter.getX() < g.xmin  or g.xmax + 0.2 > waiter.getX() > g.xmax) and \
                                        g.ymin <= waiter.getY() <= g.ymax:
                                if g.ymax - waiter.getY() < waiter.getY()- g.ymin:
                                        dx, dy = 0, 0.2
                                elif g.ymax - waiter.getY() > waiter.getY()- g.ymin:
                                        dx, dy = 0, -0.2
        
                        
                        while  table.cont(waiter.getX(), waiter.getY()) or chair2.cont(waiter.getX(), waiter.getY()) or chair1.cont(waiter.getX(), waiter.getY()) \
                        or table2.cont(waiter.getX(), waiter.getY()) or plant.cont(waiter.getX(), waiter.getY()):
                            waiter.move(dx, dy)
                                
                        for g in group:                       
                            if( g.xmin > waiter.getX() > g.xmin - 0.2 ) and (g.ymin > waiter.getY() > g.ymin - 0.2 ):
                                while waiter.getY() < 95 - (11.25 * ((i-1) * 2 + 2)):
                                      waiter.move(0,0.2)                                      
                            if( g.xmin > waiter.getX() > g.xmin - 4 ) and (g.ymax + 4 > waiter.getY() > g.ymax ):
                                while waiter.getY() > 95 - (11.25 * ((i-1) * 2 + 2)):
                                       waiter.move(0,-0.2)
                            
                            searchmess(sujidades, waiter, 95 - (11.25 * ((i-1) * 2 + 2)), 5.625 , wradius, group, 600, 0.2)
                            
                            waiter.move(-0.2, 0)
                            update(600)
                            
                    gocharge(dock1, dock2, waiter, speed, charge, 95 - (11.25 * (i * 2 + 1)),0.2)   
                            
                    while waiter.getY() > 95 - (11.25 * (i * 2 + 1)):
                        waiter.move(0, -0.2)
                        update(600)
                                
                    while waiter.getX() < 95:
                        
                        for g in group:
                                if (g.xmin - 0.2 < waiter.getX() < g.xmin or g.xmax + 0.2 > waiter.getX() > g.xmax) and \
                                        g.ymin <= waiter.getY() <= g.ymax:
                                    if g.ymax - waiter.getY() < waiter.getY()- g.ymin:
                                        dx, dy = 0, 0.2
                                    elif g.ymax - waiter.getY() > waiter.getY()- g.ymin:
                                        dx, dy = 0, -0.2
             
                        while  table.cont(waiter.getX(), waiter.getY()) or chair2.cont(waiter.getX(), waiter.getY()) or chair1.cont(waiter.getX(), waiter.getY()) \
                                or table2.cont(waiter.getX(), waiter.getY()) or plant.cont(waiter.getX(), waiter.getY()):
                                waiter.move(dx, dy)
                                
                        for g in group:
                                if( g.xmax + 0.2 > waiter.getX() > g.xmax ) and (g.ymin > waiter.getY() > g.ymin - 0.2 ):
                                    while waiter.getY() < 95 - (11.25 * (i * 2 + 1)):
                                          waiter.move(0,0.2)
                                if( g.xmax + 3 > waiter.getX() > g.xmax ) and(g.ymax + 3 > waiter.getY() > g.ymax ):
                                    while waiter.getY() > 95 - (11.25 * (i * 2 + 1)):
                                          waiter.move(0,-0.2)
                            
                        searchmess(sujidades, waiter, 95 - (11.25 * (i * 2 + 1)), 5.625 , wradius, group, 600, 0.2)
                            
                        waiter.move(0.2, 0) 
                        
                    gocharge(dock1,dock2,waiter,speed,charge, 95 - (11.25 * (i * 2 + 2)),0.2)      
                        
                    while waiter.getY() >= 95 - (11.25 * (i * 2 + 2)):
                            waiter.move(0, -0.2)
                                        
                        
                while waiter.getX() > 5:
                      searchmess(sujidades, waiter, 5, 5.625 , wradius, group, 600, 0.2)
                      waiter.move(-0.2, 0)
                      update(600)
                    
                if abs(waiter.getX() - 5) <= 1 and abs(waiter.getY() - 5) <= 1:
                      sujidades = []
                      goal = False
                      pointchosen = False

def Aleatger(click,file):
#Nesta as coordenadas dos obstáculos são aleatórias

        width = 1000  # Largura da janela
        height = 600  # Altura da janela
        buttonwidth = 70 # Largura dos botões
        buttonheight = 35 # Altura dos botões
        speed = 600 # Numero que será introduzido nos updates para o movimento
        
        #Definição da janela
        win = GraphWin("Projeto", width, height)
        win.setBackground(color_rgb(223, 209, 196))
        win.setCoords(0, 0, 1000, 600) 

        #Definição das docks
        dock1 = Dock(Point(37.5, 37.5), 75, 75)
        dock2 = Dock(Point(1000-37.5, 600-37.5), 75, 75)
        docks = [dock1.getXY(), dock2.getXY()]
        dock1.draw(win)
        dock2.draw(win)

        #definição da robo
        wradius = 35
        waiter = Waiter(Point(37.5, 37.5), wradius , win)

        #definição da mensagem de erro
        errorbox = Rectangle(Point(width/2 - width/10,0), Point(width/2 + width/10,50))
        errorbox.setWidth(4)
        errorbox.setFill("Red")
        errorbox.setOutline("White")
        errortext = Text(Point(width/2, 25), "Invalid point, try again")
        errortext.setFill("White")
        
        #define o botão que inicia o movimento
        startbutton = Button(win, Point(width - buttonwidth/2 - 10, 3 * (buttonheight/2) + 10*2) , buttonwidth, buttonheight, "Start", color_rgb(160,197,145))
        startbutton.activate()
        
        #define o botão caso o utilizador queira gerar obstaculos com outras coordenadas
        refreshbutton = Button(win, Point(width - buttonwidth/2 - 10, 5 * (buttonheight/2) + 10*3) , buttonwidth, buttonheight, "Refresh", color_rgb(217,197,224))
        refreshbutton.activate()
        
        #gera uma lista com as coordenadas dos obstáculos
        obstaculos = aleatpoint(win, wradius, width, height, buttonwidth, buttonheight)
        
        for forma in obstaculos:
            forma.draw(win)
            
        #define o botão para voltar ao menu    
        exitButton = exitbutton(win, Point(width - buttonwidth/2 - 10, buttonheight/2 + 10), buttonwidth,buttonheight )    

        #abre o ficheiro limpeza.txt e  guarda as coordenadas para uma lista chamda de localização
        arquivo2 = open("Limpeza.txt", "r")
        localizaçao = arquivo2.readlines()
        arquivo2.close()
        sujidades = []
        
        #define e desenha o robo
        waiter.draw(win)
        waiter.drawbattery(win)
        charge = (1000*7 + 600)*2
        waiter.capacity(charge)
        waiter.battery(charge)
        
        #variaveis  que ditam o acontecimento dos diferentes loops
        goal = False
        pointchosen = False
        started = True
        group = []
        for g in [forma]:
            group.append(g)
            
        while started:
         
          errormsg = True

          if pointchosen == False:
              
             p = win.getMouse()
             if refreshbutton.clicked(p) and len(sujidades)==0:#se o botao refresh tiver sido clicadoe não houver sujidades gera novos obstáculos
                  for forma in obstaculos:
                      forma.undraw()
                  
                  obstaculos = aleatpoint(win, wradius, width, height, buttonwidth, buttonheight)
                  for forma in obstaculos:
                      forma.draw(win) 
                      
                  continue
              
             if click:#se for selecionado o método de clicar 
                 
                 exitclicked(exitButton, p, win)
                
                 if startbutton.clicked(p) and len(sujidades)>0:
                       waiter.undraw()
                       waiter.undrawbattery()
                       waiter.draw(win)
                       waiter.drawbattery(win)
                       pointchosen = True
                       goal=True
                       continue
                    
                 while invalidlocal(obstaculos, p, wradius, width, height ):
                        if errormsg == True:
                            errorbox.draw(win)
                            errortext.draw(win)
                        p = win.getMouse()
                        errormsg = False
                        
                 sujidades.append(Mess(p,30))
                 sujidades[len(sujidades)-1].draw(win)
                 errorbox.undraw()
                 errortext.undraw()     
          
                 
             if file:#se for selecionado o método que vai buscar as sujidades ao ficheiro
                 exitclicked(exitButton, p, win)
                 
                 if startbutton.clicked(p):
                     waiter.undraw()
                     waiter.undrawbattery()
                     for line in range(len(localizaçao) - 2):
                         dirt = Point(eval(localizaçao[line + 1].split("-")[2]),eval(localizaçao[line + 1].split("-")[3]))
                         sujidades.append(Mess(dirt,30))
                         sujidades[line].draw(win)
                     waiter.draw(win)
                     waiter.drawbattery(win)
                     pointchosen = True
                     goal=True
                     continue
                 

          if pointchosen == True:#inicia-se o loop do movimento
              
              gocharge(dock1,dock2,waiter,speed,charge,waiter.getY(),1)#caso não tenha bateria carrega
              
              while goal == True:
                #movimento quando o robo começa na dock de baixo e acaba na de cima
                if abs(waiter.getX()-37.5)<=1 and abs(waiter.getY()-37.5)<=1 and goal == True:#verifica as coordenadas do robo     
                
                    for i in range(3):#executa este loop 3 vezes e usa o i para fazer o calculo do y em que o robo deverá estar em cada ciclo                     
                        while waiter.getX() <= 962.5:#movimento para a direita
                        
                            for g in obstaculos:#condições que ditam o movimento quando o robo entra em contacto com um dos objetos
                            
                                if (g.xmin - 3 < waiter.getX() < g.xmin or g.xmax + 3 > waiter.getX() > g.xmax) and \
                                    g.ymin <= waiter.getY() <= g.ymax:
                                    if g.ymax - waiter.getY() < waiter.getY()- g.ymin:
                                            dx, dy = 0, 1
                                    elif g.ymax - waiter.getY() > waiter.getY()- g.ymin:
                                            dx, dy = 0, -1
                 
                            while obstaculos[0].cont(waiter.getX(), waiter.getY()) or obstaculos[1].cont(waiter.getX(), waiter.getY()) or obstaculos[2].cont(waiter.getX(), waiter.getY()) \
                                or obstaculos[3].cont(waiter.getX(), waiter.getY()) or obstaculos[4].cont(waiter.getX(), waiter.getY()):
                                    waiter.move(dx, dy)#se entrar em contacto segue as condições ditadas antes
                                    
                            #volta para o trajeto ao fim de se desviar dos obstáculos        
                            for g in obstaculos:
                                if( g.xmax + 5 > waiter.getX() > g.xmax  ) and (g.ymin > waiter.getY() > g.ymin - 5 ):
                                    while waiter.getY() < 37.5 + (87.5 * ((i-1) * 2 + 2)):
                                        waiter.move(0,1)
                                        
                                if( g.xmax + 5 > waiter.getX() > g.xmax ) and(g.ymax + 5 > waiter.getY() > g.ymax):
                                    while waiter.getY() > 37.5 + (87.5 * ((i-1) * 2 + 2)):
                                        waiter.move(0,-1)

                            #executa a função que procura por sujidades                  
                            searchmess(sujidades, waiter, 37.5 + (87.5 * ((i-1) * 2 + 2)), 47.5 , wradius , obstaculos, 600, 1)
                      
                            waiter.move(1, 0)
                            update(600)
                                
                        while waiter.getY() <= 37.5 + (87.5 * (i * 2 + 1)):#anda para cima até atingir o y do trajeto de maneira limpar a sala toda
                            waiter.move(0, 1)
                            update(600)
                            
                        #executa a função que verifica se precisa de ir limpar        
                        gocharge(dock1,dock2,waiter,speed,charge,37.5 + (87.5 * (i * 2 + 1)),1)
                    
                        while waiter.getX() >= 37.5:#movimento para a esquerda
                            
                            for g in obstaculos:#condições que ditam o movimento quando o robo entra em contacto com um dos objetos
                                if (g.xmin - 3 < waiter.getX() < g.xmin  or g.xmax + 3 > waiter.getX() > g.xmax ) and \
                                    g.ymin <= waiter.getY() <= g.ymax:
                                    if g.ymax - waiter.getY() < waiter.getY()- g.ymin:
                                        dx, dy = 0, 1
                                    elif g.ymax - waiter.getY() > waiter.getY()- g.ymin:
                                        dx, dy = 0, -1        
                            
                            while  obstaculos[0].cont(waiter.getX(), waiter.getY()) or obstaculos[1].cont(waiter.getX(), waiter.getY()) or obstaculos[2].cont(waiter.getX(), waiter.getY()) \
                                or obstaculos[3].cont(waiter.getX(), waiter.getY()) or obstaculos[4].cont(waiter.getX(), waiter.getY()):
                                    waiter.move(dx, dy)#se entrar em contacto segue as condições ditadas antes
       
                            #volta para o trajeto ao fim de se desviar dos obstáculos          
                            for g in obstaculos:                       
                                    if( g.xmin  > waiter.getX() > g.xmin - 3 ) and (g.ymin > waiter.getY() > g.ymin - 3 ):
                                         while waiter.getY() < 37.5 + (87.5 * (i * 2 + 1)):
                                           waiter.move(0,1)

                                    if( g.xmin > waiter.getX() > g.xmin - 3 ) and (g.ymax + 3 > waiter.getY() > g.ymax):
                                         while waiter.getY() > 37.5 + (87.5 * (i * 2 + 1)):
                                           waiter.move(0,-1)

                            #executa a função que procura por sujidades               
                            searchmess(sujidades, waiter, 37.5 + (87.5 * (i * 2 + 1)), 47.5 , wradius, obstaculos, 600, 1)#
                                           
                            waiter.move(-1, 0)
                            update(600)
                                
                        while waiter.getY() <= 37.5 + 87.5 * (i * 2 + 2):#anda para cima até atingir o y do trajeto de maneira limpar a sala toda
                            waiter.move(0, 1)
                            update(600)
                            
                        #executa a função que verifica se precisa de ir limpar    
                        gocharge(dock1,dock2,waiter,speed,charge,37.5 + 87.5 * (i * 2 + 2),1)
                                                
                    while waiter.getX() <= 962.5:#anda para a direita até atingir a dock de cima, verificando se não sujidades
                            searchmess(sujidades, waiter, 562.5, 47.5 , wradius, obstaculos, 600, 1)                  
                            waiter.move(1, 0)
                            update(600)
                            
                            
                    if abs(waiter.getX() - 962.5) <= 1 and abs(waiter.getY() - 562.5) <= 1:#verifica as coordenadas do robo quando até ser atingida a dock de cima
                            sujidades = [] #esvazia a lista das sujidades
                            goal = False #muda as variaveis de maneira a sair do loop do movimento
                            pointchosen = False

    ########################################################################################################################################################################
                
                #movimento oposto ao anterior, quando o robo começa na dock de cima e acaba na de baixo                  
                if abs(waiter.getX() - 962.5) <= 1 and abs(waiter.getY() - 562.5) <= 1 and goal == True: #verifica as coordenadas do robo
                
                    for i in range(3):#executa este loop 3 vezes e usa o i para fazer o calculo do y em que o robo deverá estar em cada ciclo 
                        
                        while waiter.getX() >= 37.5:#movimento para a esquerda
                            for g in obstaculos:#condições que ditam o movimento quando o robo entra em contacto com um dos objetos
                                if (g.xmin - 3 < waiter.getX() < g.xmin  or g.xmax + 3 > waiter.getX() > g.xmax) and \
                                            g.ymin <= waiter.getY() <= g.ymax:
                                    if g.ymax - waiter.getY() < waiter.getY()- g.ymin:
                                            dx, dy = 0, 1
                                    elif g.ymax - waiter.getY() > waiter.getY()- g.ymin:
                                            dx, dy = 0, -1
            
                            
                            while  obstaculos[0].cont(waiter.getX(), waiter.getY()) or obstaculos[1].cont(waiter.getX(), waiter.getY()) or obstaculos[2].cont(waiter.getX(), waiter.getY()) \
                                or obstaculos[3].cont(waiter.getX(), waiter.getY()) or obstaculos[4].cont(waiter.getX(), waiter.getY()):
                                waiter.move(dx, dy)#se entrar em contacto segue as condições ditadas antes
                                
                            #volta para o trajeto ao fim de se desviar dos obstáculos        
                            for g in obstaculos:                       
                                if( g.xmin > waiter.getX() > g.xmin - 4 ) and (g.ymin > waiter.getY() > g.ymin - 4 ):
                                    while waiter.getY() < 562.5 - (87.5 * ((i-1) * 2 + 2)):
                                        waiter.move(0,1)
                                if( g.xmin > waiter.getX() > g.xmin - 4 ) and (g.ymax + 4 > waiter.getY() > g.ymax ):
                                    while waiter.getY() > 562.5 - (87.5 * ((i-1) * 2 + 2)):
                                        waiter.move(0,-1)
                            
                            #executa a função que procura por sujidades     
                            searchmess(sujidades, waiter, 562.5 - (87.5 * ((i-1) * 2 + 2)), 47.5 , wradius, obstaculos, 600, 1)
                                
                            waiter.move(-1, 0)
                            update(600)
                            
                        #executa a função que verifica se precisa de ir limpar           
                        gocharge(dock1,dock2,waiter,speed,charge,562.5 - (87.5 * (i * 2 + 1)),1)   
                                
                        while waiter.getY() >= 562.5 - (87.5 * (i * 2 + 1)):#anda para baixo até atingir o y do trajeto de maneira limpar a sala toda
                            waiter.move(0, -1)
                            update(600)
                                    
                        while waiter.getX() <= 962.5:#movimento para a direita
                        
                                for g in obstaculos:#condições que ditam o movimento quando o robo entra em contacto com um dos objetos
                                    if (g.xmin - 3 < waiter.getX() < g.xmin or g.xmax + 3 > waiter.getX() > g.xmax) and \
                                            g.ymin <= waiter.getY() <= g.ymax:
                                        if g.ymax - waiter.getY() < waiter.getY()- g.ymin:
                                            dx, dy = 0, 1
                                        elif g.ymax - waiter.getY() > waiter.getY()- g.ymin:
                                            dx, dy = 0, -1
                 
                                while  obstaculos[0].cont(waiter.getX(), waiter.getY()) or obstaculos[1].cont(waiter.getX(), waiter.getY()) or obstaculos[2].cont(waiter.getX(), waiter.getY()) \
                                    or obstaculos[3].cont(waiter.getX(), waiter.getY()) or obstaculos[4].cont(waiter.getX(), waiter.getY()):
                                    waiter.move(dx, dy)#se entrar em contacto segue as condições ditadas antes
                                
                                #volta para o trajeto ao fim de se desviar dos obstáculos     
                                for g in obstaculos:
                                    if( g.xmax + 3 > waiter.getX() > g.xmax ) and (g.ymin > waiter.getY() > g.ymin - 3 ):
                                        while waiter.getY() < 562.5 - (87.5 * (i * 2 + 1)):
                                              waiter.move(0,1)
                                    if( g.xmax + 3 > waiter.getX() > g.xmax ) and(g.ymax + 3 > waiter.getY() > g.ymax ):
                                        while waiter.getY() > 562.5 - (87.5 * (i * 2 + 1)):
                                              waiter.move(0,-1)
                                
                                #executa a função que procura por sujidades 
                                searchmess(sujidades, waiter, 562.5 - (87.5 * (i * 2 + 1)), 47.5 , wradius, obstaculos, 600, 1)
                                
                                waiter.move(1, 0) 
                                                    
                        #executa a função que verifica se precisa de ir limpar    
                        gocharge(dock1,dock2,waiter,speed,charge, 562.5 - (87.5 * (i * 2 + 2)),1)      
                            
                        while waiter.getY() >= 562.5 - (87.5 * (i * 2 + 2)):
                                waiter.move(0, -1)
                                            
                            
                    while waiter.getX() >= 37.5:#anda para a esquerda até atingir a dock de baixo
                    
                          searchmess(sujidades, waiter, 37.5, 47.5 , wradius, obstaculos, 600, 1)  
                          waiter.move(-1, 0)
                          update(600)
                        
                    if abs(waiter.getX() - 37.5) <= 1 and abs(waiter.getY() - 37.5) <= 1:#verifica as coordenadas do robo quando até ser atingida a dock de baixo
                          sujidades = [] #esvazia a lista das sujidades
                          goal = False #muda as variaveis de maneira a sair do loop do movimento
                          pointchosen = False
    
def main():
    
    menu()

main()