import pygame

pygame.init()

#grid
w = 25
h = 25
m = 2

size = (550, 700)
screen = pygame.display.set_mode(size)
screen.fill((255,255,255))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        for row in range(5):
            for col in range(5):
                if row == 0 or row == 4 or col == 0 or col == 4:
                    pygame.draw.rect(screen, (255,0,0), ((w + m) * col + m, ((h + m) * row + m)     , w, h), 1)
                    pygame.draw.rect(screen, (255,0,0), ((w + m) * col + m, ((h + m) * row + m)+ 150, w, h))

    pygame.display.flip()
