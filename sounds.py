import pygame.mixer

pygame.init()
teclas_inicial = pygame.mixer.Sound("sons/select.wav")
espaco = pygame.mixer.Sound("sons/select_espaco.wav")
esplosao_inimigo = pygame.mixer.Sound("sons/esplosao.wav")
tiro = pygame.mixer.Sound("sons/tiro.wav")
exp = pygame.mixer.Sound("sons/esp_personagem.wav")

def tocar_musica_inicial():
    pygame.mixer.music.load("sons/hope_destiny.mp3")
    pygame.mixer.music.play(-1)

def parar_musica_inicial():
    pygame.mixer.music.stop()

def tocar_musica_principal():
    pygame.mixer.music.load("sons/musica.mp3")
    pygame.mixer.music.play(-1)

def som_espaco_menu():
    espaco.play()

def som_setas_menu():
    teclas_inicial.play()

def esplosao_ini():
    esplosao_inimigo.play()

def som_tiro():
    tiro.play()

def exp_personagem():
    exp.play()

