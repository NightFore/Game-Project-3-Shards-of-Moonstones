from Tool import *
from Ressources import *
from Balance import *
from Game_ui import *

def Level_Fight():
    # Level 0
    if GameStateIG.Game_Progress == 0:

        # List of Ennemies :
        GameStateIG.Ennemy[0] = WolfIG
            
        # OST & Reset
        if GameStateIG.Fight_Event[0] == False:
            GameStateReset("All")
            pygame.mixer.music.load(Village_Under_Attack)
            pygame.mixer.music.play(-1)
            GameStateIG.Fight_Event[0] = True


        # Level Introduction
        if GameStateIG.Text_Order == 1:
            GameStateIG.Text_Line_Left[1] = "Wow! What was that?"
            GameStateIG.Text_Line_Left[2] = "-> (Press Enter)"

        if GameStateIG.Text_Order == 2:
            GameStateIG.Text_Line_Left[2] = "Wasn't that a Wolf just now?"
            GameStateIG.Text_Line_Left[3] = "-> (Press Enter)"
            Sound_Wolf_Roar.play()

        if GameStateIG.Text_Order == 3:
            GameStateIG.Text_Line_Left[3] = "Here he is!"
            GameStateIG.Text_Line_Left[4] = "-> (Press Enter)"

        if GameStateIG.Text_Order == 4:
            GameStateIG.Text_Line_Left[4] = "I'll defeat him for now."
            GameStateIG.Text_Line_Left[5] = "-> (Press Enter)"

        if GameStateIG.Text_Order == 5:            
            GameStateReset("All")
            GameStateIG.Fight_Event[1] = True
