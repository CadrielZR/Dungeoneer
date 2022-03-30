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

def player():
    screen.blit(playerImg,(playerX,playerY))

#Game Loop
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()