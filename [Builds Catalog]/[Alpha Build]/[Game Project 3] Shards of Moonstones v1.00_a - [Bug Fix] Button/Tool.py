import pygame
import pygame_textinput
from Ressources import *
from Balance import *
font = pygame.font.SysFont(None, 25)

# Game Tools Development   
# Main Tools
class GameState:
    def __init__(self, name):
        self.textinput = pygame_textinput.TextInput()
        self.Text_Line_Left     = ["", "", "", "", "", "", "", ""]
        self.Text_Line_Right    = ["", "", "", "", "", "", "", ""]
        self.Text_Order         = 1

        self.Event = [False,False,False,False,False,False]
        self.Fight_Event = [False,False,False,False,False,False]
        self.State = ""

        self.Game_Progress = ""
        self.Turn_Count = 0
GameStateIG = GameState("GameState")

def GameStateReset(Left,Right):
    if Left == True:
        GameStateIG.Text_Line_Left = ["", "", "", "", "", "", "", ""]
    if Right == True:
        GameStateIG.Text_Line_Right = ["", "", "", "", "", "", "", ""]


def GameEventReset():
    GameStateIG.Text_Line_Left = ["", "", "", "", "", "", "", ""]
    GameStateIG.Text_Line_Right = ["", "", "", "", "", "", "", ""]
    GameStateIG.Event = [False,False,False,False,False,False]
    GameStateIG.Fight_Event = [False,False,False,False,False,False]
    GameStateIG.State = ""

    
def Button(msg,x,y,w,h,ic,ac,Text_Type,action=None):
    # msg : Message / ic : Inactive Color / ac : Active Color
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Button Box - Active Color
    if x < mouse[0] < x+w and y < mouse[1] < y+h :
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        # Action
        if click[0] ==1 and action != None:
            action()

    # Button Box - Inactive Color
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))


    textSurf, textRect = Text_Type(msg, font)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)

    

def Text_Input(events):
    # Text Input
    if GameStateIG.textinput.update(events):
        GameStateIG.Text_Line_Left[0] = GameStateIG.textinput.get_text()
        GameStateIG.Text_Order += 1
                
        #Reset Text Input
        GameStateIG.textinput = pygame_textinput.TextInput()

# INTRO CHARACTER NAME
    if GameStateIG.State == "Character Name":         
        # Display
        pygame.draw.rect(gameDisplay, black, [295, 395, 210, 40])
        pygame.draw.rect(gameDisplay, game_ui_color, [300, 400, 200, 30])
        gameDisplay.blit(GameStateIG.textinput.get_surface(), (305, 405))


