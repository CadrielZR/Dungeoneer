import pygame
import random
from enemies import Slime

pygame.init()

#Screen settings
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Dungeoneer")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('playerTemp.gif')
playerX = 350
playerY = 300
playerX_change = 0
playerY_change = 0

def player(x,y):
    screen.blit(playerImg,(x,y))

#enemies
all_slimes = pygame.sprite.Group()
slime_changeX = 0.3
slime_changeY = 0.3


for i in range(3):
    new_x = random.randrange(0, WINDOW_WIDTH)
    new_y = random.randrange(0, WINDOW_HEIGHT)
    all_slimes.add(Slime(new_x, new_y))
#Game Loop
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                playerY_change = 0.2
            if event.key == pygame.K_w:
                playerY_change = -0.2

            if event.key == pygame.K_d:
                playerX_change = 0.2
            if event.key == pygame.K_a:
                playerX_change = -0.2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s or event.key == pygame.K_w:
                playerY_change = 0
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0

    all_slimes.update()

    playerY += playerY_change
    playerX += playerX_change

    # Alterar de acordo com o tamanho do mapa
    if playerX <= 0:
        playerX = 0
    elif playerX >= 760:
        playerX = 750
    elif playerY <= 0:
        playerY = 0
    elif playerY >= 600:
        playerY = 600

    new_y += slime_changeY
    new_x += slime_changeX

    if slime_changeX <= 0:
        slime_changeX = 0
    elif slime_changeX >= 760:
        slime_changeX = 750
    elif slime_changeY <= 0:
        slime_changeY = 0
    elif slime_changeY >= 600:
        slime_changeY = 600

    player(playerX,playerY)
    all_slimes.draw(screen)
    pygame.display.update()