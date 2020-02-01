import pygame
import random

class net(pygame.sprite.Sprite):
    def __init__(self, width, height, screen, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/net.png")
        self.screen = screen
        self.speed = speed
        self.height = height
        self.x = random.randint(0, width)
        self.y = 0
    
    def draw(self):
        m_screen = self.screen
        m_screen.blit(self.image, [self.x, self.y])

    def update(self):
        self.y += self.speed
        if (self.y > (self.height + 100)) :
            del(self)
            return True