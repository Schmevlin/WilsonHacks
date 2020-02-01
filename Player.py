import pygame
import math

class player(pygame.sprite.Sprite):
    sprites = [
        pygame.image.load("Images/dolphin1.png"),
        pygame.image.load("Images/dolphin2.png"),
        pygame.image.load("Images/dolphin3.png"),
        pygame.image.load("Images/dolphin4.png"),
        pygame.image.load("Images/dolphin5.png"),
        pygame.image.load("Images/dolphin6.png")
    ]
    curSprite = 0
    degrees = 0

    def __init__(self, width, height, x, y, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.sprites[self.curSprite]
        self.screen = screen
        self.x, self.y = x, y
        self.width, self.height = width, height
    
    def draw(self):
        m_screen = self.screen
        m_screen.blit(pygame.transform.rotate(self.image, self.degrees), [self.x, self.y])

    def move(self, dist):
        self.x += dist * math.cos((self.degrees - 90) * math.pi / 180)
        self.y += dist * math.sin((self.degrees - 90) * math.pi / 180)

    def rotate(self, degrees):
        self.degrees += degrees

    def nextSprite(self):
        self.curSprite += 1
        self.curSprite %= 5
        self.image = self.sprites[self.curSprite]

    def rot_center(self, image, angle):
        rotatedImage = pygame.transform.rotate(image, angle)