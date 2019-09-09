import pygame
from Proyectil import Proyectil

class naveEspacial(pygame.sprite.Sprite):
    "Clase para las naves"

    def __init__(self,ancho,alto):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenNave = pygame.image.load("Codigo Python/Space invaders xd/imagenes/nave.jpg")
        self.ImagenExplosion = pygame.image.load("Codigo Python/Space invaders xd/imagenes/explosion.jpg")
        self.rect = self.ImagenNave.get_rect()
        self.rect.centerx=ancho/2
        self.rect.centery=alto-30

        self.listaDisparo=([])
        self.Vida=True

        self.Velocidad=20

        self.sonidoDisparo=pygame.mixer.Sound("/media/gmatias89/D/Code/Codigo Python/Space invaders xd/Piu.ogg")
        self.sonidoExplosion=pygame.mixer.Sound("/media/gmatias89/D/Code/Codigo Python/Space invaders xd/pum.ogg")

    def movimientoDerecha(self):
        self.rect.right += self.Velocidad
        self.__movimiento()
    
    def movimientoIzquierda(self):
        self.rect.left -= self.Velocidad
        self.__movimiento()


    def __movimiento(self):
        if self.Vida==True:
            if self.rect.left<=0:
                self.rect.left =0
            elif self.rect.right>870:
                self.rect.right = 840

    def disparar(self,x,y):
        miProyectil = Proyectil(x,y,"Codigo Python/Space invaders xd/imagenes/disparoa.jpg",True)
        self.listaDisparo.append(miProyectil)
        self.sonidoDisparo.play()

    def destruccion(self):
        self.sonidoExplosion.play()
        self.Vida=False
        self.velocidad=0
        self.ImagenNave=self.ImagenExplosion

    def dibujar(self,superficie):
        superficie.blit(self.ImagenNave,self.rect)