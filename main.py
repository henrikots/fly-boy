import pygame
import sys
import os
import random
import cenario
import jogo
import tutorial
import ranking
import pygame.mixer
import sounds

pygame.init()
screen = pygame.display.set_mode((1000,700))
pygame.display.set_caption("FLY BOY")
screen.fill((255,255,255))
folder = "img"



def menu_iniciar():
    sounds.tocar_musica_inicial()
    cont = 1
    fonte = pygame.font.SysFont("arial", 70)
    fly_boy = pygame.image.load(os.path.join(folder,"fly_boy.png"))
    while True:

        if cont == 1:
            cor_1 = (255,255,255)
            cor_2 = (0,0,0)
            cor_3 = (0,0,0)
        elif cont == 2:
            cor_1 = (0,0,0)
            cor_2 = (255,255,255)
            cor_3 = (0,0,0)
        else:
            cor_1 = (0,0,0)
            cor_2 = (0,0,0)
            cor_3 = (255,255,255)
            
        inicio = fonte.render("Iniciar Jogo",70,cor_1)
        rank = fonte.render("Ranking",100,cor_2)
        tecl = fonte.render("Teclado(tutorial)", 100, cor_3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    sounds.som_setas_menu()
                    if cont > 1:
                        cont -= 1
                if event.key == pygame.K_DOWN:
                    sounds.som_setas_menu()
                    if cont < 3:
                        cont += 1
                if event.key == pygame.K_SPACE:
                    sounds.som_espaco_menu()
                    if cont == 1:
                        sounds.parar_musica_inicial()
                        jogo.jogo()
                        sounds.tocar_musica_inicial()
                    elif cont == 2:
                        ranking.mostrar_pontuacao()
                    elif cont == 3:
                        tutorial.show_tutorial()
        
        
        cenario.imprimir_cenario()
        screen.blit(inicio, (100, 200))
        screen.blit(rank, (100, 300))
        screen.blit(tecl,(100, 400))
        screen.blit(fly_boy,(50,50))
        pygame.display.update()
        
            
menu_iniciar()
                
                

