import pygame
import pygame_textinput

pygame.init()
pygame.display.set_caption("Shards of Moonstones")
clock = pygame.time.Clock()

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))

Text_Line = ["","","","","","","","",""]
Line = 0
textinput = pygame_textinput.TextInput()
def Test():
    with open("0.0.0_Cutscene_Introduction.txt", "r") as f:
        gameExit = False
        while not gameExit:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
                Text_Input(events, f)
                if GameStateIG.Text_Order == 5:
                    a = Text_Line[4]
                    print(Text_Line)

def Text_Input(events, f):
    # Text Input
    if GameStateIG.textinput.update(events):
        Text_Line[GameStateIG.Text_Order] = f.readline().rstrip('\n')
        print(Text_Line[GameStateIG.Text_Order])

        GameStateIG.Text_Order += 1


        
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
        
        self.Player = ["","",""]
        self.Enemy  = ["","",""]

        self.Player_Slot    = [True,False,False]
        self.Enemy_Slot     = [True,False,False]
        
        self.Experience_Gain = 0
        self.Gold_Gain = 0
GameStateIG = GameState("GameState")

Test()
