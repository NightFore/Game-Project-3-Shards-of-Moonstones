import pygame
pygame.init()
    # Game Size Screen
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))

    # Ressources
black = (0,0,0)
green = (0,180,80)
red = (200,0,0)
Text_ui_Color = black
game_ui_color = (147,169,213)
Introduction_Color = (112,146,190)
Command_Button = (142,207,244)

    # Background
Title_Screen_Background = pygame.image.load("Data\Background\Title_Screen_Background.png")
Background_Introduction = pygame.image.load("Data\Background\Background_Introduction.png")
Background_House = pygame.image.load("Data\Background\Background_House.png")

    # Background 2
Game_ui_Screen = pygame.image.load("Data\Game_ui\Game_ui_Cutscene.png")
Game_ui_Screen_Black = pygame.image.load("Data\Game_ui\Game_ui_Screen_Black.png")
Game_ui_Fight = pygame.image.load("Data\Game_ui\Game_ui_Fight.png")

    # Character / Monster
Ellesia_Img     = pygame.image.load("Data\Sprites\Character_Ellesia.png")
Wolf_Img        = pygame.image.load("Data\Sprites\Monster_Wolf.png")

    # Icon
Ellesia_Icon = pygame.image.load("Data\Icon\Ellesia_Icon.png")
Wolf_Icon = pygame.image.load("Data\Icon\Wolf_Icon.png")

    # OST
Main_Menu_OST = "Data\OST\Main_Menu.mp3"
Wake_Up = "Data\OST\Cutscene_1_1_Wake_Up.mp3"
Around_a_Campfire = "Data\OST\Cutscene_1_2_Around a Campfire.mp3"
Village_Under_Attack = "Data\OST\Fight_1_1_Village_Under_Attack.mp3"

    # Sound Effect
Sound_Wolf_Roar = pygame.mixer.Sound("Data\Sound_Effects\Sound_Wolf_Roar.wav")

Sound_Hit_Damage_1 = pygame.mixer.Sound("Data\Sound_Effects\Sound_Hit_Damage_1.wav")
Sound_Hit_Damage_2 = pygame.mixer.Sound("Data\Sound_Effects\Sound_Hit_Damage_2.wav")
Sound_Slash_Damage = pygame.mixer.Sound("Data\Sound_Effects\Sound_Slash_Damage.wav")

Sound_Miss = pygame.mixer.Sound("Data\Sound_Effects\Sound_Miss.wav")

Sound_Defeated = pygame.mixer.Sound("Data\Sound_Effects\Sound_Defeated.wav")
