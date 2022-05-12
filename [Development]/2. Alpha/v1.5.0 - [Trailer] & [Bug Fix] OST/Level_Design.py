from Tool import *
from Ressources import *
from Balance import *
from Game_ui import *

def Level_Fight():
    # Stage 1
    if GameStateIG.Game_Progress == 1:

        # Stage 1 - Enemy :
        GameStateIG.Ennemy[0] = WolfIG

        # Stage 1 - Win Condition :
        if GameStateIG.Ennemy[0].Health <= 0:
            GameStateIG.State = "Win"
            GameStateReset("Win")

            pygame.mixer.music.load(Finally_Some_Rest)
            pygame.mixer.music.play(-1)

            GameStateIG.Text_Line_Left[1] = "What was a Monster doing here?"
            GameStateIG.Text_Line_Left[2] = "-> (Press Enter)"

            GameStateIG.Background = "Cutscene"
            GameStateIG.Text_Order = 1


        # Stage 1 - Start
        elif GameStateIG.Fight_Event[0] == False:
            GameStateReset("All")
            
            pygame.mixer.music.load(Fierce_Riposte)
            pygame.mixer.music.play(-1)
            
            GameStateIG.Text_Line_Left[1] = "Wow! What was that?"
            GameStateIG.Text_Line_Left[2] = "-> (Press Enter)"
            GameStateIG.Text_Order = 1
            
            GameStateIG.Fight_Event[0] = True


        # Stage 1 - Introduction
        elif GameStateIG.Fight_Event[1] == False:
            if GameStateIG.Text_Order == 1:
                GameStateIG.Text_Line_Left[1] = "Wow! What was that?"
                GameStateIG.Text_Line_Left[2] = "-> (Press Enter)"

            if GameStateIG.Text_Order == 2:
                GameStateIG.Text_Line_Left[2] = "Wasn't that a Monster just now?"
                GameStateIG.Text_Line_Left[3] = "-> (Press Enter)"

                if GameStateIG.Sound == False:
                    Sound_Wolf_Roar.play()
                    GameStateIG.Sound = True

            if GameStateIG.Text_Order == 3:
                GameStateIG.Sound = False
                GameStateIG.Text_Line_Left[3] = "Here he is!"
                GameStateIG.Text_Line_Left[4] = "-> (Press Enter)"

            if GameStateIG.Text_Order == 4:
                GameStateReset("All")

                # Fight Background
                GameStateIG.Background = "Fight"



    # Stage 2
    if GameStateIG.Game_Progress == 2:

        # Stage 2 - Enemy :
        GameStateIG.Ennemy[0] = WolfIG(2)
        GameStateIG.Ennemy[1] = WolfIG(1)


def Win():
    # Stage 1
    if GameStateIG.Game_Progress == 1:
        if GameStateIG.Text_Order == 1:
            GameStateIG.Text_Line_Left[1] = "What was a Monster doing here?"
            GameStateIG.Text_Line_Left[2] = "-> (Press Enter)"

        if GameStateIG.Text_Order == 2:
            GameStateIG.Text_Line_Left[2] = "Something must've happened to"
            GameStateIG.Text_Line_Left[3] = "the village."
            GameStateIG.Text_Line_Left[4] = "-> (Press Enter)"
            
        if GameStateIG.Text_Order == 3:
            GameStateIG.Text_Line_Left[4] = "I wonder if they are all safe..."
            GameStateIG.Text_Line_Left[5] = "-> (Press Enter)"

        if GameStateIG.Text_Order == 4:
            GameStateIG.Text_Line_Left[5] = "I should prepare myself for a fight."
            GameStateIG.Text_Line_Left[6] = "-> (Press Enter)"

        if GameStateIG.Text_Order == 5:
            GameStateIG.State = "Results"
