import pygame
import time


# Game Settings
    # Game Setup
pygame.init()

    # Game Size Screen
gameDisplay = pygame.display.set_mode((display_width, display_height))
display_width = 800
display_height = 600

    # Game Title
pygame.display.set_caption("Shards of Moonstones")

    # Game Clock
clock = pygame.time.Clock()



#Ressources

black = (0,0,0)
green = (0,176,80)
bright_green = (96,255,96)
red = (200,0,0)
bright_red = (255,96,96)
game_ui_color = (245,218,168)
text_ui_color = (104,187,230)
text_action_color = black #Temporary

sky_color = (153,217,234)
ground_color = (34,177,76)


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
def Text_Display():
    pass

Title_Screen()
