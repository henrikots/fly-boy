import pygame
import sys
import cenario
import os
import sounds

pygame.init()
screen = pygame.display.set_mode((1000,700))
pygame.display.set_caption("RUN BOY")
screen.fill((255,255,255))

fonte = pygame.font.SysFont("arial", 50)
folder = "img"
paper = pygame.image.load(os.path.join(folder,"old_paper.png"))

rank = []

def bubbleSort():
    global rank
    for i in range(0, len(rank)):
        for u in range(0, len(rank) - 1):
            if rank[u][1] < rank[u+1][1]:
                a = rank[u]
                rank[u] = rank[u + 1]
                rank[u+1] = a

bubbleSort()

def guardar_pontuacao(pontuacao):
    global rank
    if len(rank) < 5:
        rank.append(pontuacao)
    else:
        rank[4] = pontuacao
    if len(rank) > 1:
        bubbleSort()

def mostrar_pontuacao():
    global rank
    sair = False
    while not sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sounds.som_espaco_menu()
                    sair = True
            
           
        cenario.imprimir_cenario()
        screen.blit(paper,(200,140))
        if len(rank) > 0:
            cont = 1
            y = 260
            for i in rank:
                escrever_nome = i[0]
                escrever_ponto = i[1]
                nome = fonte.render(str(cont) + "º - " + str(escrever_nome) + " - " + str(escrever_ponto) + "pts", 1, (0,0,0))
                screen.blit(nome,(240, y))
                cont += 1
                y += 50
        else:
            vazio = fonte.render("Sem dados ", 1, (0,0,0))
            screen.blit(vazio, (240, 260))
        ranking = fonte.render("Ranking ", 1, (0,0,0))
        screen.blit(ranking, (240, 190))
        pygame.display.update()




