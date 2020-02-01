import pygame
pygame.init()
width = 600
height = 550
size = width, height
white = 255, 255, 255

underlyingBanana = pygame.image.load("underlyingBanana.png")
leftBananas = [
    pygame.image.load("leftBanana1.png"),
    pygame.image.load("leftBanana2.png"),
    pygame.image.load("leftBanana3.png"),
    pygame.image.load("leftBanana4.png"),
    pygame.image.load("leftBanana4_5.png"),
    pygame.image.load("leftBanana5.png")
]
rightHitbox = [
    [[370,20],[422,70]],
    [[383,42],[443,90]],
    [[428,122],[487,166]],
    [[462,277],[527,324]],
    [[515,389],[559,447]]
]
leftHitbox = [
    [[315,56],[338,86]],
    [[280,33],[316,54]],
    [[168,27],[187,42]],
    [[85,85],[105,105]],
    [[11, 151],[56,178]],
    [[3,260],[30,285]]
]
rightBananas = [
    pygame.image.load("rightBanana1.png"),
    pygame.image.load("rightBanana2.png"),
    pygame.image.load("rightBanana3.png"),
    pygame.image.load("rightBanana4.png"),
    pygame.image.load("rightBanana5.png")
]
imgRect = underlyingBanana.get_rect()
screen = pygame.display.set_mode(size)

leftState = 0
rightState = 0
leftBananaSelected = False
rightBananaSelected = False

while 1:
    #make the x button work
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    mousePos = [pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]]
    if pygame.mouse.get_pressed()[0] and (leftBananaSelected == rightBananaSelected):
        #select right banana
        if (mousePos[0] > rightHitbox[rightState][0][0] and 
            mousePos[0] < rightHitbox[rightState][1][0] and 
            mousePos[1] > rightHitbox[rightState][0][1] and 
            mousePos[1] < rightHitbox[rightState][1][1]):
            rightBananaSelected = True
        
        #select left banana
        if (mousePos[0] > leftHitbox[leftState][0][0] and 
            mousePos[0] < leftHitbox[leftState][1][0] and 
            mousePos[1] > leftHitbox[leftState][0][1] and 
            mousePos[1] < leftHitbox[leftState][1][1]):
            leftBananaSelected = True
    elif pygame.mouse.get_pressed()[0] == False: 
        rightBananaSelected = False
        leftBananaSelected = False
    #right banana logic
    if rightBananaSelected:
        if mousePos[1] < 58: 
            rightState = 0
        elif mousePos[1] < 105:
            rightState = 1
        elif mousePos[1] < 215:
            rightState = 2
        elif mousePos[1] < 365:
            rightState = 3
        else:
            rightState = 4
    #left banana logic
    if leftBananaSelected:
        if mousePos[1] > 200:
            leftState = 5
        elif mousePos[1] > 135:
            leftState = 4
        elif mousePos[1] > 70:
            leftState = 3
        elif mousePos[0] > 316: 
            leftState = 0
        elif mousePos[0] > 242:
            leftState = 1
        elif mousePos[0] > 142:
            leftState = 2
        elif mousePos[0] > 54:
            leftState = 3
        elif mousePos[0] > 12:
            leftState = 4
        else: 
            leftState = 5

    #the actual drawing of the images    
    screen.fill(white)
    screen.blit(underlyingBanana,imgRect)
    screen.blit(leftBananas[leftState],imgRect)
    screen.blit(rightBananas[rightState], imgRect)
    pygame.display.flip()