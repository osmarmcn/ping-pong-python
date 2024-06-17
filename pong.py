import pygame
import sys

pygame.init()
# Tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Ping-Pong')

branco = (255,255,255)
preto = (0,0,0)

# Dados Bola
raio_bola = 15
velocidade_x_bola = 5
velocidade_y_bola = 5
bola = pygame.Rect(largura//2 - raio_bola,
                   altura//2 - raio_bola,
                   raio_bola,
                   raio_bola)

# Dados Plataforma
largura_plataforma = 10
altura_plataforma = 40
velocidade_plataforma = 10
player1 = pygame.Rect(10,
                      altura//2 - altura_plataforma//2,
                      largura_plataforma,
                      altura_plataforma)
player2 = pygame.Rect(largura - 10,
                      altura//2 - altura_plataforma//2,
                      largura_plataforma,
                      altura_plataforma)

player1_score = 0
player2_score = 0
font = pygame.font.Font(None, 74)


def moverBolinha():
    global velocidade_x_bola,velocidade_y_bola,bola,player1_score,player2_score

    bola.x += velocidade_x_bola
    bola.y += velocidade_y_bola


    #Colisões com a Tela
    if (bola.top <= 0 or bola.bottom>= altura):
        velocidade_y_bola *= -1


    # if (bola.left <= 0 or bola.right >= largura):
    #     bola.center = (largura//2,altura//2)
    #     velocidade_x_bola *= -1

    if bola.left <= 0:
        player2_score += 1
        bola.center = (largura//2,altura//2)
        velocidade_x_bola *= -1
    elif bola.right >= largura:
        player1_score += 1
        bola.center = (largura//2,altura//2)
        velocidade_x_bola *= -1

    
    # Colisões com a raquete
    if (bola.colliderect(player1) or bola.colliderect(player2)):
        velocidade_x_bola *= -1



def moverPlataforma():
    global velocidade_plataforma

    teclas = pygame.key.get_pressed()
    # Checagem player 1
    if teclas[pygame.K_w] and player1.top > 0:
        player1.y -= velocidade_plataforma
    if teclas[pygame.K_s] and player1.bottom < altura : 
        player1.y += velocidade_plataforma

    # Checagem player 2
    # if teclas[pygame.K_o] and player2.top > 0 :
    #     player2.y -= velocidade_plataforma
    # if teclas[pygame.K_l] and player2.bottom < altura:
    #     player2.y += velocidade_plataforma

    #Criando uma IA básica
    if player2.centery < bola.centery and player2.bottom < altura:
        player2.y += velocidade_plataforma
    elif player2.centery > bola.centery and player2.top > 0:
        player2.y -= velocidade_plataforma

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Movimentos
    moverBolinha()
    moverPlataforma()

    #Tela
    tela.fill(preto)
    pygame.draw.rect(tela,
                     branco,
                     player1)
    

    #Desenhar na tela
    pygame.draw.rect(tela, branco,player1)
    pygame.draw.rect(tela, branco,player2)
    pygame.draw.ellipse(tela,branco,bola)
    pygame.draw.aaline(tela,branco,
                       (largura//2,0),
                       (largura//2, altura))



    # Desenhar o placar
    player1_text = font.render(str(player1_score), True, branco)
    tela.blit(player1_text, (largura// 4, 20))
    player2_text = font.render(str(player2_score), True, branco)
    tela.blit(player2_text, (largura * 3 // 4, 20))


    #Atualizar tela
    pygame.display.flip()

    # Controle de FPS
    pygame.time.Clock().tick(60)