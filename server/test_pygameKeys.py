import pygame
import test_cameraControl as cc

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('A bit Racey')

clock = pygame.time.Clock()

pan = ''
tilt=''
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                print("Hey, you pressed the key, K_DOWN")
                tilt='DOWN'              
            if event.key == pygame.K_UP:
                print("Hey, you pressed the key, K_UP")
                tilt='UP'
            if event.key == pygame.K_RIGHT:
                print("Hey, you pressed the key, K_RIGHT")
                pan='RIGHT'
            if event.key == pygame.K_LEFT:
                print("Hey, you pressed the key, K_LEFT")
                pan='LEFT'
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                tilt=''              
            if event.key == pygame.K_UP:
                tilt=''
            if event.key == pygame.K_RIGHT:
                pan=''
            if event.key == pygame.K_LEFT:
                pan=''

        #print(event)

    if tilt=='UP':
        cc.moveUp()
    elif tilt=='DOWN':
        cc.moveDown()  

    if pan=='RIGHT':
        cc.moveRigth()
    elif pan=='LEFT':
        cc.moveLeft()

    pygame.display.update()
    clock.tick(30)
pygame.quit()