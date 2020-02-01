import pygame
import Player
import math

pygame.init()
width = 600
height = 600
size = width, height
white = 255, 255, 255
black = 0, 0, 0
blue = 0, 0, 255

screen = pygame.display.set_mode(size)
player = Player.player(300, 300, screen)

changeSpriteMaybe = 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player.move(-3)
    if keys[pygame.K_s]:
        player.move(3)
    if keys[pygame.K_d]:
        player.rotate(-math.pi / 24)
    if keys[pygame.K_a]:
        player.rotate(math.pi / 24)

    screen.fill(blue)

    player.draw()

    if(changeSpriteMaybe % 5 == 0):
        player.nextSprite()
    #pygame.draw.rect(screen, black, player.image)
    pygame.display.flip()
    pygame.time.wait(16)
    changeSpriteMaybe  += 1 