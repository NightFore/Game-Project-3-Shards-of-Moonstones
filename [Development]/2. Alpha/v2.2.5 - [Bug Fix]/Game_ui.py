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
    Text_ui_Screen("Stage : %i" % GameStateIG.Stage_Progress, 15, 5)
    Text_ui_Screen("Turn : %i" % GameStateIG.Stage_Progress, 665, 5) #####################

    # Commands
    Button("Attack",    400-48, 450+2, 100-3, 50-5, Command_Button, red, Text_Title_Selection, event, Attack)
    Button("Skill",     400-48, 500+2, 100-3, 50-5, Command_Button, red, Text_Title_Selection, event, Skill)
    Button("Potion",    400-48, 550+2, 100-3, 50-5, Command_Button, red, Text_Title_Selection, event, Potion)

# Player
    # Player 1
    if GameStateIG.Player_Slot[0] == True:
        gameDisplay.blit(GameStateIG.Player[0].Img, (60, 210))
        gameDisplay.blit(GameStateIG.Player[0].Icon, (10,455))
        Text_Fight("%s" % GameStateIG.Player[0].name, 60, 465)
        Text_Fight("HP: %i/%i" % (GameStateIG.Player[0].Health, GameStateIG.Player[0].Maxhealth),    170, 465)
        Text_Fight("MP: %i/%i" % (GameStateIG.Player[0].MP,     GameStateIG.Player[0].MaxMP),        260, 465)

    # Player 2
    if GameStateIG.Player_Slot[1] == True:
        gameDisplay.blit(GameStateIG.Player[1].Img, (60, 260))
        gameDisplay.blit(GameStateIG.Player[1].Icon, (10,505))
        Text_Fight("%s" % GameStateIG.Player[1].name, 60, 515)
        Text_Fight("HP: %i/%i" % (GameStateIG.Player[1].Health, GameStateIG.Player[1].Maxhealth),    170, 515)
        Text_Fight("MP: %i/%i" % (GameStateIG.Player[1].MP,     GameStateIG.Player[1].MaxMP),        260, 515)

    # Player 3
    if GameStateIG.Player_Slot[2] == True:
        gameDisplay.blit(GameStateIG.Player[2].Img, (60, 310))
        gameDisplay.blit(GameStateIG.Player[2].Icon, (10,555))
        Text_Fight("%s" % GameStateIG.Player[2].name, 60, 565)
        Text_Fight("HP: %i/%i" % (GameStateIG.Player[2].Health, GameStateIG.Player[2].Maxhealth),    170, 565)
        Text_Fight("MP: %i/%i" % (GameStateIG.Player[2].MP,     GameStateIG.Player[2].MaxMP),        260, 565)


# Enemy
    # Enemy 1
    if GameStateIG.Enemy_Slot[0] == True:
        gameDisplay.blit(GameStateIG.Enemy[0].Img,  (630, 260))
        gameDisplay.blit(GameStateIG.Enemy[0].Icon, (750, 455))
        Text_Fight("%s" % GameStateIG.Enemy[0].name, 660, 465)
        Text_Fight("HP: %i/%i" % (GameStateIG.Enemy[0].Health,  GameStateIG.Enemy[0].Maxhealth),    550, 465)
        Text_Fight("MP: %i/%i" % (GameStateIG.Enemy[0].MP,      GameStateIG.Enemy[0].MaxMP),        460, 465)

    # Enemy 2
    if GameStateIG.Enemy_Slot[1] == True:
        gameDisplay.blit(GameStateIG.Enemy[1].Img,  (630, 310))
        gameDisplay.blit(GameStateIG.Enemy[1].Icon, (750, 505))
        Text_Fight("%s" % GameStateIG.Enemy[1].name, 660, 515)
        Text_Fight("HP: %i/%i" % (GameStateIG.Enemy[1].Health,  GameStateIG.Enemy[1].Maxhealth),    550, 515)
        Text_Fight("MP: %i/%i" % (GameStateIG.Enemy[1].MP,      GameStateIG.Enemy[1].MaxMP),        460, 515)

    # Enemy 3
    if GameStateIG.Enemy_Slot[2] == True:
        gameDisplay.blit(GameStateIG.Enemy[2].Img,  (630, 360))
        gameDisplay.blit(GameStateIG.Enemy[2].Icon, (750, 555))
        Text_Fight("%s" % GameStateIG.Enemy[2].name, 660, 565)
        Text_Fight("HP: %i/%i" % (GameStateIG.Enemy[2].Health,  GameStateIG.Enemy[2].Maxhealth),    550, 565)
        Text_Fight("MP: %i/%i" % (GameStateIG.Enemy[2].MP,      GameStateIG.Enemy[2].MaxMP),        460, 565)




