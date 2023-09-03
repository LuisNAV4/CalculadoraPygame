import pygame 
import os
import math
from ObjetosBotones import *

def DibujoBotones():
    Num1.Dibujar(screen)
    Num2.Dibujar(screen)
    Num3.Dibujar(screen)
    Num4.Dibujar(screen)
    Num5.Dibujar(screen)
    Num6.Dibujar(screen)
    Num7.Dibujar(screen)
    Num8.Dibujar(screen)
    Num9.Dibujar(screen)
    Num0.Dibujar(screen)
    BotonMAS.Dibujar(screen)
    BotonMENOS.Dibujar(screen)
    BotomMULTIPLICAR.Dibujar(screen)
    BotonDIVIDIR.Dibujar(screen)
    BotonIGUALDAD.Dibujar(screen)
    BotonBorrar.DibujarIcono(screen,iconoBorrar)
    BotonPUNTO.Dibujar(screen)
    BotonBorrarTODO.Dibujar(screen)
    BotonParentecisAbierto.Dibujar(screen)
    BotonParentecisCerrado.Dibujar(screen)
    BotonElevado.Dibujar(screen)
    BotonRaiz.DibujarIcono(screen,iconoRaiz)
    
    
    CalculadoraValores.Dibujar(screen,(0,-20))
    CalculadoraResultados.Dibujar(screen)



def AccionBotones():
    Num1.Click(event)
    Num2.Click(event)
    Num3.Click(event)
    Num4.Click(event)
    Num5.Click(event)
    Num6.Click(event)
    Num7.Click(event)
    Num8.Click(event)
    Num9.Click(event)
    Num0.Click(event)
    BotonMAS.Click(event)
    BotonMENOS.Click(event)
    BotomMULTIPLICAR.Click(event)
    BotonDIVIDIR.Click(event)
    BotonIGUALDAD.Click(event)
    BotonBorrar.Click(event)
    BotonPUNTO.Click(event)
    BotonBorrarTODO.Click(event)
    BotonParentecisAbierto.Click(event)
    BotonParentecisCerrado.Click(event)
    BotonElevado.Click(event)
    BotonRaiz.Click(event)
    
def ClickBotonesAccion():
    if Num1.presionado:
        ListaNumerica.append("1")
        CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
        
    if Num2.presionado:
        ListaNumerica.append("2")
        CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
        
    if Num3.presionado:
        ListaNumerica.append("3")
        CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
        
    if Num4.presionado:
        ListaNumerica.append("4")
        CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
        
    if Num5.presionado:
        ListaNumerica.append("5")
        CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
        
    if Num6.presionado:
        ListaNumerica.append("6")
        CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
        
    if Num7.presionado:
        ListaNumerica.append("7")
        CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
        
    if Num8.presionado:
        ListaNumerica.append("8")
        CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)

    if Num9.presionado:
        ListaNumerica.append("9")
        CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
        
    if Num0.presionado:
        ListaNumerica.append("0")
        CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
        
    if BotonMAS.presionado:
        ListaNumerica.append("+")
        CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
     
    if BotonMENOS.presionado:
        ListaNumerica.append("-")
        CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
    
    if BotomMULTIPLICAR.presionado:
        ListaNumerica.append("*")
        CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
    
    if BotonDIVIDIR.presionado:
        ListaNumerica.append("/")
        CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
    
    if BotonIGUALDAD.presionado:
        CalculadoraResultados.Texto = CalculoCadena(ListaNumerica)
    
    if BotonPUNTO.presionado:
        num = len(ListaNumerica) - 1
        if ListaNumerica[num] != ".":
            ListaNumerica.append(".")
            CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
    
    if BotonBorrar.presionado:
        if len(ListaNumerica) != 0:
            ListaNumerica.pop()
            CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)

            
    if BotonBorrarTODO.presionado:
        ListaNumerica.clear()
        CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
        CalculadoraResultados.Texto = ""
        
    if BotonParentecisAbierto.presionado:
        Bandera = False
        if len(ListaNumerica) != 0:
            num = len(ListaNumerica) - 1
            try:
                num = int(ListaNumerica[num])
                Bandera = True
            except:
                if ListaNumerica[num] == ")" or ListaNumerica[num] == "(":
                    Bandera = True
                    
                if ListaNumerica[num] == ".":
                    return
                
        if Bandera:
            ListaNumerica.append("*")
            
        ListaNumerica.append("(")
        CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
        
    if BotonParentecisCerrado.presionado:
        num = len(ListaNumerica) - 1
        if ListaNumerica[num] == ".":
            return
        
        ListaNumerica.append(")")
        CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
        
    if BotonRaiz.presionado:
        ListaNumerica.append("sqrt")
        ListaNumerica.append("(")
        CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
        
    if BotonElevado.presionado:
        ListaNumerica.append("**")
        CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
        

        
