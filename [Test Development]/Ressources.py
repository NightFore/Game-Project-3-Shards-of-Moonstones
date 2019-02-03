import pygame
pygame.init()
    # Game Size Screen
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))

    # Ressources
black = (0,0,0)
Green = (60,212,122)
red = (200,0,0)
Text_ui_Color = black
game_ui_color = (147,169,213)
Introduction_Color = (112,146,190)
Command_Button = (142,207,244)
    
    # Background
Title_Screen_Background = pygame.image.load("Data\Background\Title_Screen_Background.png")
Background_Introduction = pygame.image.load("Data\Background\Background_Introduction.png")
Background_House        = pygame.image.load("Data\Background\Background_House.png")
Background_Main_Menu_1  = pygame.image.load("Data\Background\Background_Main_Menu_1.png")

    # Game_ui
Game_ui_Screen = pygame.image.load("Data\Game_ui\Game_ui_Cutscene.png")
Game_ui_Screen_Black = pygame.image.load("Data\Game_ui\Game_ui_Screen_Black.png")

Interface_Fight     = pygame.image.load("Data\Game_ui\Interface_Fight.png")
Interface_Results   = pygame.image.load("Data\Game_ui\Interface_Results.png")
Interface_Inventory = pygame.image.load("Data\Game_ui\Interface_Inventory.png")
Interface_Shop      = pygame.image.load("Data\Game_ui\Interface_Shop.png")

    # Icon
World_Map_Icon_ic   = pygame.image.load("Data\Icon\World_Map_Icon_ic.png")
World_Map_Icon_ac   = pygame.image.load("Data\Icon\World_Map_Icon_ac.png")
Exit_Button         = pygame.image.load("Data\Icon\Exit_Button.png")

Ellesia_Icon    = pygame.image.load("Data\Icon\Ellesia_Icon.png")
Iris_Icon       = pygame.image.load("Data\Icon\Iris_Icon.png")
Gyrei_Icon      = pygame.image.load("Data\Icon\Gyrei_Icon.png")

NoMonster_Icon      = pygame.image.load("Data\Icon\Monster_Icon.png")
Wolf_Icon           = pygame.image.load("Data\Icon\Wolf_Icon.png")
Direwolf_Icon       = pygame.image.load("Data\Icon\Direwolf_Icon.png")
Spectre_Icon        = pygame.image.load("Data\Icon\Spectre_Icon.png")
Shadow_Figure1_Icon = pygame.image.load("Data\Icon\Shadow_Figure1_Icon.png")

Summoner_Icon       = pygame.image.load("Data\Icon\Summoner_Icon.png")
Zombie_Icon         = pygame.image.load("Data\Icon\Zombie_Icon.png")
Ghoul_Icon          = pygame.image.load("Data\Icon\Ghoul_Icon.png")
Shadow_Figure2_Icon = pygame.image.load("Data\Icon\Shadow_Figure2_Icon.png")

    # Image
Ellesia_Img     = pygame.image.load("Data\Sprites\Ellesia_Img.png")
Iris_Img        = pygame.image.load("Data\Sprites\Iris_Img.png")
Gyrei_Img       = pygame.image.load("Data\Sprites\Gyrei_Img.png")

NoMonster_Img       = pygame.image.load("Data\Sprites\Monster_Img.png")
Wolf_Img            = pygame.image.load("Data\Sprites\Wolf_Img.png")
Direwolf_Img        = pygame.image.load("Data\Sprites\Ghoul_Img.png")
Spectre_Img         = pygame.image.load("Data\Sprites\Spectre_Img.png")
Shadow_Figure1_Img  = pygame.image.load("Data\Sprites\Shadow_Figure1_Img.png")

Summoner_Img        = pygame.image.load("Data\Sprites\Summoner_Img.png")
Zombie_Img          = pygame.image.load("Data\Sprites\Zombie_Img.png")
Ghoul_Img           = pygame.image.load("Data\Sprites\Ghoul_Img.png")
Shadow_Figure2_Img  = pygame.image.load("Data\Sprites\Shadow_Figure2_Img.png")



    # Sound Effect
Sound_Wolf_Roar = pygame.mixer.Sound("Data\Sound_Effects\Sound_Wolf_Roar.wav")

Sound_Hit_Damage_1 = pygame.mixer.Sound("Data\Sound_Effects\Sound_Hit_Damage_1.wav")
Sound_Hit_Damage_2 = pygame.mixer.Sound("Data\Sound_Effects\Sound_Hit_Damage_2.wav")
Sound_Slash_Damage = pygame.mixer.Sound("Data\Sound_Effects\Sound_Slash_Damage.wav")

Sound_Miss = pygame.mixer.Sound("Data\Sound_Effects\Sound_Miss.wav")

Sound_Defeated = pygame.mixer.Sound("Data\Sound_Effects\Sound_Defeated.wav")



    # Game OST
Serenity                    = "Data/OST/Cutscene_1_1_Serenity.mp3"
Around_a_Campfire           = "Data/OST/Cutscene_1_2_Around_a_Campfire.mp3"
Departure                   = "Data/OST/Cutscene_1_3_Departure.mp3"

Behind_the_Curtains         = "Data/OST/Cutscene_2_1_Behind_the_Curtains.mp3"
Danger_on_our_Lives         = "Data/OST/Cutscene_2_2_Danger_on_our_Lives.mp3"
Game_Credits                = "Data/OST/Cutscene_2_3_Game_Credits.mp3"

Fierce_Riposte              = "Data/OST/Fight_1_1_Fierce_Riposte.mp3"
Pushing_Forward             = "Data/OST/Fight_1_2_Pushing_Forward.mp3"
Together_We_Shall_Overcome  = "Data/OST/Fight_1_3_Together_We_Shall_Overcome.mp3"
Intimidating_Foe             = "Data/OST/Fight_1_4_Intimidating_Foe.mp3"

Sense_of_Duty               = "Data/OST/Fight_2_1_Sense_of_Duty.mp3"
Running_Through_the_Hills   = "Data/OST/Fight_2_2_Running_Through_the_Hills.mp3"
Last_Frontline              = "Data/OST/Fight_2_3_Last_Frontline.mp3"
Taking_Down_The_Mastermind  = "Data/OST/Fight_2_4_Taking_Down_The_Mastermind.mp3"
Ruling_Over_The_Hill        = "Data/OST/Fight_2_5_Ruling_Over_The_Hill.mp3"
Hot_Blooded                 = "Data/OST/Fight_2_6_Hot_Blooded.mp3"

Getting_Ready               = "Data/OST/Main_Menu_1_Getting_Ready.mp3"
Times_of_Crisis             = "Data/OST/Main_Menu_2_1_Times_of_Crisis.mp3"
Prepare_Yourself            = "Data/OST/Main_Menu_2_2_Prepare_Yourself.mp3"

Menu_Shop                   = "Data/OST/Menu_Shop.mp3"

Finally_Some_Rest           = "Data/OST/Menu_Victory_1_Finally_Some_Rest.mp3"
March_To_Glory              = "Data/OST/Menu_Victory_2_March_To_Glory.mp3"

Undisturbed_Place           = "Data/OST/Title_Screen_Undisturbed_Place.mp3"
