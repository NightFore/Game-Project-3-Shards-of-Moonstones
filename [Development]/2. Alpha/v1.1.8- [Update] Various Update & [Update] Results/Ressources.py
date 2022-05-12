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
Interface_Fight = pygame.image.load("Data\Game_ui\Interface_Fight.png")
Interface_Results = pygame.image.load("Data\Game_ui\Interface_Results.png")

    # Character / Monster
Ellesia_Img     = pygame.image.load("Data\Sprites\Character_Ellesia.png")
Wolf_Img        = pygame.image.load("Data\Sprites\Monster_Wolf.png")

    # Icon
Ellesia_Icon = pygame.image.load("Data\Icon\Ellesia_Icon.png")
Wolf_Icon = pygame.image.load("Data\Icon\Wolf_Icon.png")

    # OST
Main_Menu_OST = "Data\OST\Main_Menu.mp3"

Wake_Up             = "Data\OST\Cutscene_1_1_Wake_Up.mp3"
Around_a_Campfire   = "Data\OST\Cutscene_1_2_Around a Campfire.mp3"
Departure           = "Data/OST/Cutscene_1_3_Departure.mp3"


Shadow_Figures  = "Data/OST/Cutscene_2_1_Shadow_Figures.mp3"
It_is_Not_Over = "Data/OST/Cutscene_2_2_It_is_Not_Over.mp3"
We_Did_It      = "Data/OST/Cutscene_2_3_We_Did_It.mp3"

Village_Under_Attack    = "Data\OST\Fight_1_1_Village_Under_Attack.mp3"
Standard_Fight          = "Data/OST/Fight_1_2_Standard_Fight.mp3"
Let_Do_It_Together      = "Data/OST/Fight_1_3_Let_Do_It_Together.mp3"
Boss_Shadow_Figure      = "Data/OST/Fight_1_4_Boss_Shadow_Figure.mp3"

Sense_of_Duty           = "Data/OST/Fight_2_1_Sense_of_Duty.mp3"
They_Need_Our_Help     = "Data/OST/Fight_2_2_They_Need_Our_Help.mp3"
Dominating_The_Hill     = "Data/OST/Fight_2_3_Dominating_The_Hill.mp3"
Is_he_the_Mastermind    = "Data/OST/Fight_2_4_Is_he_the_Mastermind.mp3"
Last_Frontline          = "Data/OST/Fight_2_5_Last_Frontline.mp3"

I_am_Ready         = "Data/OST/Menu_Selection_1_I_am_Ready.mp3"
Prepare_Yourself    = "Data/OST/Menu_Selection_2_Prepare_Yourself.mp3"

Menu_Shop           = "Data/OST/Menu_Shop.mp3"

Finally_Some_Rest   = "Data/OST/Menu_Victory_1_Finally_Some_Rest.mp3"
March_To_Glory      = "Data/OST/Menu_Victory_2_March_To_Glory.mp3"

    # Sound Effect
Sound_Wolf_Roar = pygame.mixer.Sound("Data\Sound_Effects\Sound_Wolf_Roar.wav")

Sound_Hit_Damage_1 = pygame.mixer.Sound("Data\Sound_Effects\Sound_Hit_Damage_1.wav")
Sound_Hit_Damage_2 = pygame.mixer.Sound("Data\Sound_Effects\Sound_Hit_Damage_2.wav")
Sound_Slash_Damage = pygame.mixer.Sound("Data\Sound_Effects\Sound_Slash_Damage.wav")

Sound_Miss = pygame.mixer.Sound("Data\Sound_Effects\Sound_Miss.wav")

Sound_Defeated = pygame.mixer.Sound("Data\Sound_Effects\Sound_Defeated.wav")
