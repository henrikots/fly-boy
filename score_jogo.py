import pygame
import sys
import cenario
import os
import ranking
import sounds

pygame.init()
screen = pygame.display.set_mode((1000,700))
pygame.display.set_caption("RUN BOY")
screen.fill((255,255,255))
num = 0
folder = "img"
fonte = pygame.font.SysFont("arial", 50)
paper = pygame.image.load(os.path.join(folder,"old_paper.png"))
def mostrar_pontuacao(pontuacao, defesa, vida, tempo):
    
    global num
    num += 1
    tempo = int(tempo/60)
    sair = False
    name = "Jogador " + str(num)
    while not sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sounds.som_espaco_menu()
                    sair = True
                
        nome = fonte.render("Jogador  " + str(num), 1, (0,0,0))
        pont = fonte.render("Pontuação   " + str(pontuacao), 1, (0,0,0))
        defe = fonte.render("Defesa         " + str(defesa) + "        x 50", 1, (0,0,0))
        life = fonte.render("Vida             " + str(vida) + "        x 50 ", 1,(0,0,0))
        temp = fonte.render("Tempo          " + str(tempo) + "    x 50", 1, (0,0,0))

        total = pontuacao + defesa * 50 + vida * 50 + tempo * 50

        tot = fonte.render("Total: " + str(total) + "pts", 1, (0,0,0))
        
        cenario.imprimir_cenario()
        screen.blit(paper,(200,140))
        screen.blit(nome, (240,190))
        screen.blit(pont, (240,260))
        screen.blit(defe, (240,310))
        screen.blit(life, (240,360))
        screen.blit(temp, (240,410))
        screen.blit(tot, (260, 480))

        pygame.display.update()
        
    ranking.guardar_pontuacao([name, total])
    ranking.mostrar_pontuacao()
    

