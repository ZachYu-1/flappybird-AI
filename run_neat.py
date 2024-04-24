import neat

from main_loop import main
from neat_para import max_gen
from visualize import *


def run_NEAT(config_file):
    # Create an object from configuration file
    config = neat.config.Config(neat.DefaultGenome,
                                neat.DefaultReproduction,
                                neat.DefaultSpeciesSet,
                                neat.DefaultStagnation,   
                                config_file)

    # Create a population
    neat_pop = neat.population.Population(config)

    # Add a reporter
    neat_pop.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    neat_pop.add_reporter(stats)

    # Run the game
    neat_pop.run(main, max_gen)

    # get the beat fit genome
    winner = stats.best_genome()

    # visualize results
    # node_names = {-1: 'delta_x', -2: 'delta_y_top', -3: 'delta_y_bottom', 0: 'Jump or Not'}
    # draw_net(config, winner, True, node_names=node_names)
    # plot_stats(stats, ylog=False, view=True)
    # plot_species(stats, view=True)

    print('\nBest genome:\n{!s}'.format(winner))


if __name__ == '__main__':
    config_file = 'config-feedforward.txt'
    run_NEAT(config_file)
