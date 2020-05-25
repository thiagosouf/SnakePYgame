import pygame , random
from pygame.locals import *

def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return((x//10)*10, (y//10)*10)

def colisao(c1 ,c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600,600)) #tamanho do display
pygame.display.set_caption('Snake') #tilulo

snake = [(200, 200),(210,200),(220,200)] #O 0 da matriz é superior esquerdo
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255)) #cor da cobra

maca_pos = on_grid_random()
maca = pygame.Surface((10,10))
maca.fill((255,0,0))

minha_direcao = LEFT

clock = pygame.time.Clock()
velocidade = 10

font = pygame.font.Font('freesansbold.ttf', 18) #Score????
score = 0


game_over = False
while not game_over:
    clock.tick(velocidade)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type ==  KEYDOWN:
            if event.key == K_UP:
                minha_direcao=UP
            if event.key == K_DOWN:
                minha_direcao=DOWN
            if event.key == K_RIGHT:
                minha_direcao=RIGHT
            if event.key == K_LEFT:
                minha_direcao=LEFT


    if colisao(snake[0],maca_pos): #cada vez que a cobra come a maca
        maca_pos = on_grid_random() #nova posicao da maca
        snake.append((0,0)) #a cobra ganha um append no rabo
        velocidade = velocidade + 5 #velociade aumenta 5
        score = score +1

    # Se a cobra encostar na borda do jogo
    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True
        break

    # Se a cobra encostar nela mesma
    for i in range(1, len(snake) -1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break
    if game_over:
        break

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    # Comandos que fazem a cobra se mover
    if minha_direcao == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if minha_direcao == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if minha_direcao == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if minha_direcao == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])



    screen.fill((0,0,0))
    screen.blit(maca,maca_pos)

    for x in range(0, 600, 10):  # Pinta linhas Horizontais
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))
    for y in range(0, 600, 10):  # Pinta linhas verticais
        pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))

    #Pontuação do jogo
    score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 - 120, 10)
    screen.blit(score_font, score_rect)

    for pos in snake:
        screen.blit(snake_skin,pos)

    pygame.display.update()

while True: #Mensagem de game over no final do jogo
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (300, 200)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    break