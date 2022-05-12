import os
import pygame
import time
import pickle           # Load/Save Game
import pygame_textinput



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

    # Icon
Ellesia_Icon = pygame.image.load("Data\Icon\Ellesia_Icon.png")
    



# Game Core
def Game_Save():
    with open("savefile", "wb") as f:
        pickle.dump(PlayerIG, f)

def Game_Load():
    Game_Intro_2()
    global PlayerIG
##    if os.path.exists("savefile") == True:
##        with open("savefile", "rb") as f:
##            global PlayerIG
##            PlayerIG = pickle.load(f)
##        Main_Menu()
##    else:
##        Title_Screen()

def Quit_Game():
    pygame.quit()
    quit()


class Player:
    def __init__(self, name):
        self.name = name
        
        self.Level = 1
        self.Maxhealth = 44
        self.MaxMP = 20
        self.Health = self.Maxhealth
        self.MP = self.MaxMP
        self.Strength = 6
        self.Magic = 2
        self.Speed = 4
        self.Constitution = 3
        self.Defense = 2
        self.Resistance = 0
PlayerIG = Player("NightFore")

class Wolf:
    def __init__(self, name):
        self.name = name

        self.Level = 1
        self.maxhealth = 40
        self.health = self.maxhealth
        self.attack = 4
        self.speed = 3
        self.defense = 1
        self.resistance = 0
WolfIG = Wolf("Wolf")


# Gameplay    
def Title_Screen():
    pygame.mixer.music.load("Data\OST\Main_Menu.mp3")
    pygame.mixer.music.play(-1)
    
    gameDisplay.blit(Title_Screen_Background, (0,0))
    Text_Display("Shards of Moostones", display_width/2, display_height*0.25, Text_Title_Screen)

    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # Button        # 200/400/600      - Box Width / 2     # Height            - Box Height /2      800/8 = 100      600 / 12 = 50
        Button("Start", display_width*0.25 - display_width/16, display_height*0.75 - display_height/24, display_width/8, display_height/12, green, red, Text_Title_Selection, Game_Intro_1)
        Button("Load",  display_width*0.50 - display_width/16, display_height*0.75 - display_height/24, display_width/8, display_height/12, green, red, Text_Title_Selection, Game_Load)
        Button("Exit",  display_width*0.75 - display_width/16, display_height*0.75 - display_height/24, display_width/8, display_height/12, green, red, Text_Title_Selection, Quit_Game)

        pygame.display.update()

 
def Game_Intro_1():
    pygame.mixer.music.load("Data\OST\Cutscene\Introduction.mp3")
    pygame.mixer.music.play(-1)
    
    gameExit = False
    while not gameExit:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
