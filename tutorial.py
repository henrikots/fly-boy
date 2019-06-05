import pygame
import sys
import os
import cenario
import jogo
import sounds

pygame.init()
screen = pygame.display.set_mode((1000,700))
pygame.display.set_caption("RUN BOY")
screen.fill((255,255,255))


#tutorial
def show_tutorial():
    folder = "img"
    setas = pygame.image.load(os.path.join(folder,"setas.png"))
    espaco = pygame.image.load(os.path.join(folder,"espaco.png"))
    p = pygame.image.load(os.path.join(folder,"p.png"))
    fonte = pygame.font.SysFont("arial", 25)
    mover = fonte.render("Mover Personagem",1, (0,0,0))
    atirar = fonte.render("Atirar/Selecionar",1, (0,0,0))
    pause = fonte.render("Pausar/Retomar",1, (0,0,0))
    continuar = fonte.render("Aperte [Enter] para voltar ao menu, ou [Espaço] para começar o Jogo.", 1, (0,0,0))
    parar = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sounds.parar_musica_inicial()
                    sounds.som_espaco_menu()
                    jogo.jogo()
                    parar = True
                if event.key == pygame.K_RETURN:
                    sounds.som_espaco_menu()
                    parar = True
        if parar == True:
            break
        cenario.imprimir_cenario()
        screen.blit(mover,(190,160))
        screen.blit(setas,(200,200))
        screen.blit(atirar,(570,160))
        screen.blit(espaco, (500, 200))
        screen.blit(pause,(450,320))
        screen.blit(p,(500, 350))
        pygame.draw.rect(screen,(255,255,255),(115,595,795, 35))
        screen.blit(continuar,(120, 600))
        pygame.display.update()


