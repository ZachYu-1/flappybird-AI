# build the class Bird
import pygame

from init import BIRD_IMGS
from parasetting import bird_max_upward_angle, bird_max_downward_angle, bird_max_displacement, \
    bird_angular_acceleration, bird_acceleration, bird_min_incremental_angle, bird_jump_velocity


class Bird:
    # Bird's attributes
    IMGS = BIRD_IMGS
    MAX_UPWARD_ANGLE = bird_max_upward_angle
    MAX_DOWNWARD_ANGLE = bird_max_downward_angle

    # initialize the Object
    def __init__(self, x_position, y_position):
        self.bird_img = self.IMGS[0]  # use the first image as the initial image
        self.x = x_position  # starting x position
        self.y = y_position  # starting y position
        self.fly_angle = 0  # starting flying angle, initialized to be 0
        self.time = 0  # starting time set to calculate displacement, initialized to be 0
        self.velocity = 0  # starting vertical velocity, initialized to be 0
        self.index = 0  # used to change bird images, initialized to be 0

    # define a function to move the bird
    def move(self):
        self.time += 1  # count the time

        # for a body with a nonzero speed v and a constant acceleration a
        # the displacement d of this body after time t is d = vt + 1/2at^2
        displacement = self.velocity * self.time + 0.5 * bird_acceleration * self.time ** 2  # calculate the displacement when going downward

        # we don't want the bird going donw too fast
        # so we need to set a displacement limit per frame
        if displacement > bird_max_displacement:
            displacement = bird_max_displacement

        self.y = self.y + displacement  # update the bird y position after the displacement

        if displacement < 0:  # when the bird is going up
            if self.fly_angle < self.MAX_UPWARD_ANGLE:  # if the flying angle is less than the maximum upward angle
                self.fly_angle += max(bird_angular_acceleration * (self.MAX_UPWARD_ANGLE - self.fly_angle),
                                      bird_min_incremental_angle)  # accelerate the angle up
            elif self.fly_angle >= self.MAX_UPWARD_ANGLE:
                self.fly_angle = self.MAX_UPWARD_ANGLE

        else:  # when the bird is going down
            if self.fly_angle > self.MAX_DOWNWARD_ANGLE:  # if the flying angle is less than the maximum downward angle
                self.fly_angle -= abs(min(bird_angular_acceleration * (self.MAX_DOWNWARD_ANGLE - self.fly_angle),
                                          -bird_min_incremental_angle))  # accelerate the angle down
            elif self.fly_angle <= self.MAX_DOWNWARD_ANGLE:
                self.fly_angle = self.MAX_DOWNWARD_ANGLE

    # define a function to jump the bird
    def jump(self):
        self.velocity = bird_jump_velocity  # jump up by bird_jump_velocity
        self.time = 0  # when we jump, we reset the time to 0

    # define a function to get the rotated image and rotated rectangle for draw function
    def update(self):
        # if the bird is diving, then it shouldn't flap its wings
        if self.fly_angle < -45:
            self.bird_img = self.IMGS[0]
            self.index = 0  # reset the index

        # if the bird is not diving, then it should flap its wings
        # keep looping the 3 bird images to mimic flapping its wings
        elif self.index >= len(self.IMGS):
            self.index = 0

        self.bird_img = self.IMGS[self.index]
        self.index += 1

        # rotate the bird image for degree at self.tilt
        rotated_image = pygame.transform.rotate(self.bird_img, self.fly_angle)
        # store the center of the source image rectangle
        origin_img_center = self.bird_img.get_rect(topleft=(self.x, self.y)).center
        # update the center of the rotated image rectangle
        rotated_rect = rotated_image.get_rect(center=origin_img_center)
        # get the rotated bird image and the rotated rectangle
        return rotated_image, rotated_rect
