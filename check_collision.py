import pygame


def collide(bird, pipe, floor, screen):
    bird_mask = pygame.mask.from_surface(bird.bird_img)  # get the mask of bird
    top_pipe_mask = pygame.mask.from_surface(pipe.top_pipe_img)  # get the mask of top pipe
    bottom_pipe_mask = pygame.mask.from_surface(pipe.bottom_pipe_img)  # get the mask of bottom pipe

    sky_height = 0
    floor_height = floor.y
    bird_lower_end = bird.y + bird.bird_img.get_height()

    top_pipe_offset = (round(pipe.x - bird.x), round(pipe.top_pipe_topleft - bird.y))
    bottom_pipe_offset = (round(pipe.x - bird.x), round(pipe.bottom_pipe_topleft - bird.y))

    top_pipe_intersection_point = bird_mask.overlap(top_pipe_mask, top_pipe_offset)
    bottom_pipe_intersection_point = bird_mask.overlap(bottom_pipe_mask, bottom_pipe_offset)

    if top_pipe_intersection_point is not None or bottom_pipe_intersection_point is not None or bird_lower_end > floor_height or bird.y < sky_height:
        return True
    else:
        return False
