import os
import pygame

pygame.init()
screen = pygame.display.set_mode((1000,700))
pygame.display.set_caption("RUN BOY")
screen.fill((255,255,255))

cont1 = 0
cont2 = 0
cont3 = 0

folder = "img"

cont_personagem = 0

def hit():
    hit1 = pygame.image.load(os.path.join(folder,"hit1.png"))
    hit2 = pygame.image.load(os.path.join(folder,"hit2.png"))
    hit3 = pygame.image.load(os.path.join(folder,"hit3.png"))
    hit4 = pygame.image.load(os.path.join(folder,"hit4.png"))
    hit5 = hit3
    hit6 = hit2
    hit7 = hit1

    return [hit1, hit2, hit3, hit4, hit5, hit6, hit7]

def exp_inimigo():

    
    exp1 = pygame.image.load(os.path.join(folder,"exp1.png"))
    exp2 = pygame.image.load(os.path.join(folder,"exp2.png"))
    exp3 = pygame.image.load(os.path.join(folder,"exp3.png"))
    exp4 = pygame.image.load(os.path.join(folder,"exp4.png"))
    exp5 = pygame.image.load(os.path.join(folder,"exp5.png"))
    exp6 = pygame.image.load(os.path.join(folder,"exp6.png"))
    exp7 = pygame.image.load(os.path.join(folder,"exp7.png"))
    exp8 = pygame.image.load(os.path.join(folder,"exp8.png"))

    return [exp1, exp2, exp3, exp4, exp5, exp6, exp7, exp8]

def desenhar_exp1(x,y):
    global cont1
    exp = exp_inimigo()
    screen.blit(exp[cont1], (x, y))
    cont1 += 1
    if cont1 == 8:
        cont1 = 0
        return False
    return True

def desenhar_exp2(x,y):
    global cont2
    exp = exp_inimigo()
    screen.blit(exp[cont2], (x, y))
    cont2 += 1
    if cont2 == 8:
        cont2 = 0
        return False
    return True

def desenhar_exp3(x,y):
    global cont3
    exp = exp_inimigo()
    screen.blit(exp[cont3], (x, y))
    cont3 += 1
    if cont3 == 8:
        cont3 = 0
        return False
    return True


def sprite_nave():
    nave1 = pygame.image.load(os.path.join(folder,"nave1.png"))
    nave2 = pygame.image.load(os.path.join(folder,"nave2.png"))
    nave3 = pygame.image.load(os.path.join(folder,"nave3.png"))
    return [nave1, nave2, nave3]

nave = sprite_nave()
nave_hit = hit()
cont_hit = 0
def desenhar_nave(dano):
    global nave 
    global cont_personagem
    global nave_hit
    global cont_hit
    
    if dano == True:
        nv = nave_hit[cont_hit]
        cont_hit += 1
        if cont_hit == 6:
            cont_hit = 0
    else:
        nv = nave[cont_personagem]
        cont_personagem += 1
        if cont_personagem == 3:
            cont_personagem = 0
    
    return nv

def desenhar_tiro():
    bala = pygame.image.load(os.path.join(folder,"bala.png"))
    return bala

def explosao_personagem():
    exp1 = pygame.image.load(os.path.join(folder,"exp_nave1.png"))
    exp2 = pygame.image.load(os.path.join(folder,"exp_nave2.png"))
    exp3 = pygame.image.load(os.path.join(folder,"exp_nave3.png"))
    exp4 = pygame.image.load(os.path.join(folder,"exp_nave4.png"))
    exp5 = pygame.image.load(os.path.join(folder,"exp_nave5.png"))
    exp6 = pygame.image.load(os.path.join(folder,"exp_nave6.png"))
    exp7 = pygame.image.load(os.path.join(folder,"exp_nave7.png"))
    exp8 = pygame.image.load(os.path.join(folder,"exp_nave8.png"))
    exp9 = pygame.image.load(os.path.join(folder,"exp_nave9.png"))
    exp10 = pygame.image.load(os.path.join(folder,"exp_nave10.png"))
    exp11 = pygame.image.load(os.path.join(folder,"exp_nave11.png"))

    return [exp1, exp2, exp3, exp4, exp5, exp6, exp7, exp8, exp9, exp10, exp11]

cont_nave = 0
def desenhar_exp_nave(x, y):
    global cont_nave, cont_geral, new
    exp = explosao_personagem()
    screen.blit(exp[cont_nave], (x, y))
    cont_nave += 1
    if cont_nave == 8:
        cont_nave = 0
        return False
    return True



    
