import os
import pygame
import time
import pickle           # Load/Save Game
import pygame_textinput
import random



# Game Settings
    # Game Setup
pygame.init()

    # Game Size Screen
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))

    # Game Title
pygame.display.set_caption("Shards of Moonstones")

    # Game Clock
clock = pygame.time.Clock()

    #Ressources
font = pygame.font.SysFont(None, 25)

black = (0,0,0)
green = (0,180,80)
red = (200,0,0)
Text_ui_Color = black
game_ui_color = (147,169,213)
Introduction_Color = (112,146,190)
Command_Button = (142,207,244)

bright_green = (96,255,96)
bright_red = (255,96,96)
text_action_color = black #Temporary

sky_color = (153,217,234)
ground_color = (34,177,76)

    # Game Files
Title_Screen_Background = pygame.image.load("Data\Background\Title_Screen_Background.png")
Game_ui_Screen = pygame.image.load("Data\Game_ui\Game_ui_Cutscene.png")
Game_ui_Screen_Black = pygame.image.load("Data\Game_ui\Game_ui_Screen_Black.png")
Game_ui_Fight = pygame.image.load("Data\Game_ui\Game_ui_Fight.png")

    # Character / Monster
Ellesia_Img     = pygame.image.load("Data\Sprites\Character_Ellesia.png")
Wolf_Img        = pygame.image.load("Data\Sprites\Monster_Wolf.png")

    # Icon
Ellesia_Icon = pygame.image.load("Data\Icon\Ellesia_Icon.png")
Wolf_Icon = pygame.image.load("Data\Icon\Wolf_Icon.png")

def Quit_Game():
    pygame.quit()
    quit()


class Player:
    def __init__(self, name):
        self.name = name
        
        self.Level = 1
        self.Maxhealth  = 44
        self.Health     = self.Maxhealth
        self.MaxMP      = 20
        self.MP         = self.MaxMP
        self.Strength   = 6
        self.Magic      = 2
        self.Speed      = 4
        self.Defense    = 2
        self.Resistance = 0
PlayerIG = Player("NightFore")

class Wolf:
    def __init__(self, name):
        self.name = name

        self.Level = 1
        self.Maxhealth  = 40 + 6 * (self.Level - 1)
        self.Health     = self.Maxhealth
        self.MaxMP      = 0
        self.MP         = self.MaxMP
        self.Attack     = 4 + 1 * (self.Level - 1)
        self.Speed      = 3 + 1 * (self.Level - 1)
        self.Defense    = 1 + 0.5 * (self.Level - 1)
        self.Resistance = 0 + 0.5 * (self.Level - 1)
WolfIG = Wolf("Wolf")


def loop():
    global event
    global clock
    clock = pygame.time.Clock()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            Button(0,100,200,200,green,red,Yolo)


def Button(x,y,w,h,ic,ac,action=None):
    Box = pygame.Rect(x,y,w,h)
    mouse = pygame.mouse.get_pos()
    
    # Active Color
    if Box.collidepoint(mouse):
        pygame.draw.rect(gameDisplay, ac, Box)

        # Action
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(event.button)
                if action != None:
                    action()

    # Inactive Color
    else:
        pygame.draw.rect(gameDisplay, ic, Box)
    
    # You can pass the center directly to the `get_rect` method.
    pygame.display.update()
def Yolo():
    print("lol")


loop()
pygame.quit()
