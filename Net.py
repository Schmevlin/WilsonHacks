import pygame
import random

class net(pygame.sprite.Sprite):
    actualWidth = 200
    actualHeight = 100
    
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

    def move(self, dists):
        self.y += self.speed - dists[1]
        if (self.y > (self.height + 100)) :
            del(self)
            return True
        self.x += -dists[0]
    
