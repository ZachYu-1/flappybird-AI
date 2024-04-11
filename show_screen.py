# define a function to draw the screen to display the game
import pygame

from init import SCREEN_WIDTH, FONT_COLOR, BG_IMG, FONT


def draw_game(screen, birds, pipes, floor, score, generation, game_time):
    # draw the background
    screen.blit(BG_IMG, (0, 0))

    # draw the moving pipes
    for pipe in pipes:
        screen.blit(pipe.top_pipe_img, (pipe.x, pipe.top_pipe_topleft))  # draw the pipe on the top
        screen.blit(pipe.bottom_pipe_img, (pipe.x, pipe.bottom_pipe_topleft))  # draw the pipe on the bottom

    # draw the moving floor
    screen.blit(floor.IMGS[0], (floor.x1, floor.y))  # draw the first floor image
    screen.blit(floor.IMGS[1], (floor.x2, floor.y))  # draw the second floor image
    screen.blit(floor.IMGS[2], (floor.x3, floor.y))  # draw the third floor image

    # draw the animated birds
    for bird in birds:
        rotated_image, rotated_rect = bird.update()
        screen.blit(rotated_image, rotated_rect)

    # add additional information
    score_text = FONT.render('Score: ' + str(score), 1, FONT_COLOR)  # scores
    screen.blit(score_text, (SCREEN_WIDTH - 15 - score_text.get_width(), 15))

    game_time_text = FONT.render('Time: ' + str(game_time) + ' s', 1, FONT_COLOR)  # time
    screen.blit(game_time_text, (SCREEN_WIDTH - 15 - game_time_text.get_width(), 15 + score_text.get_height()))

    generation_text = FONT.render('Generation: ' + str(generation - 1), 1, FONT_COLOR)  # number of generation
    screen.blit(generation_text, (15, 15))

    bird_text = FONT.render('Birds Alive: ' + str(len(birds)), 1, FONT_COLOR)  # number of birds alive
    screen.blit(bird_text, (15, 15 + generation_text.get_height()))

    pygame.display.update()  # show the surface
