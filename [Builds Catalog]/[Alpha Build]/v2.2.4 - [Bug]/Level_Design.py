from Tool import *
from Ressources import *
from Balance import *
from Game_ui import *

def Level_Fight(event):
    Player_Enemy_Check()
    
    # Stage 1
    if GameStateIG.Stage_Progress == 1:

        # Stage 1 - Enemy
        GameStateIG.Enemy[0] = WolfIG

        # Stage 1 - Background
        gameDisplay.blit(Interface_Fight, (0,0))

        # Stage 1 - Interface
        Game_ui_Fight(event)

        # Stage 1 - Start
        if GameStateIG.Music == False:
            Game_State_Reset("Text")
            pygame.mixer.music.load(Fierce_Riposte)
            pygame.mixer.music.play(-1)
            GameStateIG.Music = True



    # Stage 2
    if GameStateIG.Stage_Progress == 2:

        # Stage 2 - Enemy :
        GameStateIG.Enemy[0] = WolfIG(2)
        GameStateIG.Enemy[1] = WolfIG(1)



def Player_Enemy_Check():
    if GameStateIG.Player[0] != "":
        GameStateIG.Player_Slot[0] = True
        
    if GameStateIG.Player[1] != "":
        GameStateIG.Player_Slot[1] = True
        
    if GameStateIG.Player[2] != "":
        GameStateIG.Player_Slot[2] = True
        
    if GameStateIG.Enemy[0] != "":
        GameStateIG.Enemy_Slot[0] = True
        
    if GameStateIG.Enemy[1] != "":
        GameStateIG.Enemy_Slot[1] = True
        
    if GameStateIG.Enemy[2] != "":
        GameStateIG.Enemy_Slot[2] = True
        
    
