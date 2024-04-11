# build the class Floor
from init import FLOOR_IMG
from parasetting import floor_velocity


class Floor:
    # Floor's attributes
    IMGS = [FLOOR_IMG, FLOOR_IMG, FLOOR_IMG]  # we need 3 floor images to set up the moving floor
    VELOCITY = floor_velocity  # the moving velocity of the floor
    IMG_WIDTH = FLOOR_IMG.get_width()  # the width of the floor

    # initialize the Object
    def __init__(self, y_position):
        # these 3 images have different starting position but have the same y position
        self.x1 = 0  # the starting x position of the first floor image
        self.x2 = self.IMG_WIDTH  # the starting x position of the second floor image
        self.x3 = self.IMG_WIDTH * 2  # the starting x position of the third floor image
        self.y = y_position  # the y position of the floor image

    # define a function to move the floor
    def move(self):
        self.x1 -= self.VELOCITY  # move to the left with the velocity of VELOCITY
        self.x2 -= self.VELOCITY  # move to the left with the velocity of VELOCITY
        self.x3 -= self.VELOCITY  # move to the left with the velocity of VELOCITY

        if self.x1 + self.IMG_WIDTH < 0:  # if the first floor image moves out of the screen
            self.x1 = self.x3 + self.IMG_WIDTH  # then move the first floor image to to the right of the third floor image
        if self.x2 + self.IMG_WIDTH < 0:  # if the second floor image moves out of the screen
            self.x2 = self.x1 + self.IMG_WIDTH  # then move the second floor image to to the right of the first floor image
        if self.x3 + self.IMG_WIDTH < 0:  # if the third floor image moves out of the screen
            self.x3 = self.x2 + self.IMG_WIDTH  # then move the third floor image to to the right of the second floor image