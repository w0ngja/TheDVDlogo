from ctypes.wintypes import RECT
import sys, pygame

pygame.init()

size = width, height = 800, 600
speed = [2, 2]
black = 0, 0, 0
clock = pygame.time.Clock()
FPS= 60

screen = pygame.display.set_mode(size)
pygame.display.set_caption('The DVD logo')
ball = pygame.image.load("img/dvdlogo.svg")
celebrate = pygame.image.load("img/celebrate.png")
ballrect = ball.get_rect()
celebrate_status = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

    ballrect = ballrect.move(speed)
    
    if (ballrect.left == 0 and ballrect.top == 0) or (ballrect.right == 0 and ballrect.top == 0) or (ballrect.left == 0 and ballrect.bottom == 0) or (ballrect.right == 0 and ballrect.bottom ==0):
        celebrate_status = True

    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]

    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    if celebrate_status == False:
        screen.fill('grey')
    else:
        screen.blit(celebrate, (0,0))

    screen.blit(ball, ballrect)

    clock.tick(FPS)
    pygame.display.flip()