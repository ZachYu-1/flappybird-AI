# import packages to build the AI
import neat
import pygame

from bird import Bird
from floor import Floor
from parasetting import *
from pipe import Pipe
from init import SCREEN
from get_index import get_index
from neat_para import prob_threshold_to_jump, failed_punishment
from check_collision import collide
from show_screen import draw_game
generation = 0

# define a function to run the main game loop
def main(genomes, config):
    global generation  # use the global variable gen and SCREEN
    screen = SCREEN
    generation += 1  # update the generation

    score = 0  # initiate score to 0
    clock = pygame.time.Clock()  # set up a clock object to help control the game framerate
    start_time = pygame.time.get_ticks()  # reset the start_time after every time we update our generation

    floor = Floor(floor_starting_y_position)  # build the floor
    pipes_list = [Pipe(pipe_starting_x_position + i * pipe_horizontal_gap) for i in
                  range(pipe_max_num)]  # build the pipes and seperate them by pipe_horizontal_gap

    models_list = []  # create an empty list to store all the training neural networks
    genomes_list = []  # create an empty list to store all the training genomes
    birds_list = []  # create an empty list to store all the training birds

    for genome_id, genome in genomes:  # for each genome
        birds_list.append(
            Bird(bird_starting_x_position, bird_starting_y_position))  # create a bird and append the bird in the list
        genome.fitness = 0  # start with fitness of 0
        genomes_list.append(genome)  # append the genome in the list
        model = neat.nn.FeedForwardNetwork.create(genome,
                                                  config)  # set up the neural network for each genome using the configuration we set
        models_list.append(model)  # append the neural network in the list

    run = True

    while run is True:  # when we run the program

        # check the event of the game and quit if we close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                break

        # stop the game when the score exceed the maximum score
        # break the loop and restart when no bird left
        if score >= max_score or len(birds_list) == 0:
            run = False
            break

        game_time = round((pygame.time.get_ticks() - start_time) / 1000, 2)  # record the game time for this generation

        clock.tick(FPS)  # update the clock, run at FPS frames per second (FPS). This can be used to help limit the runtime speed of a game.

        floor.move()  # move the floor

        pipe_input_index = get_index(pipes_list, birds_list)  # get the input index of the pipes list

        passed_pipes = []  # create an empty list to hold all the passed pipes
        for pipe in pipes_list:
            pipe.move()  # move the pipe
            if pipe.x + pipe.IMG_WIDTH < birds_list[0].x:  # if the bird passed the pipe
                passed_pipes.append(pipe)  # append the pipe to the passed pipes list

        score = len(
            passed_pipes)  # calculate the score of the game, which equals to the number of pipes the bird passed

        for index, bird in enumerate(birds_list):
            bird.move()  # move the bird
            delta_x = bird.x - pipes_list[
                pipe_input_index].x  # input 1: the horizontal distance between the bird and the pipe
            delta_y_top = bird.y - pipes_list[
                pipe_input_index].top_pipe_height  # input 2: the vertical distance between the bird and the top pipe
            delta_y_bottom = bird.y - pipes_list[
                pipe_input_index].bottom_pipe_topleft  # input 3: the vertical distance between the bird and the bottom pipe
            net_input = (delta_x, delta_y_top, delta_y_bottom)
            # input the bird's distance from the pipes to get the output of whether to jump or not
            output = models_list[index].activate(net_input)

            if output[0] > prob_threshold_to_jump:  # if the model output is greater than the probability threshold to jump
                bird.jump()  # then jump the bird

            bird_failed = True if collide(bird, pipes_list[pipe_input_index], floor, screen) is True else False

            # the fitness function is a combination of game score, alive time, and a punishment for collision
            genomes_list[index].fitness = game_time + score - bird_failed * failed_punishment

            if bird_failed:
                models_list.pop(index)  # drop the model from the list if collided
                genomes_list.pop(index)  # drop the genome from the list if collided
                birds_list.pop(index)  # drop the bird from the list if collided
        pygame.display.set_caption('Flappy Bird')
        draw_game(screen, birds_list, pipes_list, floor, score, generation)  # draw the screen of the game