# Setup
        pygame.display.update()
        gameDisplay.blit(Game_ui_Screen, (0,0))
        Game_Text_Event()
        global PlayerIG
        Text_Input(events)

    # Game Intro 1 :
        # Player Name
        if GameStateIG.Event[1] == False :
            if GameStateIG.Text_Order == 1:
                GameStateIG.Text_Line_Right[1] = "Wake up young child..."
                GameStateIG.Text_Line_Right[2] = "-> (Press Enter)"

            if GameStateIG.Text_Order == 2:
                GameStateIG.Text_Line_Right[2] = ""
                GameStateIG.Text_Line_Left[1] = "Huh...? Where am I?"
                GameStateIG.Text_Line_Left[2] = "-> (Press Enter)"

            if GameStateIG.Text_Order == 3:
                GameStateIG.Text_Line_Left[2] = ""
                GameStateIG.Text_Line_Right[2] = "Tell me your name."
                GameStateIG.Text_Line_Right[3] = "-> (Press Enter)"

            if GameStateIG.Text_Order == 4:
                GameStateIG.Text_Line_Right[3] = "And maybe I can answer you."
                GameStateIG.Text_Line_Right[4] = "-> (Enter your Name)"
                GameStateIG.Text_Order = 1
                GameStateIG.Event[1] = True


        elif GameStateIG.Event[2] == False:
            #Input Box
            GameStateIG.State = "Character Name"
            
            if GameStateIG.Text_Line_Left[0] != "":
                PlayerIG = Player(GameStateIG.Text_Line_Left[0])

                GameStateIG.State = ""
                GameStateIG.Event[2] = True
                GameStateIG.Text_Order = 1

            elif GameStateIG.Text_Order == 2 :
                GameStateIG.Text_Line_Right[4] = "That doesn't seem like a real name!"
                GameStateIG.Text_Line_Right[5] = "-> (Enter your Name)"

            elif GameStateIG.Text_Order == 3 :
                GameStateIG.Text_Line_Right[5] = "Please, tell me your name!"
                GameStateIG.Text_Line_Right[6] = "-> (Enter your Name)"
                
            elif GameStateIG.Text_Order == 4 :
                GameStateIG.Text_Order = 3


        elif GameStateIG.Event[3] == False:
            if GameStateIG.Text_Order == 1:
                GameStateIG.Text_Line_Left[2] = "My name is %s." % PlayerIG.name
                GameStateIG.Text_Line_Left[3] = "-> (Press Enter)"
            
            if GameStateIG.Text_Order == 2:
                GameStateReset(False,True)
                GameStateIG.Text_Line_Left[3] = ""
                GameStateIG.Text_Line_Right[1] = ("I see... You're %s... " % PlayerIG.name)
                GameStateIG.Text_Line_Right[2] = "-> (Press Enter)"
            
            if GameStateIG.Text_Order == 3:
                GameStateIG.Text_Line_Right[2] = ("So that's my new Summon Name.")
                GameStateIG.Text_Line_Right[3] = "-> (Press Enter)"
            
            if GameStateIG.Text_Order == 4:
                GameStateIG.Text_Line_Right[3] = ""
                GameStateIG.Text_Line_Left[3] = "Wh... What do you mean?"
                GameStateIG.Text_Line_Left[4] = "-> (Press Enter)"
            
            if GameStateIG.Text_Order == 5:
                GameStateIG.Text_Line_Left[4] = ""
                GameStateIG.Text_Line_Right[3] = ("It means that I will look after you.")
                GameStateIG.Text_Line_Right[4] = "-> (Press Enter)"
            
            if GameStateIG.Text_Order == 6:
                GameStateIG.Text_Line_Right[4] = ("But you will also have to obey me.")
                GameStateIG.Text_Line_Right[5] = "-> (Press Enter)"
            
            if GameStateIG.Text_Order == 7:
                GameStateIG.Text_Line_Right[5] = ("I hope you won't disappoint me.")
                GameStateIG.Text_Line_Right[6] = "-> (Press Enter)"
            
            if GameStateIG.Text_Order == 8:
                GameStateIG.Event[3] = True
                GameStateIG.Text_Order = 1


        elif GameStateIG.Event[4] == False:
            if GameStateIG.Text_Order == 1:
                GameStateReset(False,True)
                GameStateIG.Text_Line_Right[1] = "I will send you off to accomplish"
                GameStateIG.Text_Line_Right[2] = "a important mission."
                GameStateIG.Text_Line_Right[3] = "-> (Press Enter)"
                
            if GameStateIG.Text_Order == 2:
                GameStateIG.Text_Line_Right[3] = ""
                GameStateIG.Text_Line_Left[4] = "So what is that mission?"
                GameStateIG.Text_Line_Left[5] = "-> (Press Enter)"
                
            if GameStateIG.Text_Order == 3:
                GameStateIG.Text_Line_Left[5] = ""
                GameStateIG.Text_Line_Right[3] = "You don't have to know about it."
                GameStateIG.Text_Line_Right[4] = "-> (Press Enter)"
                
            if GameStateIG.Text_Order == 4:
                GameStateIG.Text_Line_Right[4] = "You will understand when you will"
                GameStateIG.Text_Line_Right[5] = "have to do when you confront her."
                GameStateIG.Text_Line_Right[6] = "-> (Press Enter)"
                
            if GameStateIG.Text_Order == 5:
                GameStateIG.Text_Line_Right[6] = "You're going to fall asleep now."
                GameStateIG.Text_Line_Right[7] = "-> (Press Enter)"
                
            if GameStateIG.Text_Order == 6:
                Game_Intro_2()




def Game_Intro_2():
    pygame.mixer.music.load("Data\OST\Selection_Menu\#1 Around a Campfire.mp3")
    pygame.mixer.music.play(-1)

    GameStateIG.Text_Order = 0
    GameEventReset()

    gameExit = False
    while not gameExit:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
