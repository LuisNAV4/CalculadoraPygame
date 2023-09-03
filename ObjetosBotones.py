import pygame

class Botones:
    def __init__(self,x,y,width,height,Num):
        self.rect = pygame.Rect(x,y,width,height)
        self.dimesionesImagen = (width-10,height-10)
        self.color_normal = (200,200,200)
        self.color_presionado = (100,100,100)
        self.Texto = Num
        self.Font = pygame.font.SysFont("arial",26)
        self.presionado = False
        
    def Dibujar(self,screen):
        Color = self.color_presionado if self.presionado else self.color_normal
        pygame.draw.rect (screen,Color,self.rect)
        
        Texto_Render = self.Font.render(self.Texto, True, (0,0,0))
        Texto_Rect = Texto_Render.get_rect(center= self.rect.center)
        screen.blit(Texto_Render,Texto_Rect)
        
    def Click(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.presionado = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.presionado = False
            
            
    def DibujarIcono(self,screen,icono):
        Color = self.color_presionado if self.presionado else self.color_normal
        Icono = pygame.image.load(icono)
        Icono = pygame.transform.scale(Icono,(self.dimesionesImagen))
        CentrarImagen = Icono.get_rect(center= self.rect.center)
        pygame.draw.rect (screen,Color,self.rect)
        screen.blit(Icono,CentrarImagen)
            
class Pantalla:
    def __init__(self,Calculo):
        self.rect = pygame.Rect(0,0,330,140)
        self.Texto = Calculo
        self.font = pygame.font.SysFont("arial",24) 
        self.ColorFondo = pygame.Color("#9b9b9b")
        
    def Dibujar(self,screen,Desplazamiento):
        pygame.draw.rect(screen, self.ColorFondo, self.rect)
        
        TextoRender = self.font.render(self.Texto, True, (0,0,0))
        TextoRect = TextoRender.get_rect(center= self.rect.center)
        TextoRect.move_ip (Desplazamiento)
        screen.blit(TextoRender,TextoRect)
        
class Label:
    def __init__(self,x,y,Texto):
        self.Texto = Texto
        self.posicion = (x,y)
        self.font = pygame.font.SysFont("arial",24)
        
    def Dibujar(self,screen):
        textorender = self.font.render(self.Texto,True,(0,0,0))
        screen.blit(textorender,self.posicion)
        
        