import pygame
import sys
import os
import random

pygame.init()
screen = pygame.display.set_mode((1000,700))
screen.fill((255,255,255))

#inimigo
cont_inimigo_1 = 0
cont_inimigo_2 = 0
cont_inimigo_3 = 0


x_inimigo_1 = 1002
x_inimigo_2 = 1002
x_inimigo_3 = 1002
y_inimigo_1 = 100
y_inimigo_2 = 200
y_inimigo_3 = 300

velocidade = 2
old_pont = 0

folder = "img"
mina = pygame.image.load(os.path.join(folder,"mina_cópia.png"))

def iniciar_inimigo():
    global velocidade, old_pont, cont_inimigo_1, cont_inimigo_2, cont_inimigo_3, x_inimigo_1, x_inimigo_2, x_inimigo_3, y_inimigo_1, y_inimigo_2, y_inimigo_3 
    cont_inimigo_1 = 0
    cont_inimigo_2 = 0
    cont_inimigo_3 = 0


    x_inimigo_1 = 1002
    x_inimigo_2 = 1002
    x_inimigo_3 = 1002
    y_inimigo_1 = 100
    y_inimigo_2 = 200
    y_inimigo_3 = 300

    velocidade = 2
    old_pont = 0

def desenhar_inimigo(inimigo_1, inimigo_2, inimigo_3, pontuacao, defesa):
    global velocidade, old_pont, cont_inimigo_1, cont_inimigo_2, cont_inimigo_3, x_inimigo_1, x_inimigo_2, x_inimigo_3, y_inimigo_1, y_inimigo_2, y_inimigo_3 

    if pontuacao - old_pont == 100:
        old_pont = pontuacao
        velocidade += 1.2
        
    if inimigo_1 == True:
        x_inimigo_1 -= velocidade
        screen.blit(mina, (x_inimigo_1,y_inimigo_1)) #inimigo_1
        if x_inimigo_1 + 80 <= -2:
            inimigo_1 = False
            defesa -= 1
    else:
        cont_inimigo_1 += 1
        x_inimigo_1 = 1002
        if cont_inimigo_1 == 80:
            cont_inimigo_1 = 0
            y_inimigo_1 = random.randint(30, 430)
            while (y_inimigo_1 + 80 >= y_inimigo_2 and y_inimigo_1 <= y_inimigo_2 + 80) or (y_inimigo_1 + 80 >= y_inimigo_3 and y_inimigo_1 <= y_inimigo_3 + 80):
                y_inimigo_1 = random.randint(10, 430)
            x_inimigo_1 = 1002
            inimigo_1 = True

    if inimigo_2 == True:
        x_inimigo_2 -= velocidade
        screen.blit(mina, (x_inimigo_2,y_inimigo_2)) #inimigo_2
        if x_inimigo_2 + 80 <= -2:
            inimigo_2 = False
            defesa -= 1
    else:
        cont_inimigo_2 += 1
        x_inimigo_2 = 1002
        if cont_inimigo_2 == 150:
            cont_inimigo_2 = 0
            y_inimigo_2 = random.randint(30, 430)
            while (y_inimigo_2 + 80 >= y_inimigo_1 and y_inimigo_2 <= y_inimigo_1 + 80) or (y_inimigo_2 + 80 >= y_inimigo_3 and y_inimigo_2 <= y_inimigo_3 + 80):
                y_inimigo_2 = random.randint(10, 430)
            inimigo_2 = True
            
    if inimigo_3 == True:
        x_inimigo_3 -= velocidade
        screen.blit(mina, (x_inimigo_3,y_inimigo_3)) #inimigo_1
        if x_inimigo_3 + 80 <= -2:
            inimigo_3 = False
            defesa -= 1
    else:
        x_inimigo_3 = 1002
        cont_inimigo_3 += 1
        if cont_inimigo_3 == 200:
            cont_inimigo_3 = 0
            y_inimigo_3 = random.randint(30, 430)
            while (y_inimigo_3 + 80 >= y_inimigo_1 and y_inimigo_3 <= y_inimigo_1 + 80) or (y_inimigo_3 + 80 >= y_inimigo_2 and y_inimigo_3 <= y_inimigo_2 + 80):
                y_inimigo_3 = random.randint(10, 430)
            inimigo_3 = True
    return [inimigo_1, x_inimigo_1, y_inimigo_1, inimigo_2, x_inimigo_2, y_inimigo_2, inimigo_3, x_inimigo_3, y_inimigo_3, defesa]
    #           0           1            2            3         4            5             6            7         8           9   
     #terminar de desenhar inimigos

    
