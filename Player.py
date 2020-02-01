import pygame
import math

class player(pygame.sprite.Sprite):
    sprites = [[
        pygame.image.load("Images/dolphin1.png"),
        pygame.image.load("Images/dolphin2.png"),
        pygame.image.load("Images/dolphin3.png"),
        pygame.image.load("Images/dolphin4.png"),
        pygame.image.load("Images/dolphin5.png"),
        pygame.image.load("Images/dolphin6.png")
    ],
    [
        pygame.image.load("Images/dolphin1oof.png"),
        pygame.image.load("Images/dolphin2oof.png"),
        pygame.image.load("Images/dolphin3oof.png"),
        pygame.image.load("Images/dolphin4oof.png"),
        pygame.image.load("Images/dolphin5oof.png"),
        pygame.image.load("Images/dolphin6oof.png")
    ]]
    dead = 0
    curSprite = 0
    degrees = 0
    dist = math.sqrt((200 / 2)**2 + (100 / 2)**2)
    width = 200
    height = 100
    depth = 1000

    def __init__(self, x, y, screen, depth):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.sprites[self.dead][self.curSprite]
        self.screen = screen
        self.depth = depth
        self.x, self.y = x, y
        self.updateRect()
    
    def draw(self):
        m_screen = self.screen
        m_screen.blit(pygame.transform.rotate(self.image, self.toDegrees(self.degrees)), [self.actualX(), self.actualY()])
        # print(self.degrees)

    def move(self, dist):
        # self.x += dist * math.cos(-self.degrees)
        # self.y += dist * math.sin(-self.degrees)
        self.updateRect()
        self.depth += dist * math.sin(-self.degrees)
        return [dist * math.cos(-self.degrees), dist * math.sin(-self.degrees)]

    def rotate(self, degrees):
        self.degrees += degrees
        self.degrees %= (math.pi * 2)

    def nextSprite(self):
        self.curSprite += 1
        self.curSprite %= 5
        self.image = self.sprites[self.dead][self.curSprite]

    def actualX(self):
        return self.x - (self.width / 2)

    def actualY(self):
        return self.y - (self.height / 2)

    def toRadians(self, angle):
        return angle * (math.pi / 180)

    def toDegrees(self, angle):
        return angle * (180 / math.pi)

    def lookRay(self):
        pygame.draw.line(self.screen, (0,0,0), (self.x, self.y), (self.x + 150*math.cos(-self.degrees), self.y + 150*math.sin(-self.degrees)))

    def updateRect(self):
        self.rect = pygame.Rect(self.actualX(), self.actualY(), self.width, self.height)

    def touching(self, net):
        if self.x > net.x and self.x < net.x + net.actualWidth and self.y > net.y and self.y < net.y + net.actualHeight:
            return True
        else:
            return False
    

    
    def moveY(self, dist):
        self.updateRect()
        self.depth -= dist
    def die(self):
        self.dead = 1
