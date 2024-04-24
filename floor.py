from init import FLOOR_IMG
from neat_para import *


class Floor:
    # attributes
    IMGS = [FLOOR_IMG, FLOOR_IMG, FLOOR_IMG]  # 3 images to show the moving
    VELOCITY = floor_velocity  # moving velocity
    IMG_WIDTH = FLOOR_IMG.get_width()  # width

    # initialize
    def __init__(self, y_position):
        self.x1 = 0
        self.x2 = self.IMG_WIDTH
        self.x3 = self.IMG_WIDTH * 2
        self.y = y_position

    # move the floor
    def move(self):
        self.x1 -= self.VELOCITY
        self.x2 -= self.VELOCITY
        self.x3 -= self.VELOCITY

        if self.x1 + self.IMG_WIDTH < 0:
            self.x1 = self.x3 + self.IMG_WIDTH  # move the first floor to the right of the third
        if self.x2 + self.IMG_WIDTH < 0:
            self.x2 = self.x1 + self.IMG_WIDTH  # move the second floor image to the right of the first
        if self.x3 + self.IMG_WIDTH < 0:
            self.x3 = self.x2 + self.IMG_WIDTH  # move the third floor to the right of the second
