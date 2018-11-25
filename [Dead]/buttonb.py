import pygame

pygame.init()
width, height = (200,300)
gameDisplay = pygame.display.set_mode((width, height))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (30, 30, 30)
FONT = pygame.font.Font("freesansbold.ttf", 50)
green = (0,180,80)
red = (200,0,0)



def Button(x,y,w,h,ic,ac,event,action=None):
    Box = pygame.Rect(x,y,w,h)
    mouse = pygame.mouse.get_pos()
    # Active Color
    if Box.collidepoint(mouse):
        pygame.draw.rect(gameDisplay, ac, Box)

        # Action
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(event.button)
                if action != None:
                    action()

    # Inactive Color
    else:
        pygame.draw.rect(gameDisplay, ic, Box)
    
    # You can pass the center directly to the `get_rect` method.
    pygame.display.update()
