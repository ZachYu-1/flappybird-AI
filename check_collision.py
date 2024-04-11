# define a function to check collision
import pygame


def collide(bird, pipe, floor, screen):
    # Creates a Mask object from the given surface by setting all the opaque pixels and not setting the transparent pixels
    bird_mask = pygame.mask.from_surface(bird.bird_img)  # get the mask of the bird
    top_pipe_mask = pygame.mask.from_surface(pipe.top_pipe_img)  # get the mask of the pipe on the top
    bottom_pipe_mask = pygame.mask.from_surface(pipe.bottom_pipe_img)  # get the mask of the pipe on the bottom

    sky_height = 0  # the sky height is the upper limit
    floor_height = floor.y  # the floor height is the lower limit
    bird_lower_end = bird.y + bird.bird_img.get_height()  # the y position of the lower end of the bird image

    # in order to check whether the bird hit the pipe, we need to find the point of intersection of the bird and the pipes
    # if overlap, then mask.overlap(othermask, offset) return (x, y)
    # if not overlap, then mask.overlap(othermask, offset) return None
    # more information regarding offset, https://www.pygame.org/docs/ref/mask.html#mask-offset-label
    top_pipe_offset = (round(pipe.x - bird.x), round(pipe.top_pipe_topleft - bird.y))
    bottom_pipe_offset = (round(pipe.x - bird.x), round(pipe.bottom_pipe_topleft - bird.y))

    # Returns the first point of intersection encountered between bird's mask and pipe's masks
    top_pipe_intersection_point = bird_mask.overlap(top_pipe_mask, top_pipe_offset)
    bottom_pipe_intersection_point = bird_mask.overlap(bottom_pipe_mask, bottom_pipe_offset)

    if top_pipe_intersection_point is not None or bottom_pipe_intersection_point is not None or bird_lower_end > floor_height or bird.y < sky_height:
        return True
    else:
        return False
