import pygame
import time

# Load/Save Game
import pickle


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
green = (0,180,80)
red = (200,0,0)

black = (0,0,0)
bright_green = (96,255,96)
bright_red = (255,96,96)
game_ui_color = (245,218,168)
text_ui_color = (104,187,230)
text_action_color = black #Temporary

sky_color = (153,217,234)
ground_color = (34,177,76)

    # Game Files
Title_Screen_Background = pygame.image.load("Data\Background\Title_Screen_Background.png")



# Game Core
def Title_Screen():
    gameDisplay.blit(Title_Screen_Background, (0,0))
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                        # Width 50%     - Box Width / 2     # Height            - Box Height /2      800/8 = 100      600 / 12 = 50
        Button("Start", display_width/2 - display_width/16, display_height*0.45 - display_height/24, display_width/8, display_height/12, green, red, Text_Title_Selection, Game_Intro)
        Button("Load",  display_width/2 - display_width/16, display_height*0.60 - display_height/24, display_width/8, display_height/12, green, red, Text_Title_Selection, Game_Load)
        Button("Exit",  display_width/2 - display_width/16, display_height*0.75 - display_height/24, display_width/8, display_height/12, green, red, Text_Title_Selection, Quit_Game)

        pygame.display.update()

    
def Game_Save():
    with open("savefile", "wb") as f:
        pickle.dump(PlayerIG, f)

def Game_Load():
    if os.path.exists("savefile") == True:
        with open("savefile", "rb") as f:
            global PlayerIG
            PlayerIG = pickle.load(f)
        Main_Menu()
    else:
        Title_Screen()

def Quit_Game():
    pygame.quit()
    quit()



# Game Tools Development
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

def Text_Display(msg, x, y, color):
    Text_Screen = font.render(msg, True, color)
    gameDisplay.blit(Text_Screen, x, y)

def Text_Title_Selection():
    pass

# Game Build
def Game_Intro():
    pass

Title_Screen()
