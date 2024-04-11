import neat

from main_loop import main
from neat_para import max_gen


def run_NEAT(config_file):
    # use NEAT algorithm to build a neural network based on the pre-set configurtion
    # Create a neat.config.Config object from the configuration file
    config = neat.config.Config(neat.DefaultGenome,
                                neat.DefaultReproduction,
                                neat.DefaultSpeciesSet,
                                neat.DefaultStagnation,
                                config_file)

    # Create a neat.population.Population object using the Config object created above
    neat_pop = neat.population.Population(config)

    # show the summary statistics of the learning progress
    neat_pop.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    neat_pop.add_reporter(stats)

    # Call the run method on the Population object, giving it your fitness function and (optionally) the maximum number of generations you want NEAT to run
    neat_pop.run(main, max_gen)

    # get the most fit genome genome as our winner with the statistics.best_genome() function
    winner = stats.best_genome()

    # visualize the results
    # node_names = {-1: 'delta_x', -2: 'delta_y_top', -3: 'delta_y_bottom', 0: 'Jump or Not'}
    # draw_net(config, winner, True, node_names=node_names)
    # plot_stats(stats, ylog=False, view=True)
    # plot_species(stats, view=True)

    # show the final statistics
    print('\nBest genome:\n{!s}'.format(winner))


# run the game!
if __name__ == '__main__':
    config_file = 'config-feedforward.txt'
    run_NEAT(config_file)
