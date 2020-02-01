import pygame
import Player
import Net
import random
import math
import Bubble
import Explosion

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Arial', 30)

width = 1000
height = 1000
size = width, height
white = 255, 255, 255
black = 0, 0, 0
blue = 0, 0, 255
maxDepth = 2000
done = False
control = True
won = False
boat = pygame.image.load("Images/boat.png")
boatX = width / 4
endCondition = 0
actualWon = False

coolFacts = [
    r"In 2013 over 90 million pounds of fish were caught",
    r"About 38.5 million tonnes of bycatch results from current preferred fishing practice each year",
    r"Over just 40 years there has been a decrease recorded in marine species of 39%",
    r"Almost 30% of fish stocks commercially fished are over-fished",
    r"In the North East Atlantic and nearby seas, 39% of fish stocks are classified as overfished. In the Mediterranean Sea and the Black Sea there is sufficient data for 85 stocks, which shows that 88% of these (75) are overfished",
    r"Today, each person eats on average 19.2kg of fish a year – around twice as much as 50 years ago"
]

screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
player = Player.player(width / 2, height * 2 / 3, screen, maxDepth)
nets = []
bubbles = []
for i in range(0, 20):
    bubbles.append(Bubble.bubble(width, height, screen))

changeSpriteMaybe = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        

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
    if keys[pygame.K_ESCAPE]:
        done = True

    if (player.depth < 0):
        won = True

    blue = 50 + 175 * (1 - (player.depth / maxDepth))
    if (blue > 225):
        blue = 225
        top = True
    else:
        top = False

    if (blue < 10):
        endCondition = 1
        done = True

    screen.fill((0, 0, blue))
    for bubble in bubbles:
        bubble.move(dists)
        bubble.draw()


    pygame.draw.rect(screen, (230, 230, 255), pygame.Rect(0, 0, width, -player.depth))
    if (-player.depth > 0):
        boatX -= dists[0]
        screen.blit(boat, [boatX, -player.depth - 140])

    if (actualWon):
        textsurface = myfont.render('You got your revenge and saved the world!', False, (0, 0, 255))
        screen.blit(textsurface, [100, 100])

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

    if (player.actualX() > boatX and player.actualX() < boatX + 300 and player.actualY() > (-player.depth - 140) and player.actualY() < (-player.depth - 140 + 150)):
        explosion = Explosion.explosion(screen, boatX, -player.depth - 140)
        explosion.explodeP1(boatX, -player.depth - 140)
        boatX = 100000
        explosion.explodeP2(boatX, -player.depth - 140)
        actualWon = True

    for net in nets:
        net.drawFront()

    pygame.draw.rect(screen, black, pygame.Rect(width / 20, (height * 2 / 5) - 50, width / 10, (height / 5) + 50))
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((width / 20) + (width / 100), (height * 2 / 5) + (width / 100) - 50, (width / 10) - (width * 2 / 100), ((height / 5) - 2 * (width / 100)) + 50))
    bottom = (height * 2 / 5) + (width / 100) + (height / 5) - 2 * (width / 100)
    y = height - (bottom - ((height / 5) - 2 * (width / 100)) * (player.depth / (maxDepth + 457)))
    if y < (height * 2 / 5) + (width / 100) - 50:
        y = (height * 2 / 5) + (width / 100) - 50
    pygame.draw.line(screen, (255, 0, 0), ((width / 20) + (width / 100), y), ((width / 20) + (width / 100) + ((width / 10) - (width * 2 / 100)), y))

    if (changeSpriteMaybe % 45 == 0 and control and not won):
        nets.append(Net.net(width, height, screen, 4))

    for net in nets:
        if (net.y > height or net.y < -300 or net.x > width or net.x < -300):
            nets.remove(net)

    for bubble in bubbles:
        if (bubble.y > height or bubble.y < -25 or bubble.x > width or bubble.x < -25):
            bubbles.remove(bubble)
            bubbles.append(Bubble.bubble(width, height, screen))

    if(changeSpriteMaybe % 5 == 0):
        player.nextSprite()
    #pygame.draw.rect(screen, black, player.image)
    pygame.display.flip()
    pygame.time.wait(16)
    changeSpriteMaybe += 1 

# end logic

endMessages = [pygame.image.load("Images/message1.png"),
               pygame.image.load("Images/message2.png"),
               pygame.image.load("Images/message3.png"),
               pygame.image.load("Images/message4.png"),
               pygame.image.load("Images/message5.png"),
               pygame.image.load("Images/message6.png")]

if (endCondition == 0):
    pygame.quit()
if (endCondition == 1):
    screen.blit(endMessages[random.randint(0, 5)], [0, 0])
    pygame.display.flip()
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()