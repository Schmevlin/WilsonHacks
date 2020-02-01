import pygame
import Player

pygame.init()
width = 600
height = 550
size = width, height
white = 255, 255, 255
black = 0, 0, 0

screen = pygame.display.set_mode(size)
player = Player.player(100, 100, 100, 100, screen)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player.move(0, -1)
    if keys[pygame.K_s]:
        player.move(0, 1)
    if keys[pygame.K_d]:
        player.rotate(.1)
    if keys[pygame.K_a]:
        player.rotate(.1)

    screen.fill(white)

    player.draw()
    player.nextSprite()
    #pygame.draw.rect(screen, black, player.image)
    pygame.display.flip()