def Game_ui_Results(event):
# Player
    # Player 1
    if GameStateIG.Player_Slot[0] == True:
        Slot = 0
        
        gameDisplay.blit(Ellesia_Icon, (55, 55))

        Text_Fight("Player %i:" % Slot, 160, 10)
        Text_Fight("%s" % GameStateIG.Player[Slot].name, 160, 30)
        Text_Fight("Class:", 160, 70)
        Text_Fight("%s" % GameStateIG.Player[Slot].Class, 160, 90)

        Text_Fight("Level : %i" % GameStateIG.Player[Slot].Level, 310, 10)
        Text_Fight("Experience:", 310, 50)
        Text_Fight("%i -> %i" % (GameStateIG.Player[Slot].Experience, (GameStateIG.Player[Slot].Experience + GameStateIG.EXP_Gain)),  310, 70)
                        
        if GameStateIG.Player[Slot].Experience >= 100:
            Text_Fight("Level Up!", 310, 110)
            

    if GameStateIG.Player_Slot[1] == True:
        Slot += 1
        
        gameDisplay.blit(Iris_Icon, (55, 55+150*Slot))
        
        Text_Fight("Player %i:" % Slot, 160, 10+150*Slot)
        Text_Fight("%s" % GameStateIG.Player[Slot].name, 160, 30+150*Slot)
        Text_Fight("Class:", 160, 70+150*Slot)
        Text_Fight("%s" % GameStateIG.Player[Slot].Class, 160, 90+150*Slot)
        
        Text_Fight("Level : %i" % GameStateIG.Player[Slot].Level, 310, 10+150*Slot)
        Text_Fight("Experience:", 310, 50+150*Slot)
        Text_Fight("%i -> %i" % (GameStateIG.Player[Slot].Experience, (GameStateIG.Player[Slot].Experience + GameStateIG.EXP_Gain)),  310, 70+150*Slot)
                        
        if GameStateIG.Player[Slot].Experience >= 100:
            Text_Fight("Level Up!", 310, 110+150*Slot)


    if GameStateIG.Player_Slot[2] == True:
        Slot += 1
        
        gameDisplay.blit(Gyrei_Icon, (55, 55+150*Slot))

        Text_Fight("Player %i:" % Slot, 160, 10+150*Slot)
        Text_Fight("%s" % GameStateIG.Player[Slot].name, 160, 30+150*Slot)
        Text_Fight("Class:", 160, 70+150*Slot)
        Text_Fight("%s" % GameStateIG.Player[Slot].Class, 160, 90+150*Slot)

        Text_Fight("Level : %i" % GameStateIG.Player[Slot].Level, 310, 10+150*Slot)
        Text_Fight("Experience:", 310, 50+150*Slot)
        Text_Fight("%i -> %i" % (GameStateIG.Player[Slot].Experience, (GameStateIG.Player[Slot].Experience + GameStateIG.EXP_Gain)),  310, 70+150*Slot)
                        
        if GameStateIG.Player[Slot].Experience >= 100:
            Text_Fight("Level Up!", 310, 110+150*Slot)



# Enemy
    # Enemy 1
    Text_Fight("Enemy Defeated", 460, 15)

    if GameStateIG.Enemy_Slot[0] == True:
        Slot = 0
        gameDisplay.blit(GameStateIG.Enemy[Slot].Icon,     (465, 75+75*Slot))
        Text_Fight("%s" % GameStateIG.Enemy[Slot].name,    515, 85)
        
    # Enemy 2
    if GameStateIG.Enemy_Slot[1] == True:
        Slot += 1
        gameDisplay.blit(GameStateIG.Enemy[Slot].Icon,     (465, 75+75*Slot))
        Text_Fight("%s" % GameStateIG.Enemy[Slot].name,    515, 85+75*Slot)

    # Enemy 3
    if GameStateIG.Enemy_Slot[2] == True:
        Slot += 1
        gameDisplay.blit(GameStateIG.Enemy[Slot].Icon,     (465, 75+75*Slot))
        Text_Fight("%s" % GameStateIG.Enemy[Slot].name,    515, 75+75*Slot)



# Total Gain
    Text_Fight("Results :", 460, 310)
    
    Text_Fight("Experience Gain :", 460, 340)
    Text_Fight("+%i" % GameStateIG.EXP_Gain, 460, 360)
    
    Text_Fight("Total Gold :", 460, 400)
    Text_Fight("%i -> %i" % (PlayerIG.Gold, GameStateIG.Gold_Gain), 460, 420)



# Drop
    Text_Fight("Drop", 660, 15)



# Inventory
    Text_Fight("Inventory", 660, 160)




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
