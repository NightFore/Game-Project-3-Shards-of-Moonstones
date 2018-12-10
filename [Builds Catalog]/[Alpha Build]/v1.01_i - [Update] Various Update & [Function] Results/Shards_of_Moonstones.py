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
    pygame.mixer.music.load(Wake_Up)
    pygame.mixer.music.play(-1)
    
    gameExit = False
    while not gameExit:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
# Setup
        pygame.display.update()

        #Background
        gameDisplay.blit(Game_ui_Screen, (0,0))
        gameDisplay.blit(Background_Introduction, (0,0))
        
        Game_Text_Event()
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
                GameStateReset("Right")
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
                GameStateReset("Right")
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
    # OST
    pygame.mixer.music.load(Around_a_Campfire)
    pygame.mixer.music.play(-1)

    # Reset
    GameStateReset("Event")

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
                GameStateReset("All")
                GameStateIG.Background = "Results"
                gameDisplay.blit(Interface_Results, (0,0))
                Game_ui_Results(event)
                
            

Title_Screen()
