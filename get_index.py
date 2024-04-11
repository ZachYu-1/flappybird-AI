# define a function to get the input index of the pipes
def get_index(pipes, birds):
    # get the birds' x position
    bird_x = birds[0].x
    # calculate the x distance between birds and each pipes
    list_distance = [pipe.x + pipe.IMG_WIDTH - bird_x for pipe in pipes]
    # get the index of the pipe that has the minimum non negative distance(the closest pipe in front of the bird)
    index = list_distance.index(min(i for i in list_distance if i >= 0))
    return index
