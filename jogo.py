import pygame
import sys
import os
import cenario
import random
import inimigos
import time
import score_jogo
import sprite
import sounds

#inicia o pygame
pygame.init()
screen = pygame.display.set_mode((1000,700))
pygame.display.set_caption("RUN BOY")
screen.fill((255,255,255))

#função para escrever o layout
def layout(pontuacao, vida, defesa):
    fonte = pygame.font.SysFont("arial", 20)
    pont = "Pontuação: " + str(pontuacao)
    vid = "Vida: " + str(vida)
    defe = "Defesa: " + str(defesa)
    defes = fonte.render(defe, 1, (0,0,0))
    score = fonte.render(pont,1, (0,0,0))
    life = fonte.render(vid,1, (0,0,0))
    screen.blit(life, (5,5))
    screen.blit(score, (850, 5))
    screen.blit(defes,(450, 5))

#função para escrever o pause
def pause():
    fonte = pygame.font.SysFont("arial", 50)
    pause = fonte.render("P", 1, (0,0,0))
    screen.blit(pause,(490, 100))

#início do jogo
def jogo():

    sounds.tocar_musica_principal()
    hit = False
    
    #inicia os valores dos inimigos
    inimigos.iniciar_inimigo()

    #pega o tempo de início
    time_inicial = int(time.time())

    #variáveis que determinará se será chamado a animação de explosão
    exp1 = False
    exp2 = False
    exp3 = False

    #váriáveis x e y do personagem
    x = 51
    y = 200

    #variáveis que determina quais inimigos irão aparecer
    inimigo_1 = True
    inimigo_2 = False
    inimigo_3 = False

    #variáveis que rotacionam o personagem
    rodar = False
    cont_girar = 0
    valor_rotate = 0

    #variáveis de controle de pontuação, vida e defesa
    pontuacao = 0
    vida = 3
    defesa = 5

    #variável que receberá a imagem do personagem
    personagem = sprite.desenhar_nave(hit)
    largura_personagem, altura_personagem = personagem.get_rect().size

    #variáveis de controle do tiro
    tiro = False
    cont_tiro = 1
    dist = 0
    iniciar_tiro = False

    #função de controle de frames
    clock = pygame.time.Clock()

    #varável para controlar o pause
    vdd = False

    #carrega o sprite do tiro
    bala = sprite.desenhar_tiro()

    cont_hit = 1
    
    while True:
        #determina a quantidade de frames por segundo
        clock.tick(30)

        if hit == True:
            cont_hit += 1
            if cont_hit == 8:
                cont_hit = 1
                hit = False

        #carrega o sprite da nave a ser mostrado
        personagem = sprite.desenhar_nave(hit)
        personagem = pygame.transform.rotate(personagem, valor_rotate)

        #------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #verifica a entrada de dados dos teclados
        #cima
        if pygame.key.get_pressed()[pygame.K_UP]:
            y -= 5
            if y <= 0:
                y += 5
        #baixo
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            y += 5
        #esquerda
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            x -= 5
            if x <= 50:
                x += 5
        #direita
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            rodar = True
            x += 6.5
            if x + largura_personagem >= 400:
                x -= 5
        else:
            rodar = False
        #espaço
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            if tiro == False:
                tiro = True
                iniciar_tiro = True
        #------------------------------------------------------------------------------------------------------------------------------------------------------------------
                
        #diminui o valor de x do personagem para ele ao valor inicial se nenhuma tecla é clicada
        x -= 1.5
        if x <= 50:
            x += 1.5

        #verifica se o personagem encostou no mar ou a defesa é igual a 0
        if y + altura_personagem >= 542:
            vida = 0

        if defesa == 0:
            continuar = True
            sounds.exp_personagem()
            while continuar == True:
                clock.tick(20)
                cenario.imprimir_cenario()
                continuar = sprite.desenhar_exp_nave(x,y)
                pygame.display.update()
                
            break

        #faz com que o personagem se incline quando a seta da direita for clicada
        if rodar == True:
            if cont_girar <= 6:
                personagem = pygame.transform.rotate(personagem, 0.75)
                valor_rotate += 0.75
                cont_girar += 1
            
        if rodar == False:
            if cont_girar >= 6:
                personagem = pygame.transform.rotate(personagem, -0.75)
                valor_rotate -= 0.75
                cont_girar -= 1

        #------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #chama a função para imprimir o cenário do jogo
        cenario.imprimir_cenario()

        #o 'var_inimigos' recebe os valores de x e y dos inimigos, e seus estados, True ou False
        var_inimigos = inimigos.desenhar_inimigo(inimigo_1, inimigo_2, inimigo_3, pontuacao, defesa)
        inimigo_1 = var_inimigos[0]
        inimigo_2 = var_inimigos[3]
        inimigo_3 = var_inimigos[6]

        # 'var_inimigos' também passa o valor de defesa ainda restante
        defesa = var_inimigos[9]

        #------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # desenha o tiro e seu percurso 
        if tiro == True:
            if iniciar_tiro == True:
                sounds.som_tiro()
                #é setado o valor inicial do tiro de acordo com o personagem
                x_tiro = x + 100
                y_tiro = y + 54
                iniciar_tiro = False
            screen.blit(bala, (x_tiro ,y_tiro)) #tiro
            #velocidade do tiro
            x_tiro += 20
            #distancia percorrida pelo tiro
            dist += 20
            if dist == 600:
                #se a distancia percorrida for igual a 600 ele some
                tiro = False
                dist = 0
                
        #------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #verificação da colisão do tiro com os inimigos e dos inimigos com o personagem
        if inimigo_1 == True:
            # verificação de colisão da altura e largura do personagem com o inimigo 1 
            if y + altura_personagem  >= var_inimigos[2] and y <= var_inimigos[2] + 80 and x + largura_personagem >= var_inimigos[1] and x <= var_inimigos[1] + 80:
                #se verdadeiro o inimigo desaparece, é descontado vida, e é chamado e setado os valores para a animação de explosão
                inimigo_1 = False
                vida -= 1
                exp1 = True
                x_exp1 = var_inimigos[1]
                y_exp1 = var_inimigos[2]
                hit = True
                sounds.esplosao_ini()
            #verificação de colisão do tiro com o inimigo 1
            if tiro == True and (y_tiro + 10  >= var_inimigos[2] and y_tiro <= var_inimigos[2] + 80 and x_tiro >= var_inimigos[1]):
                #se verdadeiro o inimigo desaparece, é acrescentado da pontuação e é chamado e setado os valores da animação de explosão
                inimigo_1 = False
                pontuacao += 5
                exp1 = True
                x_exp1 = var_inimigos[1]
                y_exp1 = var_inimigos[2]
                sounds.esplosao_ini()
        #------------------------------------------------------------------------------------------------------------------------------------------------------------------
        if inimigo_2 == True:
            # verificação de colisão da altura e largura do personagem com o inimigo 2
            if y + altura_personagem  >= var_inimigos[5] and y <= var_inimigos[5] + 80 and x + largura_personagem >= var_inimigos[4] and x <= var_inimigos[4] + 80:
                #se verdadeiro o inimigo desaparece, é descontado vida, e é chamado e setado os valores para a animação de explosão
                inimigo_2 = False
                vida -= 1
                exp2 = True
                x_exp2 = var_inimigos[4]
                y_exp2 = var_inimigos[5]
                hit = True
                sounds.esplosao_ini()
            #verificação de colisão do tiro com o inimigo 2
            if tiro == True and (y_tiro + 10 >= var_inimigos[5] and y_tiro <= var_inimigos[5] + 80 and x_tiro >= var_inimigos[4]):
                #se verdadeiro o inimigo desaparece, é acrescentado da pontuação e é chamado e setado os valores da animação de explosão
                inimigo_2 = False
                pontuacao += 5
                exp2 = True
                x_exp2 = var_inimigos[4]
                y_exp2 = var_inimigos[5]
                sounds.esplosao_ini()
        #------------------------------------------------------------------------------------------------------------------------------------------------------------------  
        if inimigo_3 == True:
            # verificação de colisão da altura e largura do personagem com o inimigo 3
            if y + altura_personagem  >= var_inimigos[8] and y <= var_inimigos[8] + 80 and x + largura_personagem >= var_inimigos[7] and x <= var_inimigos[7] + 80:
                #se verdadeiro o inimigo desaparece, é descontado vida, e é chamado e setado os valores para a animação de explosão
                inimigo_3 = False
                vida -= 1
                exp3 = True
                x_exp3 = var_inimigos[7]
                y_exp3 = var_inimigos[8]
                hit = True
                sounds.esplosao_ini()
            #verificação de colisão do tiro com o inimigo 3
            if tiro == True and (y_tiro + 10 >= var_inimigos[8] and y_tiro <= var_inimigos[8] + 80 and x_tiro >= var_inimigos[7]):
                #se verdadeiro o inimigo desaparece, é acrescentado da pontuação e é chamado e setado os valores da animação de explosão
                inimigo_3 = False
                pontuacao += 5
                exp3 = True
                x_exp3 = var_inimigos[7]
                y_exp3 = var_inimigos[8]
                sounds.esplosao_ini()
        #------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #se a explosão for chamada ela irá chamar uma função para ser desenhada
        if exp1 == True:
            exp1 = sprite.desenhar_exp1(x_exp1, y_exp1)
        if exp2 == True:
            exp2 = sprite.desenhar_exp2(x_exp2, y_exp2)
        if exp3 == True:
            exp3 = sprite.desenhar_exp3(x_exp3, y_exp3)
        #------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #verifica se o usuário ainda está com vida
        if vida <= 0:
            sounds.exp_personagem()
            continuar = True
            while continuar == True:
                clock.tick(20)
                cenario.imprimir_cenario()
                continuar = sprite.desenhar_exp_nave(x,y)
                pygame.display.update()
            break

        #é chamado o layout
        layout(pontuacao, vida, defesa) #layout
        
        #a nave é desenhada na tela
        screen.blit(personagem,(x,y)) #personagem
        

        
        #pausar jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    vdd = True
                    while vdd:
                        pause()
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_p:
                                    vdd = False
        
        pygame.display.update()#atualiza a tela
    
    sounds.parar_musica_inicial()    
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #pega o tempo do termino
    time_atual = int(time.time())
    #faz uma subtração para saber os segundos
    seg = time_atual - time_inicial
    #é chamado a tela de pontos
    score_jogo.mostrar_pontuacao(pontuacao, defesa, vida, seg)

