from __future__ import print_function
import pygame

pygame.init()

# set up the screen
SCREEN_WIDTH = 288
SCREEN_HEIGHT = 512
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# set up the font
FONT = pygame.font.Font('PixeloidSansBold-PKnYd.ttf', 13)
FONT_COLOR = (255, 255, 255)

# load images
BIRD_IMGS = [pygame.image.load('./images/Flappy Bird.png'),
             pygame.image.load('./images/Flappy Bird Wings Up.png'),
             pygame.image.load('./images/Flappy Bird Wings Down.png')]
BOTTOM_PIPE_IMG = pygame.image.load('./images/pipe-green.png')
TOP_PIPE_IMG = pygame.transform.flip(BOTTOM_PIPE_IMG, False, True)
FLOOR_IMG = pygame.image.load('./images/base.png')
BG_IMG = pygame.transform.scale(pygame.image.load('./images/background-day.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))

IMAGES, SOUNDS, HITMASKS = {}, {}, {}
