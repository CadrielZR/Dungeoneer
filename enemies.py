import pygame
class Slime (pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('slime.gif')
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

class Slime_Tar (pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('slime tar.gif')
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

class Skeleton (pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('skeleton idle.gif')
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

class Skeleton_Hat (pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('skeleton idle hat.gif')
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

class Skeleton_Armor (pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('skeleton idle armor.gif')
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)