import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()


largura = 640
altura = 480
x_Snake = largura/2
y_Snake = altura/2
velocidade = 2
x_controle = velocidade
y_controle = 0

x_Apple= randint(40,600)
y_Apple = randint(50,430)

pontos = 0
fonte = pygame.font.SysFont('arial',40,True,True)

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Snake Game')
relogio = pygame.time.Clock()
lista_cobra = []
comprimento_inicial = 5
morreu = False

def aumenta_Snake(lista_cobra):
    for xey in lista_cobra:
        pygame.draw.rect(tela,(0,255,0),(xey[0],xey[1],20,20))

def reiniciar_jogo():
    global pontos,comprimento_inicial,x_Snake,y_Snake,lista_cobra,lista_cabeca,x_Apple,y_Apple,morreu
    pontos = 0
    comprimento_inicial = 5
    x_Snake = int(largura/2)
    y_Snake = int(largura/2)
    lista_cobra =[]
    lista_cabeca = []
    x_Apple= randint(40,600)
    y_Apple = randint(50,430)
    morreu = False

while True:
    relogio.tick(120)
    tela.fill((255,255,255))
    mensagem = f'Pontos:{pontos}'
    texto_formatado = fonte.render(mensagem, True, (0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0

            if event.key == K_d:
                if x_controle == - velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0

            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0

            if event.key == K_s:
                if y_controle == - velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0
               
    x_Snake = x_Snake + x_controle
    y_Snake = y_Snake + y_controle
        

    Snake = pygame.draw.rect(tela, (0,255,0),(x_Snake,y_Snake,20,20))
    Apple = pygame.draw.rect(tela, (255,0,0),(x_Apple,y_Apple,20,20))

    if Snake.colliderect(Apple):
        x_Apple = randint(40,600)
        y_Apple = randint(50,430)
        pontos = pontos + 1
        comprimento_inicial = comprimento_inicial + 20
        

    lista_cabeca = []
    lista_cabeca.append(x_Snake)
    lista_cabeca.append(y_Snake)
    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial',20,True,True)
        mensagem = 'Game Over! Pressione R para jogar novamente'
        texto_formatado = fonte2.render(mensagem,True, (0,0,0))
        ret_texto = texto_formatado.get_rect()

        morreu = True 
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            ret_texto.center = (largura//2, largura//2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()

    if x_Snake > largura:
        x_Snake = 0

    if x_Snake < 0:
        x_Snake = largura

    if y_Snake < 0:
        y_Snake = largura

    if y_Snake > largura:
        y_Snake = 0

    


    if len(lista_cobra) > comprimento_inicial:
         del lista_cobra[0]

    aumenta_Snake(lista_cobra)

  


   
    
    tela.blit(texto_formatado, (450,40))
    pygame.display.update()




