from Tool import *
from Ressources import *
from Balance import *
from Game_ui import *

def Level_Fight():
    # Stage 1
    if GameStateIG.Stage_Progress == 0:

        # Stage 1 - Enemy
        if GameStateIG.Stage_Boot == False:
            GameStateIG.Enemy[0] = Wolf("Wolf 1")
            GameStateIG.Enemy[1] = Wolf("Wolf 2")
            GameStateIG.Enemy[2] = Wolf("Wolf 3")
            
            GameStateIG.Enemy_X = [640,500,640]
            GameStateIG.Enemy_Y = [190,255,320]
            
            GameStateIG.Stage_Boot = True

        # Stage 1 - Background
        gameDisplay.blit(Interface_Fight, (0,0))

        # Stage 1 - Interface
        Game_ui_Fight()

        # Stage 1 - Start
        if GameStateIG.Music == False:
            Game_State_Reset("Text")
            pygame.mixer.music.load(Fierce_Riposte)
            pygame.mixer.music.play(-1)
            GameStateIG.Music = True



    # Stage 2
    if GameStateIG.Stage_Progress == 1:

        # Stage 2 - Enemy :
        GameStateIG.Enemy[0] = WolfIG(2)
        GameStateIG.Enemy[1] = WolfIG(1)
        
    
