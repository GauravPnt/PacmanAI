from typing import Type

import pygame
from pygame.math import Vector2

vec = pygame.math.Vector2

WIDTH, HEIGHT = 560, 620

ROWS = 30
COLS = 28

CELL_WIDTH = WIDTH // COLS
CELL_HEIGHT = HEIGHT // ROWS

FPS = 60

GREY = (107, 107, 107)
BLACK = (0, 0, 0)
PACMAN_COLOR = (255, 255, 0)
BLINKY_COLOR = (255, 0, 0)
PINKY_COLOR = (255, 184, 255)
INKY_COLOR = (0, 255, 255)
CLYDE_COLOR = (255, 184, 82)

# noinspection PyArgumentList
UP = vec(0, -1)
# noinspection PyArgumentList
DOWN = vec(0, 1)
# noinspection PyArgumentList
LEFT = vec(-1, 0)
# noinspection PyArgumentList
RIGHT = vec(1, 0)
# noinspection PyArgumentList
ORIGIN = vec(0, 0)

INF = float('inf')
