import pygame

class player(pygame.sprite.Sprite):

    def __init__(self, width, height, x, y, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Rect(x, y, width, height)
        self.screen = screen
        self.x, self.y = x, y
    
    def draw(self):
        pygame.draw.rect(self.screen, (0, 0, 0), self.image)

    def move(self, x, y):
        self.x += x
        self.y += y