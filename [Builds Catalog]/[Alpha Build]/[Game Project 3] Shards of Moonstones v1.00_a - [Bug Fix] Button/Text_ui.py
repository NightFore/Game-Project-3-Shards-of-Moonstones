import pygame
from Ressources import *
from Tool import *
from Level_Design import *
font = pygame.font.SysFont(None, 25)

def Text_Display(msg, x, y, Text_Type):
    textSurf, textRect = Text_Type(msg, font)
    textRect.center = (x, y)
    gameDisplay.blit(textSurf, textRect)
    
def Game_ui():
    # Interface
    Text_ui_Screen("Stage : %i" % GameStateIG.Game_Progress, 15, 5)
    Text_ui_Screen("Turn : %i" % GameStateIG.Game_Progress, 665, 5)

    # Commands
    Button("Attack", 400-48, 450+2, 100-3, 50-5, Command_Button, red, Text_Title_Selection, Attack)
    Button("Magic",  400-48, 500+2, 100-3, 50-5, Command_Button, red, Text_Title_Selection, Magic)
    Button("Guard",  400-48, 550+2, 100-3, 50-5, Command_Button, red, Text_Title_Selection, Guard)

    # Player 1
    gameDisplay.blit(Ellesia_Icon, (10,455))
    gameDisplay.blit(Ellesia_Img, (60, 210))
    Text_Fight("%s" % PlayerIG.name, 60, 465)
    Text_Fight("HP: %i/%i" % (PlayerIG.Health, PlayerIG.Maxhealth), 170, 465)
    Text_Fight("MP: %i/%i" % (PlayerIG.MP, PlayerIG.MaxMP), 260, 465)

    # Ennemy 1
    gameDisplay.blit(Wolf_Icon, (750,455))
    gameDisplay.blit(Wolf_Img, (630, 260))
    Text_Fight("%s" % Ennemy_1.name, 660, 465)
    Text_Fight("HP: %i/%i" % (Ennemy_1.Health, Ennemy_1.Maxhealth), 550, 465)
    Text_Fight("MP: %i/%i" % (Ennemy_1.MP, Ennemy_1.MaxMP), 460, 465)

def Game_Text_Event():
# Left
    # Text
    Text_ui(GameStateIG.Text_Line_Left[1], 10, 450)
    Text_ui(GameStateIG.Text_Line_Left[2], 10, 470)
    Text_ui(GameStateIG.Text_Line_Left[3], 10, 490)
    Text_ui(GameStateIG.Text_Line_Left[4], 10, 510)
    Text_ui(GameStateIG.Text_Line_Left[5], 10, 530)
    Text_ui(GameStateIG.Text_Line_Left[6], 10, 550)
    Text_ui(GameStateIG.Text_Line_Left[7], 10, 570)


# Right
    # Text
    Text_ui(GameStateIG.Text_Line_Right[1], 460, 450)
    Text_ui(GameStateIG.Text_Line_Right[2], 460, 470)
    Text_ui(GameStateIG.Text_Line_Right[3], 460, 490)
    Text_ui(GameStateIG.Text_Line_Right[4], 460, 510)
    Text_ui(GameStateIG.Text_Line_Right[5], 460, 530)
    Text_ui(GameStateIG.Text_Line_Right[6], 460, 550)
    Text_ui(GameStateIG.Text_Line_Right[7], 460, 570)



# Secondary Tools
def Text_Title_Screen(msg, font):
    font = pygame.font.SysFont(None, 75)
    textSurface = font.render(msg, True, (210,100,240))
    return textSurface, textSurface.get_rect()
    
def Text_Title_Selection(msg, font):
    font = pygame.font.SysFont(None, 30)
    textSurface = font.render(msg, True, (black))
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

def Text_Introduction(msg, font):
    font = pygame.font.SysFont(None, 75)
    textSurface = font.render(msg, True, (Introduction_Color))
    return textSurface, textSurface.get_rect()
