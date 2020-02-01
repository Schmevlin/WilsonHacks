import pygame

class explosion(pygame.sprite.Sprite):
    frames = [pygame.image.load("Images/frame_00_delay-0.06s.gif"), 
              pygame.image.load("Images/frame_01_delay-0.06s.gif"),
              pygame.image.load("Images/frame_02_delay-0.06s.gif"),
              pygame.image.load("Images/frame_03_delay-0.06s.gif"),
              pygame.image.load("Images/frame_04_delay-0.06s.gif"),
              pygame.image.load("Images/frame_05_delay-0.06s.gif"),
              pygame.image.load("Images/frame_06_delay-0.06s.gif"),
              pygame.image.load("Images/frame_07_delay-0.04s.gif"),
              pygame.image.load("Images/frame_08_delay-0.04s.gif"),
              pygame.image.load("Images/frame_09_delay-0.04s.gif"),
              pygame.image.load("Images/frame_10_delay-0.04s.gif"),
              pygame.image.load("Images/frame_11_delay-0.04s.gif"),
              pygame.image.load("Images/frame_12_delay-0.04s.gif"),
              pygame.image.load("Images/frame_13_delay-0.04s.gif"),
              pygame.image.load("Images/frame_14_delay-0.04s.gif"),
              pygame.image.load("Images/frame_15_delay-0.04s.gif"),
              pygame.image.load("Images/frame_16_delay-0.04s.gif"),
              pygame.image.load("Images/frame_17_delay-0.04s.gif"),
              pygame.image.load("Images/frame_18_delay-0.04s.gif"),
              pygame.image.load("Images/frame_19_delay-0.04s.gif"),
              pygame.image.load("Images/frame_20_delay-0.04s.gif"),
              pygame.image.load("Images/frame_21_delay-0.04s.gif"),
              pygame.image.load("Images/frame_22_delay-0.04s.gif"),
              pygame.image.load("Images/frame_23_delay-0.04s.gif"),
              pygame.image.load("Images/frame_24_delay-0.04s.gif")]
        
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x == x
        self.y == y