import pygame
import random

class bubble(pygame.sprite.Sprite):
    sprite =  pygame.image.load("Images/bubble.png")

    def __init__(self, width, height, screen):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.screen = screen
    
    def draw(self):
        self.screen.blit(self.sprite, [self.x, self.y])

    def move(self, dists):
        self.x += -dists[0] / 2
        self.y += -dists[1] / 2