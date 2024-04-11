# define a function to draw the screen to display the game
import pygame

from bird import Bird
from init import SCREEN_WIDTH, FONT_COLOR, BG_IMG, FONT


def draw_game(screen, birds, pipes, floor, score, generation):
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
    score_text = FONT.render('Score: ' + str(score), 1, FONT_COLOR)  # set up the text to show the scores
    screen.blit(score_text, (SCREEN_WIDTH - 15 - score_text.get_width(), 15))  # draw the scores

    generation_text = FONT.render('Generation: ' + str(generation - 1), 1,
                                  FONT_COLOR)  # set up the text to show the number of generation
    screen.blit(generation_text, (15, 15))  # draw the generation

    bird_text = FONT.render('Birds Alive: ' + str(len(birds)), 1,
                            FONT_COLOR)  # set up the text to show the number of birds alive
    screen.blit(bird_text, (15, 15 + generation_text.get_height()))  # draw the number of birds alive

    progress_text = FONT.render('Pipes Remained: ' + str(len(pipes) - score), 1,
                                FONT_COLOR)  # set up the text to show the progress
    screen.blit(progress_text, (15, 15 + generation_text.get_height() + bird_text.get_height()))  # draw the progress

    pygame.display.update()  # show the surface
