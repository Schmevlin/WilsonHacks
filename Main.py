import pygame
import Player
import Net
import math

pygame.init()
width = 1000
height = 1000
size = width, height
white = 255, 255, 255
black = 0, 0, 0
blue = 0, 0, 255
maxDepth = 1000
control = True
won = False

coolFacts = [
    r"in 2013 over 90 million pounds of fish were caught",
    r"About 38.5 million tonnes of bycatch results from current preferred fishing practice each year",
    r"Over just 40 years there has been a decrease recorded in marine species of 39%",
    r"Almost 30% of fish stocks commercially fished are over-fished",
    r"In the North East Atlantic and nearby seas, 39% of fish stocks are classified as overfished. In the Mediterranean Sea and the Black Sea there is sufficient data for 85 stocks, which shows that 88% of these (75) are overfished",
    r"Today, each person eats on average 19.2kg of fish a year – around twice as much as 50 years ago"
]

screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
player = Player.player(width / 2, height * 3 / 4, screen, maxDepth)
nets = []

changeSpriteMaybe = 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        

    keys = pygame.key.get_pressed()

    if (control):
        dists = [0, 0]
        if keys[pygame.K_w]:
            dists = player.move(3)
        elif keys[pygame.K_s]:
            dists = player.move(-3)
    else:
        dists = [0, 9]
        player.moveY(-3)

   
    if keys[pygame.K_d]:
        player.rotate(-math.pi / 24)
    elif keys[pygame.K_a]:
        player.rotate(math.pi / 24)

    if (depth < 0):
        win = True

    blue = 50 + 175 * (1 - (player.depth / maxDepth))
    if (blue > 225):
        blue = 225
        top = True
    else:
        top = False

    screen.fill((0, 0, blue))

    pygame.draw.rect(screen, (230, 230, 255), pygame.Rect(0, 0, width, -player.depth))

    for net in nets:
        if (not net.theChosenNet):
            net.move(dists)
        if (control):
            if (player.touching(net)):
                player.die()
                net.theChosenNet = True
                control = False
                player.x = net.x + (net.actualWidth / 2)
                player.y = net.y + (net.actualHeight / 2)
    
    for net in nets:
        net.drawBack()

    player.draw()
    # player.lookRay()

    for net in nets:
        net.drawFront()

    if (changeSpriteMaybe % 60 == 2 and control):
        nets.append(Net.net(width, height, screen, 3))

    for net in nets:
        if (net.y > height or net.y < -300 or net.x > width or net.x < -300):
            nets.remove(net)

    if(changeSpriteMaybe % 5 == 0):
        player.nextSprite()
    #pygame.draw.rect(screen, black, player.image)
    pygame.display.flip()
    pygame.time.wait(16)
    changeSpriteMaybe += 1 