import pygame

pygame.init()

#Screen settings
screen = pygame.display.set_mode((800,600))
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


    playerY += playerY_change
    playerX += playerX_change
    player(playerX,playerY)
    pygame.display.update()