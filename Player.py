import pygame

class player(pygame.sprite.Sprite):
    sprites = [
        pygame.image.load("dolphin1.png"),
        pygame.image.load("dolphin2.png"),
        pygame.image.load("dolphin3.png"),
        pygame.image.load("dolphin4.png"),
        pygame.image.load("dolphin5.png"),
        pygame.image.load("dolphin6.png")
    ]
    curSprite = 0

    def __init__(self, width, height, x, y, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.sprites[self.curSprite]
        self.screen = screen
        self.x, self.y = x, y
        self.width, self.height = width, height
    
    def draw(self):
        m_screen = self.screen
        m_screen.blit(self.image, [self.x, self.y])

    def move(self, x, y):
        self.x += x
        self.y += y

    def rotate(self, degrees):
        pygame.transform.rotate(self.image, degrees)

    def nextSprite(self):
        self.curSprite += 1
        self.curSprite %= 5
        self.image = self.sprites[self.curSprite]