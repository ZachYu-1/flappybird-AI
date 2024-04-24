import pygame

from init import BIRD_IMGS
from neat_para import *


class Bird:
    # Bird's attributes
    IMGS = BIRD_IMGS
    MAX_UPWARD_ANGLE = bird_max_upward_angle
    MAX_DOWNWARD_ANGLE = bird_max_downward_angle

    # initialize
    def __init__(self, x_position, y_position):
        self.bird_img = self.IMGS[0]
        self.x = x_position  # starting x position
        self.y = y_position  # starting y position
        self.fly_angle = 0  # starting flying angle
        self.time = 0  # starting time set to calculate displacement
        self.velocity = 0  # starting vertical velocity
        self.index = 0

    # move the bird
    def move(self):
        self.time += 1
        displacement = self.velocity * self.time + 0.5 * bird_acceleration * self.time ** 2
        # set a displacement limit
        if displacement > bird_max_displacement:
            displacement = bird_max_displacement

        self.y = self.y + displacement  # update the y position

        if displacement < 0:  # going up
            if self.fly_angle < self.MAX_UPWARD_ANGLE:
                self.fly_angle += max(bird_angular_acceleration * (self.MAX_UPWARD_ANGLE - self.fly_angle),
                                      bird_min_incremental_angle)
            elif self.fly_angle >= self.MAX_UPWARD_ANGLE:
                self.fly_angle = self.MAX_UPWARD_ANGLE

        else:  # going down
            if self.fly_angle > self.MAX_DOWNWARD_ANGLE:
                self.fly_angle -= abs(min(bird_angular_acceleration * (self.MAX_DOWNWARD_ANGLE - self.fly_angle),
                                          -bird_min_incremental_angle))
            elif self.fly_angle <= self.MAX_DOWNWARD_ANGLE:
                self.fly_angle = self.MAX_DOWNWARD_ANGLE

    # jump the bird
    def jump(self):
        self.velocity = bird_jump_velocity
        self.time = 0

    # update image
    def update(self):
        if self.fly_angle < -45:
            self.bird_img = self.IMGS[0]
            self.index = 0

        elif self.index >= len(self.IMGS):
            self.index = 0

        self.bird_img = self.IMGS[self.index]
        self.index += 1

        rotated_image = pygame.transform.rotate(self.bird_img, self.fly_angle)
        origin_img_center = self.bird_img.get_rect(topleft=(self.x, self.y)).center
        rotated_rect = rotated_image.get_rect(center=origin_img_center)
        return rotated_image, rotated_rect
