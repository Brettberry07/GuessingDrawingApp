import pygame

from globals import *

class Frame:

    '''
    Frame

    #############
    #           #
    #           #
    #############
    #   O    O  #
    #############

    '''

    #list that holds the borders
    top_border = pygame.Rect(0, 0, SCREEN_WIDTH, 10)
    bottom_border = pygame.Rect(0, SCREEN_HEIGHT - 10, SCREEN_WIDTH, 10)
    left_border = pygame.Rect(0, 0, 10, SCREEN_HEIGHT)
    right_border = pygame.Rect(SCREEN_WIDTH-10, 0, 10, SCREEN_HEIGHT)
    middle_border = pygame.Rect(0, 500, SCREEN_WIDTH, 10)

    borders = [top_border, bottom_border, left_border, right_border, middle_border]
    color = (50, 50, 50)

    @staticmethod
    def draw():
        for border in Frame.borders:
            pygame.draw.rect(screen, Frame.color, border)