def BotonesPresionado():
    if event.key == pygame.K_KP1 or event.key == pygame.K_1:
        ListaNumerica.append("1")
        CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
        
    if event.key == pygame.K_KP2 or event.key == pygame.K_2:
        ListaNumerica.append("2")
        CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
        
    if event.key == pygame.K_KP3 or event.key == pygame.K_3:
        ListaNumerica.append("3")
        CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
        
    if event.key == pygame.K_KP4 or event.key == pygame.K_4:
        ListaNumerica.append("4")
        CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
        
    if event.key == pygame.K_KP5 or event.key == pygame.K_5:
        ListaNumerica.append("5")
        CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
        
    if event.key == pygame.K_KP6 or event.key == pygame.K_6:
        ListaNumerica.append("6")
        CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
        
    if event.key == pygame.K_KP7 or event.key == pygame.K_7:
        ListaNumerica.append("7")
        CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
        
    if event.key == pygame.K_KP8 or event.key == pygame.K_8:
        ListaNumerica.append("8")
        CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)

    if event.key == pygame.K_KP9 or event.key == pygame.K_9:
        ListaNumerica.append("9")
        CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
        
    if event.key == pygame.K_KP0 or event.key == pygame.K_0:
        ListaNumerica.append("0")
        CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
        
    if event.key == pygame.K_KP_PLUS:
        ListaNumerica.append("+")
        CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
     
    if event.key == pygame.K_KP_MINUS:
        ListaNumerica.append("-")
        CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
    
    if event.key == pygame.K_KP_MULTIPLY:
        ListaNumerica.append("*")
        CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
    
    if event.key == pygame.K_KP_DIVIDE:
        ListaNumerica.append("/")
        CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
    
    if event.key == pygame.K_KP_ENTER:
        CalculadoraResultados.Texto = CalculoCadena(ListaNumerica)
    
    if event.key == pygame.K_KP_PERIOD:
        num = len(ListaNumerica) - 1
        if ListaNumerica[num] != ".":
            ListaNumerica.append(".")
            CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
    
    if event.key == pygame.K_BACKSPACE:
        if len(ListaNumerica) != 0:
            ListaNumerica.pop()
            CalculadoraValores.Texto = ActualizarPantallaCalculadora(ListaNumerica)
            


def CalculoCadena(Lista):
    Resultado = 0
    Ecuacion = ""
    try:
        for i in Lista:
            Ecuacion += i
            
        if 'sqrt' in Ecuacion:
            Ecuacion = Ecuacion.replace('sqrt', 'math.sqrt')
                      
        Resultado = eval(Ecuacion)
        print(f"Resultado: {Resultado}")
        TextoCalculadora = f"={Resultado}"
        return TextoCalculadora
        
    except:
        TextoCalculadora = "Syntax Error"
        return TextoCalculadora
            
        
def ActualizarPantallaCalculadora(Lista):
    TextoTransformado = ""
    for i in Lista:
        TextoTransformado += i
    
    return TextoTransformado


pygame.init()
screen = pygame.display.set_mode((330,460))
pygame.display.set_caption("Calculadora")
Icon = pygame.image.load("Icono/Icon.png")
pygame.display.set_icon(Icon)
running = True
clock = pygame.time.Clock()
FPS = 30

Y = 40

#Diseño Botones
Num1 = Botones(20,370 - Y,50,50,"1") 
Num2 = Botones(80,370 - Y,50,50,"2")
Num3 = Botones(140,370 - Y,50,50,"3")
Num4 = Botones(20,310 - Y,50,50,"4")
Num5 = Botones(80,310 - Y,50,50,"5")
Num6 = Botones(140,310 - Y,50,50,"6")
Num7 = Botones(20,250 - Y,50,50,"7")
Num8 = Botones(80,250 - Y,50,50,"8")
Num9 = Botones(140,250 - Y,50,50,"9")
Num0 = Botones(20,430 - Y,110,50,"0")
BotonMAS = Botones(200,430 - Y,50,50,"+")
BotonMENOS = Botones(200,370 - Y,50,50,"-")
BotomMULTIPLICAR = Botones(200,310 - Y,50,50,"x")
BotonDIVIDIR = Botones(200,250 - Y,50,50,"/")
BotonIGUALDAD = Botones(260,310 - Y,50,170,"=")
BotonPUNTO = Botones(140,430 - Y,50,50,".")
BotonBorrar = Botones(260,250 - Y,50,50,"")
BotonBorrarTODO = Botones(260,190 - Y,50,50,"C")
BotonParentecisAbierto = Botones(80,190 - Y,50,50,"(")
BotonParentecisCerrado = Botones(140,190 - Y,50,50,")")
BotonElevado = Botones(200,190 - Y,50,50,"^") 
BotonRaiz = Botones (20,190 - Y,50,50,"")

iconoBorrar = "Icono/Borrar.png"
iconoRaiz = "Icono/Raiz.png"

CalculadoraValores = Pantalla("")
CalculadoraResultados= Label(30,80,"")

ListaNumerica = []

while running:
    screen.fill((255,255,255))
    DibujoBotones()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        AccionBotones()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            ClickBotonesAccion()
        
        if event.type == pygame.KEYDOWN:
            BotonesPresionado()
            

            
    pygame.display.flip()
    
    clock.tick(FPS)
    
os.system('CLS')
pygame.quit()