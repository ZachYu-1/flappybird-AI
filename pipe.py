# build the class Pipe
import random

from init import TOP_PIPE_IMG, BOTTOM_PIPE_IMG
from parasetting import pipe_vertical_gap, pipe_velocity, top_pipe_min_height, top_pipe_max_height


class Pipe:
    # Pipe's attributes
    VERTICAL_GAP = pipe_vertical_gap  # the gap between the top and bottom pipes
    VELOCITY = pipe_velocity  # the moving velocity of the pipes
    IMG_WIDTH = TOP_PIPE_IMG.get_width()  # the width of the pipe
    IMG_LENGTH = TOP_PIPE_IMG.get_height()  # the length of the pipe

    # initialize the Object
    def __init__(self, x_position):
        self.top_pipe_img = TOP_PIPE_IMG  # get the image for the pipe on the top
        self.bottom_pipe_img = BOTTOM_PIPE_IMG  # get the image for the pipe on the bottom
        self.x = x_position  # starting x position of the first set of pipes
        self.top_pipe_height = 0  # the height of the top pipe, initialized to be 0
        self.top_pipe_topleft = 0  # the topleft position of the top pipe, initialized to be 0
        self.bottom_pipe_topleft = 0  # the topleft position of the bottom pipe, initialized to be 0
        self.random_height()  # set the height of the pipes randomly as well as the starting topleft position for top and bottom pipes

    # define a function to move the pipe
    def move(self):
        self.x -= self.VELOCITY

    # define a function to randomize pipe gaps
    def random_height(self):
        self.top_pipe_height = random.randrange(top_pipe_min_height,
                                                top_pipe_max_height)  # the range is between top_pipe_min_height and top_pipe_max_height
        self.top_pipe_topleft = self.top_pipe_height - self.IMG_LENGTH  # the topleft position of the top pipe should be the random height - the length of the pipe
        self.bottom_pipe_topleft = self.top_pipe_height + self.VERTICAL_GAP  # the topleft position of the bottom pipe should be the random height + the GAP
