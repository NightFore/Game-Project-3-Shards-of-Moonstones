import pygame
from buttona import *

pygame.init()
width, height = (200,300)
gameDisplay = pygame.display.set_mode((width, height))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (30, 30, 30)
FONT = pygame.font.Font("freesansbold.ttf", 50)
green = (0,180,80)
red = (200,0,0)


def loop():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            omg(0,100,200,200,green,red,event,Yolo)


loop()
pygame.quit()
