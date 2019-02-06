import pygame
import pygame_textinput
from Ressources import *

font = pygame.font.SysFont(None, 25)

def Game_Load():
    pass 
def Game_Save():
    pass

def Quit_Game():
    pygame.quit()
    quit()



class GameState:
    def __init__(self, name):
        self.textinput = pygame_textinput.TextInput()
        self.Text_Line_Left     = ["", "", "", "", "", "", "", ""]
        self.Text_Line_Right    = ["", "", "", "", "", "", "", ""]
        self.Text_Order         = 1

        self.Cutscene = False
        self.Event = [False,False,False,False,False,False]
        self.Fight_Event = [False,False,False,False,False,False]
        self.State = ""

        self.Game_Progress = 1
        self.Turn_Count = 0
        
        self.Sound = False
        self.Background = "Cutscene"
        
        self.Ennemy = ["","",""]
GameStateIG = GameState("GameState")

def GameStateReset(State):
    if State == "Left":
        GameStateIG.Text_Line_Left = ["", "", "", "", "", "", "", ""]
        
    if State == "Right":
        GameStateIG.Text_Line_Right = ["", "", "", "", "", "", "", ""]
        
    if State == "All":
        GameStateIG.Text_Line_Left = ["", "", "", "", "", "", "", ""]
        GameStateIG.Text_Line_Right = ["", "", "", "", "", "", "", ""]

    if State == "Event":
        GameStateIG.Text_Line_Left = ["", "", "", "", "", "", "", ""]
        GameStateIG.Text_Line_Right = ["", "", "", "", "", "", "", ""]
        GameStateIG.Event = [False,False,False,False,False,False]
        GameStateIG.Fight_Event = [False,False,False,False,False,False]
        GameStateIG.Sound = False
        GameStateIG.Background = 0
        GameStateIG.State = "" 


    if State == "Win":
        GameStateIG.Text_Line_Left = ["", "", "", "", "", "", "", ""]
        GameStateIG.Text_Line_Right = ["", "", "", "", "", "", "", ""]
        GameStateIG.Event = [False,False,False,False,False,False]
        GameStateIG.Fight_Event = [False,False,False,False,False,False]
        GameStateIG.Sound = False
        GameStateIG.Background = 0

    
def Button(msg,x,y,w,h,ic,ac,Text_Type,event,action=None):
    # msg : Message / ic : Inactive Color / ac : Active Color
    Box = pygame.Rect(x,y,w,h)
    mouse = pygame.mouse.get_pos()
    # Active Color
    if Box.collidepoint(mouse):
        pygame.draw.rect(gameDisplay, ac, Box)

        # Action
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if action != None:
                    action()

    # Inactive Color
    else:
        pygame.draw.rect(gameDisplay, ic, Box)
        
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


