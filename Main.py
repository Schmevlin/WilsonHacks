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
        player.rotate(-.5)
    if keys[pygame.K_a]:
        player.rotate(-.1)

    screen.fill(white)

    player.draw()

    if(changeSpriteMaybe % 5 == 0):
        player.nextSprite()
    #pygame.draw.rect(screen, black, player.image)
    pygame.display.flip()
    pygame.time.wait(16)
    changeSpriteMaybe  += 1 