# Setup
        pygame.display.update()
        gameDisplay.blit(Game_ui_Screen, (0,0))
        Game_Text_Event()
        Text_Input(events)


    # Game Intro 2 :
        # Transition
        if GameStateIG.Event[1] == False :
            if GameStateIG.Text_Order == 0:
                gameDisplay.blit(Game_ui_Screen_Black, (0,0))
                Text_Display("1 Week Later...", display_width/2, display_height*3/8, Text_Introduction)
    
            if GameStateIG.Text_Order == 1:
                GameStateIG.Event[1] = True

        # Part 1
        elif GameStateIG.Event[2] == False :
            if GameStateIG.Text_Order == 1:
                GameStateIG.Text_Line_Left[1] = "Hm... Huh... What's happening?"
                GameStateIG.Text_Line_Left[2] = "-> (Press Enter)"
                
            if GameStateIG.Text_Order == 2:
                GameStateIG.Text_Line_Left[2] = "It's been noisy for a while now."
                GameStateIG.Text_Line_Left[3] = "-> (Press Enter)"
                
            if GameStateIG.Text_Order == 3:
                GameStateIG.Text_Line_Left[3] = "I probably should go check out"
                GameStateIG.Text_Line_Left[4] = "What's happening outside."
                GameStateIG.Text_Line_Left[5] = "-> (Press Enter)"

            if GameStateIG.Text_Order == 4:
                GameStateIG.Event[2] = True
                GameStateIG.Text_Order = 1

        # Part 2
        elif GameStateIG.Event[3] == False :
            GameStateIG.Game_Progress = 1
            Level_Fight()
        













# Level Design
def Level_Fight():
    if GameStateIG.Game_Progress == 1:
        # OST
        if GameStateIG.Fight_Event[0] == False:
            GameStateReset(True,True)
            pygame.mixer.music.load("Data\OST\Fight\#1-1 Village_Under_Attack.mp3")
            pygame.mixer.music.play(-1)
            GameStateIG.Fight_Event[0] = True

        elif GameStateIG.Fight_Event[1] == False:
            if GameStateIG.Text_Order == 1:
                GameStateIG.Text_Line_Left[1] = "Wow! What was that?"
                GameStateIG.Text_Line_Left[2] = "-> (Press Enter)"

            if GameStateIG.Text_Order == 2:
                GameStateIG.Text_Line_Left[2] = "Wasn't that a Wolf just now?"
                GameStateIG.Text_Line_Left[3] = "-> (Press Enter)"

            if GameStateIG.Text_Order == 3:
                GameStateIG.Text_Line_Left[3] = "I'll defeat him for now."
                GameStateIG.Text_Line_Left[4] = "-> (Press Enter)"

            if GameStateIG.Text_Order == 4:            
                GameStateReset(True,True)
                GameStateIG.Fight_Event[1] = True

        elif GameStateIG.Fight_Event[2] == False:
            gameDisplay.blit(Game_ui_Fight, (0,0))
            Game_ui()



                

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
    



def Game_ui():
    # Interface
    Text_ui_Screen("Stage : %i" % GameStateIG.Game_Progress, 5, 5)
    
    # Player 1
    gameDisplay.blit(Ellesia_Icon, (10,455))
    Text_Fight("%s" % PlayerIG.name, 60, 465)
    Text_Fight("HP: %i/%i" % (PlayerIG.Health, PlayerIG.Maxhealth), 170, 465)
    Text_Fight("MP: %i/%i" % (PlayerIG.MP, PlayerIG.MaxMP), 260, 465)

    # Ennemy 1
    Text_Fight("%s" % PlayerIG.name, 660, 465)
    Text_Fight("HP: %i/%i" % (PlayerIG.Health, PlayerIG.Maxhealth), 550, 465)
    Text_Fight("MP: %i/%i" % (PlayerIG.MP, PlayerIG.MaxMP), 460, 465)




        
def Text_Display(msg, x, y, Text_Type):
    textSurf, textRect = Text_Type(msg, font)
    textRect.center = (x, y)
    gameDisplay.blit(textSurf, textRect)

    
def Button(msg,x,y,w,h,ic,ac,Text_Type,action=None):
    # msg : Message / ic : Inactive Color / ac : Active Color
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Button Box - Active Color
    if x < mouse[0] < x+w and y < mouse[1] < y+h :
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        # Action
        if click[0] ==1 and action !=None:
            action()

    # Button Box - Inactive Color
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))


    textSurf, textRect = Text_Type(msg, font)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)

    

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
    



def Text_Input(events):
    # Text Input
    if GameStateIG.textinput.update(events):
        GameStateIG.Text_Line_Left[0] = GameStateIG.textinput.get_text()
        GameStateIG.Text_Order += 1
                
        #Reset Text Input
        GameStateIG.textinput = pygame_textinput.TextInput()

# Rest Text Order => 1
##    if GameStateIG.Text_Order > 7:
##            GameStateIG.Text_Order  = 1

# INTRO CHARACTER NAME
    if GameStateIG.State == "Character Name":         
        # Display
        pygame.draw.rect(gameDisplay, black, [295, 395, 210, 40])
        pygame.draw.rect(gameDisplay, game_ui_color, [300, 400, 200, 30])
        gameDisplay.blit(GameStateIG.textinput.get_surface(), (305, 405))





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
    font = pygame.font.SysFont("comicsansms", 30)
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
    
        
Title_Screen()
