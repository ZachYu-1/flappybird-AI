import neat
import pygame

from bird import Bird
from floor import Floor
from neat_para import *
from pipe import Pipe
from init import SCREEN
from get_index import get_index
from check_collision import collide
from show_screen import draw_game


def neat_loop(genomes, config):
    global generation
    screen = SCREEN
    generation += 1  # update the generation

    score = 0  # initiate score to 0
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()  # reset the start_time after every time we update our generation

    floor = Floor(floor_starting_y_position)  # build the floor
    pipes_list = [Pipe(pipe_starting_x_position + i * pipe_horizontal_gap) for i in
                  range(pipe_max_num)]  # build the pipes

    models_list = []
    genomes_list = []
    birds_list = []

    for genome_id, genome in genomes:
        birds_list.append(
            Bird(bird_starting_x_position, bird_starting_y_position))  # create a bird
        genome.fitness = 0
        genomes_list.append(genome)  # append the genome
        model = neat.nn.FeedForwardNetwork.create(genome, config)  # set up the neural network for each genome
        models_list.append(model)  # append the neural network

    run = True

    while run is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                break

        if score >= max_score or len(birds_list) == 0:
            run = False
            break

        game_time = round((pygame.time.get_ticks() - start_time) / 1000, 2)  # record the game time for this generation

        clock.tick(FPS)

        floor.move()  # move the floor

        pipe_input_index = get_index(pipes_list, birds_list)

        passed_pipes = []
        for pipe in pipes_list:
            pipe.move()  # move the pipe
            if pipe.x + pipe.IMG_WIDTH < birds_list[0].x:
                passed_pipes.append(pipe)  # append the passed pipes list

        score = len(passed_pipes)

        for index, bird in enumerate(birds_list):
            bird.move()  # move the bird
            delta_x = bird.x - pipes_list[
                pipe_input_index].x  # input the horizontal distance
            delta_y_top = bird.y - pipes_list[
                pipe_input_index].top_pipe_height  # input the vertical distance
            delta_y_bottom = bird.y - pipes_list[
                pipe_input_index].bottom_pipe_topleft  # input the vertical distance
            net_input = (delta_x, delta_y_top, delta_y_bottom)
            output = models_list[index].activate(net_input)

            if output[0] > prob_threshold_to_jump:
                bird.jump()

            bird_failed = True if collide(bird, pipes_list[pipe_input_index], floor, screen) is True else False

            genomes_list[index].fitness = game_time + score - bird_failed * failed_punishment

            if bird_failed:
                models_list.pop(index)
                genomes_list.pop(index)
                birds_list.pop(index)
        pygame.display.set_caption('Flappy Bird')
        draw_game(screen, birds_list, pipes_list, floor, score, generation, game_time)
