from Tool import *
from Text_ui import *

def Level_Fight():
    global Ennemy_1
    global Ennemy_2
    global Ennemy_3
    
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
            Ennemy_1 = WolfIG
            Game_ui()
