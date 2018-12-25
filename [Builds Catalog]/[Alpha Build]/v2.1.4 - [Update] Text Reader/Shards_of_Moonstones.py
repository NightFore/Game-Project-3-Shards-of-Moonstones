import os
import pygame
import time
import pickle           # Load/Save Game

from Balance        import *
from Level_Design   import *
from Ressources     import *
from Text_Font      import *
from Tool           import *
from Game_ui        import *

pygame.init()
pygame.display.set_caption("Shards of Moonstones")
clock = pygame.time.Clock()

def Title_Screen():
    # Game Setup
    global PlayerIG
    
    # OST
    pygame.mixer.music.load(Undisturbed_Place)
    pygame.mixer.music.play(-1)

    # Background
    gameDisplay.blit(Title_Screen_Background, (0,0))

    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit_Game()

            # Game Title
            Text_Display("Shards of Moostones", 400, 150, Text_Title_Screen)

            # Commands
            Button("Start", 150, 425, 100, 50, green, red, Text_Title_Selection, event, Game_Intro_1)
            Button("Load",  350, 425, 100, 50, green, red, Text_Title_Selection, event, Game_Load)
            Button("Exit",  550, 425, 100, 50, green, red, Text_Title_Selection, event, Quit_Game)

            pygame.display.update()
            
def Game_Intro_1():
    pygame.mixer.music.load(Serenity)
    pygame.mixer.music.play(-1)
    
    f = open("0.0.0_Cutscene_Introduction.txt", "r")
    
    gameExit = False
    while not gameExit:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
                
        pygame.display.update()
        gameDisplay.blit(Game_ui_Screen, (0,0))
        gameDisplay.blit(Background_Introduction, (0,0))
        Game_Text_Event()
        print(GameStateIG.Text_Order)

    # Game Intro 1 :
        # "0.0.0_Cutscene_Introduction.txt"
        if GameStateIG.Event[1] == False :
            Text_Input(events, f)
            
            if GameStateIG.Text_Order == 5:
                GameStateIG.State = "Character Name"
                
            if GameStateIG.State == "Character Name":
                if GameStateIG.Text_Line_Input != "":
                    PlayerIG = Player(GameStateIG.Text_Line_Input)

                    f = open("0.0.1_Cutscene_Introduction.txt", "r")
                    Game_State_Reset("Introduction")
                    GameStateIG.Event[1] = True

        # "0.0.1_Cutscene_Introduction.txt"
        elif GameStateIG.Event[2] == False:
            Text_Input(events,f)




def Game_Intro_2():
    # OST
    pygame.mixer.music.load(Around_a_Campfire)
    pygame.mixer.music.play(-1)

    # Reset
    Game_State_Reset("Event")

    # Cutscene
    GameStateIG.Text_Order = 0
    
    gameExit = False
    while not gameExit:
        events = pygame.event.get()
        pygame.display.update()

        # Background
        gameDisplay.blit(Game_ui_Screen, (0,0))
        gameDisplay.blit(Background_House, (0,0))
        
        Game_Text_Event()
        Text_Input(events)
        
        # Game Intro 2 :
        if GameStateIG.Event[1] == False:
            # Cutscene
            if GameStateIG.Text_Order == 0:
                gameDisplay.blit(Game_ui_Screen_Black, (0,0))
                Text_Display("1 Week Later...", display_width/2, display_height*3/8, Text_Introduction)
                
            if GameStateIG.Text_Order == 1:
                GameStateIG.Text_Line_Left[1] = "Hm... Huh... What's happening?"
                GameStateIG.Text_Line_Left[2] = "-> (Press Enter)"
                
            if GameStateIG.Text_Order == 2:
                GameStateIG.Text_Line_Left[2] = "It's been noisy for a while now."
                GameStateIG.Text_Line_Left[3] = "-> (Press Enter)"
                
            if GameStateIG.Text_Order == 3:
                GameStateIG.Text_Line_Left[3] = "I probably should go check out"
                GameStateIG.Text_Line_Left[4] = "what's happening outside."
                GameStateIG.Text_Line_Left[5] = "-> (Press Enter)"

                # Sound
                if GameStateIG.Event[2] == False:
                    Sound_Wolf_Roar.play()
                    GameStateIG.Event[2] = True
                    
            if GameStateIG.Text_Order == 4:
                GameStateIG.Event[1] = True
                GameStateIG.Event[3] = True

        for event in events:
            if event.type == pygame.QUIT:
                exit()
                
            if GameStateIG.Event[3] == True :
                GameStateIG.State = "Fight"
                GameStateIG.Background = "Cutscene"
                Main_Level()
        

def Main_Level():
    gameExit = False
    while not gameExit:
        events = pygame.event.get()
        pygame.display.update()
        
        # Background
        if GameStateIG.Background == "Cutscene":
            gameDisplay.blit(Game_ui_Screen, (0,0))
            
        Game_Text_Event()
        Text_Input(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()

            # Main_Level
            if GameStateIG.State == "":
                pass


            # Fight
            if GameStateIG.State == "Fight":
                Level_Fight()

            # Start Fight
            if GameStateIG.Background == "Fight":
                gameDisplay.blit(Interface_Fight, (0,0))
                Game_ui_Fight(event)

            # Win
            elif GameStateIG.State == "Win":
                Win()

            # Results
            elif GameStateIG.State == "Results":
                Game_State_Reset("All")
                GameStateIG.Background = "Results"
                gameDisplay.blit(Interface_Results, (0,0))
                Game_ui_Results(event)
                
            
Title_Screen()
