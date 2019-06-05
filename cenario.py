#cenário
import pygame
import random
import os

pygame.init()
screen = pygame.display.set_mode((1000,700))
pygame.display.set_caption("RUN BOY")
screen.fill((255,255,255))

x_nuvem = 600
y_nuvem = 100

x_ilha_pequena = 1000
x_ilha_media = 1000
x_ilha_grande = 1000

x_ilha_voadora = 700
y_ilha_voadora = 400

folder = "img"
nuvem = pygame.image.load(os.path.join(folder,"nuvem.png"))
largura_nuvem = nuvem.get_rect().size[0]

fundo = pygame.image.load(os.path.join(folder,"background.png"))
mar = pygame.image.load(os.path.join(folder,"mar.png"))

ilha_grande = pygame.image.load(os.path.join(folder,"ilha_grande.png"))

ilha_voadora = pygame.image.load(os.path.join(folder,"ilha_voadora.png"))

def imprimir_cenario():
    var_cenario = cenario()
    screen.blit(fundo,(0,0))
    screen.blit(ilha_voadora, (var_cenario[5],var_cenario[6]))
    screen.blit(nuvem, (var_cenario[0],var_cenario[1])) #nuvem
    screen.blit(mar, (0,540)) #chão
    screen.blit(ilha_grande,(var_cenario[4],493))

def cenario():
    
    global x_nuvem, y_nuvem, x_ilha_pequena, x_ilha_media, x_ilha_grande, x_ilha_voadora, y_ilha_voadora
    
    x_nuvem -= 0.8
    
    x_ilha_pequena -= 0.6
    x_ilha_media -= 0.4
    x_ilha_grande -= 0.2

    x_ilha_voadora -= 0.3

    if x_ilha_voadora + 100 <= 0:
        x_ilha_voadora = 1002
        y_ilha_voadora = random.randint(340, 400)
    
    if x_nuvem + largura_nuvem  <= 0:
        x_nuvem = 1300
        y_nuvem = random.randint(20, 260)

    if x_ilha_pequena + 50 <= -0.5:
        x_ilha_pequena = 1002
    if x_ilha_media + 90 <= -0.5:
        x_ilha_media = 1002
    if x_ilha_grande + 170 <= -0.5:
        x_ilha_grande = 1002
    return [x_nuvem, y_nuvem, x_ilha_pequena, x_ilha_media, x_ilha_grande, x_ilha_voadora, y_ilha_voadora]
    

