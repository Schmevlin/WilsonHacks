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
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.key.K_w:
                player.move(1, 0)
            if event.key == K_S:
                player.move(-1, 0)
            if event.key == K_D:
                player.move(0, 1)
            if event.key == K_A:
                player.move(0, -1)

    screen.fill(white)

    player.draw()
    #pygame.draw.rect(screen, black, player.image)
    pygame.display.flip()