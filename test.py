### Test python file ###

import sys
import pygame as pg
from time import sleep

#initialize pygame
pg.init()

# Define screen size
WIDTH, HEIGHT = 1920, 1080
SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Test Game")

# Define Screen Colors
White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)

# Main Game loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    SCREEN.fill(White)

#End of game loop