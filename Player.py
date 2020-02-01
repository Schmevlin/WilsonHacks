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
    degrees = math.pi / 2
    dist = math.sqrt((200 / 2)**2 + (100 / 2)**2)
    width = 200
    height = 100

    def __init__(self, x, y, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.sprites[self.curSprite]
        self.screen = screen
        self.x, self.y = x, y
    
    def draw(self):
        m_screen = self.screen
<<<<<<< Updated upstream
        m_screen.blit(pygame.transform.rotate(self.image, self.toDegrees(self.degrees) - 90), [self.actualX(), self.actualY()])
        print(self.degrees)
=======
        m_screen.blit(pygame.transform.rotate(self.image, -self.toDegrees(self.degrees)), [self.actualX(), self.actualY()])
>>>>>>> Stashed changes

    def move(self, dist):
        self.x += dist * math.cos(self.degrees + (math.pi / 2))
        self.y += dist * math.sin(self.degrees + (math.pi / 2))

    def rotate(self, degrees):
        self.degrees += degrees
        self.degrees %= (math.pi * 2)

    def nextSprite(self):
        self.curSprite += 1
        self.curSprite %= 5
        self.image = self.sprites[self.curSprite]

    def actualX(self):
        return self.x - (self.width / 2) + (math.sin(math.pi + self.degrees) * self.dist)

    def actualY(self):
        return self.y - (self.height / 2) + (math.cos(math.pi + self.degrees) * self.dist)

    def toRadians(self, angle):
        return angle * (math.pi / 180)

    def toDegrees(self, angle):
        return angle * (180 / math.pi)
    def lookRay(self):
        pygame.draw.line(self.screen, (0,0,0), (self.x, self.y), (self.x + 150*math.cos(self.degrees), self.y + 150*math.sin(self.degrees)))