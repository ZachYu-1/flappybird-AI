def get_index(pipes, birds):
    # the position of bird
    bird_x = birds[0].x
    # the distance between bird and pipes
    list_distance = [pipe.x + pipe.IMG_WIDTH - bird_x for pipe in pipes]
    # get the index of pipe that is the closest to the bird
    index = list_distance.index(min(i for i in list_distance if i >= 0))
    return index
