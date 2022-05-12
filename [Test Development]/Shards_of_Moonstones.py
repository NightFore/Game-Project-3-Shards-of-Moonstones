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
            GameStateIG.event = event
            if event.type == pygame.QUIT:
                Quit_Game()

            # Game Title
            Text_Display("Shards of Moostones", 400, 150, Text_Title_Screen)

            # Commands
            Button("Start", 150, 425, 100, 50, Green, Red, Text_Title_Selection, GameStateIG.event, "", Game_Intro_1)
            Button("Load",  350, 425, 100, 50, Green, Red, Text_Title_Selection, GameStateIG.event, "", Game_Load)
            Button("Exit",  550, 425, 100, 50, Green, Red, Text_Title_Selection, GameStateIG.event, "", Quit_Game)

            pygame.display.update()
            
def Game_Intro_1():
    pygame.mixer.music.load(Serenity)
    pygame.mixer.music.play(-1)
    
    GameStateIG.Text_File = open("0.0.1_Cutscene_Introduction.txt", "r")
    
# Setup
    gameExit = False
    while not gameExit:
        events = pygame.event.get()
        pygame.display.update()
        gameDisplay.blit(Game_ui_Screen, (0,0))
        gameDisplay.blit(Background_Introduction, (0,0))
        Game_Text_Event()
        
# "0.0.1_Cutscene_Introduction.txt"
        if GameStateIG.Event[1] == False :
            Text_Input(events, GameStateIG.Text_File)
            
            if GameStateIG.Text_Order == 4:
                GameStateIG.State = "Character Name"
                
            if GameStateIG.State == "Character Name":
                if GameStateIG.Text_Line_Input != "":
                    PlayerIG = Player(GameStateIG.Text_Line_Input)
                    GameStateIG.Player[0] = PlayerIG

                    GameStateIG.Text_File = open("0.0.2_Cutscene_Introduction.txt", "r")
                    Game_State_Reset("Event")
                    GameStateIG.Event[1] = True

# "0.0.2_Cutscene_Introduction.txt"
        elif GameStateIG.Event[2] == False:
            Text_Input(events, GameStateIG.Text_File)

            if GameStateIG.Text_Order == 18:
                Game_Intro_2()

        for event in events:
            GameStateIG.event = event
            if event.type == pygame.QUIT:
                exit()




def Game_Intro_2():
    pygame.mixer.music.load(Around_a_Campfire)
    pygame.mixer.music.play(-1)

    Game_State_Reset("All")
    GameStateIG.Text_File = open("0.1.1_Cutscene_Introduction_2.txt", "r")

# Setup
    gameExit = False
    while not gameExit:
        events = pygame.event.get()
        pygame.display.update()
        gameDisplay.blit(Game_ui_Screen, (0,0))
        gameDisplay.blit(Background_House, (0,0))
        Game_Text_Event()

# "0.1.1_Cutscene_Introduction.txt"
        if GameStateIG.Event[1] == False:
            Text_Input(events, GameStateIG.Text_File)
            
            if GameStateIG.Text_Order == 0:
                gameDisplay.blit(Game_ui_Screen_Black, (0,0))
                Text_Display("1 Week Later...", display_width/2, display_height*3/8, Text_Introduction)

            if GameStateIG.Text_Order == 3:
                if GameStateIG.Sound == False:
                    Sound_Wolf_Roar.play()
                    GameStateIG.Sound = True

            if GameStateIG.Text_Order == 4:
                GameStateIG.Sound = False

            if GameStateIG.Text_Order == 6:
                if GameStateIG.Sound == False:
                    Sound_Wolf_Roar.play()
                    GameStateIG.Sound = True
                    
            if GameStateIG.Text_Order == 7:
                GameStateIG.State = "Level_Fight"
                GameStateIG.Background = "Level_Fight"
                Main_Menu()


        for event in events:
            GameStateIG.event = event
            if event.type == pygame.QUIT:
                exit()
        

def Main_Menu():
    gameExit = False
    while not gameExit:
        events = pygame.event.get()
        pygame.display.update()
        
        if GameStateIG.Background == "Cutscene":
            gameDisplay.blit(Game_ui_Screen, (0,0))

        Game_Text_Event()
        for event in events:
            GameStateIG.event = event
            if event.type == pygame.QUIT:
                exit()
                
    # Main_Menu
            if GameStateIG.State == "":
                # Background
                if GameStateIG.Zone_Progress == 1:
                    if GameStateIG.Background == "":
                        gameDisplay.blit(Background_Main_Menu_1, (0,0))

                # Menu
                Interface_Main_Menu()
                if GameStateIG.Menu == "Inventory":
                    Inventory()

                if GameStateIG.Menu == "Shop":
                    Shop()
                        


            # Fight
            if GameStateIG.State == "Level_Fight":
                Level_Fight()
                Player_Enemy_Check()
                Action_Point()

                if GameStateIG.Attack_Choice == True:
                    Attack_Choice()
                Win_Condition()

            # Win
            elif GameStateIG.State == "Win":
                Win(events)

            # Results
            elif GameStateIG.State == "Result":
                Game_State_Reset("Text")
                GameStateIG.Background = "Result"
                gameDisplay.blit(Interface_Results, (0,0))
                Battle_Result()


def Player_Enemy_Check():
    if GameStateIG.Player[0] != "":
        GameStateIG.Player_Slot[0] = True
        
    if GameStateIG.Player[1] != "":
        GameStateIG.Player_Slot[1] = True
        
    if GameStateIG.Player[2] != "":
        GameStateIG.Player_Slot[2] = True
        
    if GameStateIG.Enemy[0] != "" and GameStateIG.Enemy[0] != NoMonsterIG:
        GameStateIG.Enemy_Slot[0] = True
        
    if GameStateIG.Enemy[1] != "" and GameStateIG.Enemy[1] != NoMonsterIG:
        GameStateIG.Enemy_Slot[1] = True
        
    if GameStateIG.Enemy[2] != "" and GameStateIG.Enemy[2] != NoMonsterIG:
        GameStateIG.Enemy_Slot[2] = True
        

def Win_Condition():
    if GameStateIG.Enemy[0].Health <= 0:
        GameStateIG.Enemy_Death[0] = True
        
    if GameStateIG.Enemy[1].Health <= 0:
        GameStateIG.Enemy_Death[1] = True
        
    if GameStateIG.Enemy[2].Health <= 0:
        GameStateIG.Enemy_Death[2] = True

    if GameStateIG.Enemy_Death == [True,True,True]:
        Game_State_Reset("Win")

def Win(events):
    if GameStateIG.Zone_Progress == 1:
        if GameStateIG.Music == False:
            pygame.mixer.music.load(Finally_Some_Rest)
            pygame.mixer.music.play(-1)
            GameStateIG.Music = True
        
        if GameStateIG.Stage_Progress == 0:
            if GameStateIG.Text_Cutscene == False:
                GameStateIG.Text_File = open("1.0.0_Victory.txt", "r")
                GameStateIG.Text_Cutscene = True
                
            if GameStateIG.Text_Cutscene == True:
                Text_Input(events, GameStateIG.Text_File)

            if GameStateIG.Text_Order == 5:
                GameStateIG.State = "Result"


GameStateIG.Player = [PlayerIG, IrisIG, GyreiIG]
Main_Menu()
