import pygame

class explosion(pygame.sprite.Sprite):
    frames = [pygame.image.load("ExplosionGif/frame_00_delay-0.06s.gif"), 
              pygame.image.load("ExplosionGif/frame_01_delay-0.06s.gif"),
              pygame.image.load("ExplosionGif/frame_02_delay-0.06s.gif"),
              pygame.image.load("ExplosionGif/frame_03_delay-0.06s.gif"),
              pygame.image.load("ExplosionGif/frame_04_delay-0.06s.gif"),
              pygame.image.load("ExplosionGif/frame_05_delay-0.06s.gif"),
              pygame.image.load("ExplosionGif/frame_06_delay-0.06s.gif"),
              pygame.image.load("ExplosionGif/frame_07_delay-0.04s.gif"),
              pygame.image.load("ExplosionGif/frame_08_delay-0.04s.gif"),
              pygame.image.load("ExplosionGif/frame_09_delay-0.04s.gif"),
              pygame.image.load("ExplosionGif/frame_10_delay-0.04s.gif"),
              pygame.image.load("ExplosionGif/frame_11_delay-0.04s.gif"),
              pygame.image.load("ExplosionGif/frame_12_delay-0.04s.gif"),
              pygame.image.load("ExplosionGif/frame_13_delay-0.04s.gif"),
              pygame.image.load("ExplosionGif/frame_14_delay-0.04s.gif"),
              pygame.image.load("ExplosionGif/frame_15_delay-0.04s.gif"),
              pygame.image.load("ExplosionGif/frame_16_delay-0.04s.gif"),
              pygame.image.load("ExplosionGif/frame_17_delay-0.04s.gif"),
              pygame.image.load("ExplosionGif/frame_18_delay-0.04s.gif"),
              pygame.image.load("ExplosionGif/frame_19_delay-0.04s.gif"),
              pygame.image.load("ExplosionGif/frame_20_delay-0.04s.gif"),
              pygame.image.load("ExplosionGif/frame_21_delay-0.04s.gif"),
              pygame.image.load("ExplosionGif/frame_22_delay-0.04s.gif"),
              pygame.image.load("ExplosionGif/frame_23_delay-0.04s.gif"),
              pygame.image.load("ExplosionGif/frame_24_delay-0.04s.gif")]

    x = 0
    y = 0

    def __init__(self, screen, x, y):
        self.screen = screen
        self.x == x
        self.y == y

    def explodeP1(self, x, y):
        for i in range(0, 6):
            self.screen.blit(self.frames[i], [x, y])
            pygame.display.flip()
            pygame.time.delay(12)
    
    def explodeP2(self, x, y):
        for i in range(6, 24):
            self.screen.blit(self.frames[i], [x, y])
            pygame.display.flip()
            pygame.time.delay(8)