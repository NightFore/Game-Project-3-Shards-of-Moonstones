from Text_Font import *
from Tool import *
from Balance import *

def Game_Text_Event():
# Left
    # Text
    Text_ui(GameStateIG.Text_Line_Left[1], 10, 450)
    Text_ui(GameStateIG.Text_Line_Left[2], 10, 470)
    Text_ui(GameStateIG.Text_Line_Left[3], 10, 490)
    Text_ui(GameStateIG.Text_Line_Left[4], 10, 510)
    Text_ui(GameStateIG.Text_Line_Left[5], 10, 530)
    Text_ui(GameStateIG.Text_Line_Left[6], 10, 550)
    Text_ui(GameStateIG.Text_Line_Left[7], 10, 570)


# Right
    # Text
    Text_ui(GameStateIG.Text_Line_Right[1], 460, 450)
    Text_ui(GameStateIG.Text_Line_Right[2], 460, 470)
    Text_ui(GameStateIG.Text_Line_Right[3], 460, 490)
    Text_ui(GameStateIG.Text_Line_Right[4], 460, 510)
    Text_ui(GameStateIG.Text_Line_Right[5], 460, 530)
    Text_ui(GameStateIG.Text_Line_Right[6], 460, 550)
    Text_ui(GameStateIG.Text_Line_Right[7], 460, 570)
    

def Game_ui_Fight(event):
    # Interface
    Text_ui_Screen("Stage : %i" % GameStateIG.Game_Progress, 15, 5)
    Text_ui_Screen("Turn : %i" % GameStateIG.Game_Progress, 665, 5)

    # Commands
    Button("Attack", 400-48, 450+2, 100-3, 50-5, Command_Button, red, Text_Title_Selection, event, Attack)
    Button("Magic",  400-48, 500+2, 100-3, 50-5, Command_Button, red, Text_Title_Selection, event, Magic)
    Button("Potion",  400-48, 550+2, 100-3, 50-5, Command_Button, red, Text_Title_Selection, event, Potion)

    # Player 1
    gameDisplay.blit(Ellesia_Icon, (10,455))
    gameDisplay.blit(Ellesia_Img, (60, 210))
    Text_Fight("%s" % PlayerIG.name, 60, 465)
    Text_Fight("HP: %i/%i" % (PlayerIG.Health, PlayerIG.Maxhealth), 170, 465)
    Text_Fight("MP: %i/%i" % (PlayerIG.MP, PlayerIG.MaxMP), 260, 465)

    # Ennemy 1
    if GameStateIG.Ennemy[0] == WolfIG:
        gameDisplay.blit(Wolf_Icon, (750,455))
        gameDisplay.blit(Wolf_Img, (630, 260))
    Text_Fight("%s" % GameStateIG.Ennemy[0].name, 660, 465)
    Text_Fight("HP: %i/%i" % (GameStateIG.Ennemy[0].Health, GameStateIG.Ennemy[0].Maxhealth), 550, 465)
    Text_Fight("MP: %i/%i" % (GameStateIG.Ennemy[0].MP, GameStateIG.Ennemy[0].MaxMP), 460, 465)


def Game_ui_Results(event):
    # Box 1
    gameDisplay.blit(Ellesia_Icon, (55,55))

    # Box 2
    Text_Fight("Player 1:", 160, 10)
    Text_Fight("%s" % PlayerIG.name, 160, 30)
    Text_Fight("Class: ######", 160, 70)

    # Box 3
    Text_Fight("Level : %i" % PlayerIG.Level, 310, 10)
        
    Text_Fight("Experience:", 310, 50)
    Text_Fight("%i -> ######" % PlayerIG.Experience, 310,70)
                    # Exp Gain
                    
    if PlayerIG.Experience >= 100:
        Text_Fight("Level Up!", 310, 110)


def Game_ui_Main(event):
    pass
##    Shop()
##    Training()
##    Next_Level()
##
##    Characters_Status()
##    Inventory()
##    Game_Save()

##    World_Map()
##    
##    Quit_Game()

    # Stage_Progress



def Shop():
    pass

def Training():
    pass

def Next_Level():
    GameStateIG.Game_Progress += 1

def Characters_Status():
    pass

def Inventory():
    pass

def World_Map():
    pass
