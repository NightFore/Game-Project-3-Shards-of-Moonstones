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


############### Debug Zone
def Test():
    with open("0.0.2_Cutscene_Introduction.txt", "r") as f:
        gameExit = False
        while not gameExit:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
                Text_Input(events, f)


class Player:
    def __init__(self, name):
        self.name   = name
PlayerIG = Player("Ellesia")
############### Debug Zone


        
class GameState:
    def __init__(self, name):
        
        self.textinput          = pygame_textinput.TextInput()
        self.Text_Line_Input    = ""
        
        self.Text_File          = open("0.0.0_None.txt", "r")
        self.Text_Line          = ""
        self.Text_Line_Left     = ["","","","","","","","",""]
        self.Text_Line_Right    = ["","","","","","","","",""]
        
        self.Text_Order         = 0
        self.Order_Left         = 0
        self.Order_Right        = 0
        
        self.State = ""
        self.Event          = [False,False,False,False,False,False]
        self.Fight_Event    = [False,False,False,False,False,False]
        self.Win_Results    = False
        
        self.Sound  = False
        self.Music  = False
        self.Background = "Cutscene"
        self.Text_Cutscene = False

        self.Zone_Progress  = 1
        self.Stage_Progress = 1
        self.Turn_Count = 0
        
        self.Player = ["","",""]
        self.Player_Slot    = [False,False,False]
        
        self.Enemy  = ["","",""]
        self.Enemy_Slot     = [False,False,False]
        self.Enemy_Death    = [False,False,False]
        
        self.Experience_Gain = 0
        self.Gold_Gain = 0
GameStateIG = GameState("GameState")


def Game_State_Reset(State):
    if State == "All":
        GameStateIG.Text_Line_Input    = ""
        
        GameStateIG.Text_Line          = ""
        GameStateIG.Text_Line_Left     = ["","","","","","","","",""]
        GameStateIG.Text_Line_Right    = ["","","","","","","","",""]
        
        GameStateIG.Text_Order         = 0
        GameStateIG.Order_Left         = 0
        GameStateIG.Order_Right        = 0
        
        GameStateIG.State = ""
        GameStateIG.Event = [False,False,False,False,False,False]
        GameStateIG.Fight_Event = [False,False,False,False,False,False]
        GameStateIG.Win_Results    = False
        
        GameStateIG.Sound = False
        GameStateIG.Music = False

        GameStateIG.Player = ["","",""]
        GameStateIG.Player_Slot    = [True,False,False]
        
        GameStateIG.Enemy  = ["","",""]
        GameStateIG.Enemy_Slot     = [True,False,False]
        GameStateIG.Enemy_Death    = [False,False,False]
        


    if State == "Event":
        GameStateIG.State = ""
        GameStateIG.Text_Order = 0
        
    if State == "Left":
        GameStateIG.Text_Line_Left = ["","","","","","","","",""]
        GameStateIG.Order_Left  = 1
        
    if State == "Right":
        GameStateIG.Text_Line_Right = ["","","","","","","","",""]
        GameStateIG.Order_Right = 1

    if State == "Text":
        GameStateIG.Text_Line          = ""
        GameStateIG.Text_Line_Left     = ["","","","","","","","",""]
        GameStateIG.Text_Line_Right    = ["","","","","","","","",""]
        
        GameStateIG.Text_Order         = 0
        GameStateIG.Order_Left         = 0
        GameStateIG.Order_Right        = 0


    if State == "Win":
        GameStateIG.Text_Order         = 0
        GameStateIG.Order_Left         = 0
        GameStateIG.Order_Right        = 0
        
        GameStateIG.State = "Win"
        GameStateIG.Event = [False,False,False,False,False,False]
        GameStateIG.Fight_Event = [False,False,False,False,False,False]
        
        GameStateIG.Sound = False
        GameStateIG.Music = False
        GameStateIG.Background = "Cutscene"




        
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




def Text_Input(events, f):
    if GameStateIG.textinput.update(events):
        # Input
        GameStateIG.Text_Line_Input = GameStateIG.textinput.get_text()
        GameStateIG.textinput = pygame_textinput.TextInput()

        # Read
        GameStateIG.Text_Line = f.readline().rstrip('\n').replace("%PlayerIG.name", ("%s" % PlayerIG.name))
        
        if "[L]" in GameStateIG.Text_Line:
            GameStateIG.Order_Left += 1
            if GameStateIG.Order_Left == 7:
                Game_State_Reset("Left")
                
            GameStateIG.Text_Line_Left[GameStateIG.Order_Left]      = GameStateIG.Text_Line.strip("[L]")
            GameStateIG.Text_Line_Left[GameStateIG.Order_Left+1]    = "(-> Press Enter)"
            GameStateIG.Text_Line_Right[GameStateIG.Order_Right+1]  = ""
            print(GameStateIG.Text_Line_Left[GameStateIG.Order_Left])

        elif "[R]" in GameStateIG.Text_Line:
            GameStateIG.Order_Right += 1
            if GameStateIG.Order_Right == 7:
                Game_State_Reset("Right")
                
            GameStateIG.Text_Line_Right[GameStateIG.Order_Right]    = GameStateIG.Text_Line.strip("[R]")
            GameStateIG.Text_Line_Left[GameStateIG.Order_Left+1]    = ""
            GameStateIG.Text_Line_Right[GameStateIG.Order_Right+1]  = "(-> Press Enter)"
            print(GameStateIG.Text_Line_Right[GameStateIG.Order_Right])
        GameStateIG.Text_Order += 1

# INTRO CHARACTER NAME
    if GameStateIG.State == "Character Name":
        
        pygame.draw.rect(gameDisplay, black, [295, 395, 210, 40])
        pygame.draw.rect(gameDisplay, game_ui_color, [300, 400, 200, 30])
        gameDisplay.blit(GameStateIG.textinput.get_surface(), (305, 405))
