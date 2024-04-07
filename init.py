# import packages to build the game
from __future__ import print_function
import pygame
import time
import os
import random

# initialize pygame
pygame.init()

# set up the screen to display the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 550
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# set up the font
FONT = pygame.font.SysFont('comicsansms', 20)
FONT_COLOR = (255, 255, 255)  # white font

# load the required images
BIRD_IMGS = [pygame.image.load('./images/Flappy Bird.png'),
             pygame.image.load('./images/Flappy Bird Wings Up.png'),
             pygame.image.load('./images/Flappy Bird Wings Down.png')]
BOTTOM_PIPE_IMG = pygame.image.load('./images/Super Mario pipe.png')
TOP_PIPE_IMG = pygame.transform.flip(BOTTOM_PIPE_IMG, False,
                                     True)  # flip the image of the bottom pipe to get the image for the pipe on the top
FLOOR_IMG = pygame.image.load('./images/Stone Floor.png')
BG_IMG = pygame.transform.scale(pygame.image.load('./images/City Skyline.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))
