import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

gray = (125, 125, 125)
black = (0, 0, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)

polygon(screen, gray, [(0,0), (0,400),
                               (400,400), (400,0)])

# Body
circle(screen, yellow, (200, 200), 110)
circle(screen, black, (200, 200), 110, 2)

# Eyes
circle(screen, red, (150, 180), 20)
circle(screen, black, (150, 180), 20, 2)
circle(screen, black, (150, 180), 6)

circle(screen, red, (250, 180), 15)
circle(screen, black, (250, 180), 15, 2)
circle(screen, black, (250, 180), 6)

# Eyebrows
polygon(screen, black, [(90,125), (175,172),
                               (180,162), (95,115)])
polygon(screen, black, [(300,155), (225,172),
                               (220,162), (305,145)])

# Mouth
rect(screen, black, (160, 250, 90, 30))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
