import pygame,sys
from pygame.locals import *
from random import randint
from Invasor import Invasor
from Nave import naveEspacial
from Proyectil import Proyectil
ancho = 900
alto = 480

listaEnemigo = ([])

def detenerTodo():
    for enemigo in listaEnemigo:
        for disparo in enemigo.listaDisparo:
            enemigo.listaDisparo.remove(disparo)

        enemigo.conquista=True

def cargarEnemigos():
    enemigo1 = Invasor(114,100,100, "Codigo Python/Space invaders xd/imagenes/marcianoA.jpg","Codigo Python/Space invaders xd/imagenes/MarcianoB.jpg")
    enemigo2 = Invasor(100,25,100, "Codigo Python/Space invaders xd/imagenes/Marciano2A.jpg","Codigo Python/Space invaders xd/imagenes/Marciano2B.jpg")
    enemigo3 = Invasor(200,100,100, "Codigo Python/Space invaders xd/imagenes/Marciano3A.jpg","Codigo Python/Space invaders xd/imagenes/Marciano3B.jpg")
    enemigo4 = Invasor(200,25,100, "Codigo Python/Space invaders xd/imagenes/Marciano2A.jpg","Codigo Python/Space invaders xd/imagenes/Marciano2B.jpg")
    enemigo5 = Invasor(314,100,100, "Codigo Python/Space invaders xd/imagenes/marcianoA.jpg","Codigo Python/Space invaders xd/imagenes/MarcianoB.jpg")
    enemigo6 = Invasor(300,25,100, "Codigo Python/Space invaders xd/imagenes/Marciano3A.jpg","Codigo Python/Space invaders xd/imagenes/Marciano3B.jpg")
    #6 izquierdos
    enemigo7 = Invasor(414,100,100, "Codigo Python/Space invaders xd/imagenes/marcianoA.jpg","Codigo Python/Space invaders xd/imagenes/MarcianoB.jpg")
    enemigo8 = Invasor(400,25,100, "Codigo Python/Space invaders xd/imagenes/Marciano2A.jpg","Codigo Python/Space invaders xd/imagenes/Marciano2B.jpg")
    enemigo9 = Invasor(500,100,100, "Codigo Python/Space invaders xd/imagenes/Marciano3A.jpg","Codigo Python/Space invaders xd/imagenes/Marciano3B.jpg")
    enemigo10 = Invasor(500,25,100, "Codigo Python/Space invaders xd/imagenes/Marciano2A.jpg","Codigo Python/Space invaders xd/imagenes/Marciano2B.jpg")
    enemigo11= Invasor(514,100,100, "Codigo Python/Space invaders xd/imagenes/marcianoA.jpg","Codigo Python/Space invaders xd/imagenes/MarcianoB.jpg")
    enemigo12 = Invasor(500,25,100, "Codigo Python/Space invaders xd/imagenes/Marciano3A.jpg","Codigo Python/Space invaders xd/imagenes/Marciano3B.jpg")
    enemigo13 = Invasor(600,100,100, "Codigo Python/Space invaders xd/imagenes/Marciano3A.jpg","Codigo Python/Space invaders xd/imagenes/Marciano3B.jpg")
    enemigo14 = Invasor(600,25,100, "Codigo Python/Space invaders xd/imagenes/Marciano2A.jpg","Codigo Python/Space invaders xd/imagenes/Marciano2B.jpg")
    
    listaEnemigo.append(enemigo1)
    listaEnemigo.append(enemigo2)
    listaEnemigo.append(enemigo3)
    listaEnemigo.append(enemigo4)
    listaEnemigo.append(enemigo5)
    listaEnemigo.append(enemigo6)
    listaEnemigo.append(enemigo7)
    listaEnemigo.append(enemigo8)
    listaEnemigo.append(enemigo9)
    listaEnemigo.append(enemigo10)
    listaEnemigo.append(enemigo11)
    listaEnemigo.append(enemigo12)
    listaEnemigo.append(enemigo13)
    listaEnemigo.append(enemigo14)


def SpaceInvader():
    pygame.init()
    pygame.mixer.init()

    ventana = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Space-Invaders-trucho")
    ventana.fill((0,0,0))
    ImagenFondo = pygame.image.load("Codigo Python/Space invaders xd/imagenes/Fondo.jpg")

    pygame.mixer.music.load("Codigo Python/Space invaders xd/intro.mp3")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(3)
    sonidoExplosion=pygame.mixer.Sound("Codigo Python/Space invaders xd/puff.ogg")
    miFuenteSistema = pygame.font.SysFont("Arial",35)
    Texto =miFuenteSistema.render("Fin del Juego",0,(255,255,255))

    Jugador = naveEspacial(ancho,alto)
    cargarEnemigos()
    


  

    enJuego=True



    reloj = pygame.time.Clock()

    while True:
        reloj.tick(60)

        

        tiempo = int(pygame.time.get_ticks()/1000)

        for evento in pygame.event.get():
            if evento.type==QUIT:
                pygame.quit()
                sys.exit()
            if enJuego==True:
                if evento.type == pygame.KEYDOWN:
                    if evento.key ==K_LEFT:
                        Jugador.movimientoIzquierda()
                
                    elif evento.key==K_RIGHT:
                        Jugador.movimientoDerecha()
                    
                    elif evento.key==K_SPACE:
                        x,y=Jugador.rect.center
                        Jugador.disparar(x,y)


        ventana.blit(ImagenFondo,(0,0))

        Jugador.dibujar(ventana)


        if len(Jugador.listaDisparo)>0:
            for x in Jugador.listaDisparo:
                x.dibujar(ventana)
                x.trayectoria()

                if x.rect.top<10:
                    Jugador.listaDisparo.remove(x)
                else:
                    for enemigo in listaEnemigo:
                        if x.rect.colliderect(enemigo.rect):
                            listaEnemigo.remove(enemigo)
                            Jugador.listaDisparo.remove(x)
                            sonidoExplosion.play()
        if len(listaEnemigo)>0:
            for enemigo in listaEnemigo:
                enemigo.comportamiento(tiempo)
                enemigo.dibujar(ventana)

                if enemigo.rect.colliderect(Jugador.rect):
                    Jugador.destruccion()
                    enJuego=False
                    detenerTodo()

                if len(enemigo.listaDisparo)>0:
                    for x in enemigo.listaDisparo:
                        x.dibujar(ventana)
                        x.trayectoria()

                        if x.rect.colliderect(Jugador.rect):
                            Jugador.destruccion()
                            enJuego=False
                            detenerTodo()

                        if x.rect.top>900:
                            enemigo.listaDisparo.remove(x)
                        else:
                            for disparo in Jugador.listaDisparo:
                                if x.rect.colliderect(disparo.rect):
                                    Jugador.listaDisparo.remove(disparo)
                                    enemigo.listaDisparo.remove(x)

        if enJuego == False:
            pygame.mixer.music.fadeout(3000)
            ventana.blit(Texto,(300,250))

        pygame.display.flip()


#seguir = True
#while seguir == True:
    SpaceInvader()
#    miFuenteSistema2 = pygame.font.SysFont("Arial",25)
#    Texto2 =miFuenteSistema.render("Reiniciar? Y/N",0,(255,255,255))
#    ventana.blit(Texto2,(300,350))