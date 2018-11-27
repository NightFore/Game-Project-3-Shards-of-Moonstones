import pygame

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

    # Game Files
Title_Screen_Background = pygame.image.load("Data\Background\Title_Screen_Background.png")
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
Introduction = "Data\OST\Cutscene\Introduction.mp3"
Village_Under_Attack = "Data\OST\Fight\#1-1 Village_Under_Attack.mp3"
