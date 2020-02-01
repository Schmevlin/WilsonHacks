import pygame
import random

class net(pygame.sprite.Sprite):
    actualWidth = 200
    actualHeight = 100
    theChosenNet = False

    def __init__(self, width, height, screen, speed):
        pygame.sprite.Sprite.__init__(self)
        self.backImage = pygame.image.load("Images/netBack.png")
        self.frontImage = pygame.image.load("Images/netFront.png")
        self.screen = screen
        self.speed = speed
        self.height = height
        self.x = random.randint(0, width)
        self.y = -100
    
    def drawFront(self):
        m_screen = self.screen
        m_screen.blit(self.frontImage, [self.x, self.y])

    def drawBack(self):
        m_screen = self.screen
        m_screen.blit(self.backImage, [self.x, self.y])

    def move(self, dists):
        self.y += self.speed - dists[1]
        self.x += -dists[0]
    
