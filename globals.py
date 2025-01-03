import pygame
import sys
import time
import numpy as np
from PIL import Image

# constants
CANVAS_RECT = pygame.Rect(10, 10, 680, 490) # this is anywhere within the drawing region

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
BACKGROUND_COLOR = (255, 255, 255)
FPS = 120

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
canvas_screen = screen.subsurface(CANVAS_RECT)