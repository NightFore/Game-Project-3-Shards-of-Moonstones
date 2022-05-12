import pygame
from Ressources import *
font = pygame.font.SysFont(None, 25)

# Text
def Text_Display(msg, x, y, Text_Type):
    textSurf, textRect = Text_Type(msg, font)
    textRect.center = (x, y)
    gameDisplay.blit(textSurf, textRect)

# Font
def Text_Title_Screen(msg, font):
    font = pygame.font.SysFont(None, 75)
    textSurface = font.render(msg, True, (210,100,240))
    return textSurface, textSurface.get_rect()
    
def Text_Title_Selection(msg, font):
    font = pygame.font.SysFont(None, 30)
    textSurface = font.render(msg, True, (black))
    return textSurface, textSurface.get_rect()

def Text_Introduction(msg, font):
    font = pygame.font.SysFont(None, 75)
    textSurface = font.render(msg, True, (Introduction_Color))
    return textSurface, textSurface.get_rect()

def Text_ui(msg, x, y):
    font = pygame.font.SysFont("comicsansms", 20)
    Text_Line = font.render(msg, True, Text_ui_Color)
    gameDisplay.blit(Text_Line,  (x,y))

def Text_ui_Screen(msg, x, y):
    font = pygame.font.SysFont("comicsansms", 25)
    Text_Line = font.render(msg, True, Text_ui_Color)
    gameDisplay.blit(Text_Line,  (x,y))

def Text_Fight(msg, x, y):
    font = pygame.font.SysFont(None, 25)
    Text_Line = font.render(msg, True, Text_ui_Color)
    gameDisplay.blit(Text_Line,  (x,y))
