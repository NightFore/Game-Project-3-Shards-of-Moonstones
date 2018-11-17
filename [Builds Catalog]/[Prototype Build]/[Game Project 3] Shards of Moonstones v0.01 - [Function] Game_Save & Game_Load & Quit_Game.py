import sys
import os
import random
import pickle
import pygame
import time
import pygame_textinput

#Setup
pygame.init()
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Shards of Moonstones")
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

    
