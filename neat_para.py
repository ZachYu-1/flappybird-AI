generation = 0
max_gen = 100  # the maximum number of generation
prob_threshold_to_jump = 0.8  # the probability threshold to jump
failed_punishment = 10  # the punishment after collision

FPS = 30  # run the game at 30 FPS
max_score = 100  # the maximum score to terminate

bird_max_upward_angle = 35  # the maximum upward angle
bird_max_downward_angle = -35  # the maximum downward angle
bird_min_incremental_angle = 4  # the minimum incremental angle
bird_angular_acceleration = 0.1  # the angular of bird
bird_jump_velocity = -8  # the jump up velocity
bird_acceleration = 3  # the gravity
bird_max_displacement = 12  # the maximum displacement per frame
bird_starting_x_position = 150  # the starting position
bird_starting_y_position = 250  # the starting position

floor_velocity = 4  # the moving velocity
floor_starting_y_position = 400  # the starting position

pipe_max_num = 100  # equals to the maximum score
pipe_vertical_gap = 100  # the gap between a set of pipes
pipe_horizontal_gap = 160  # the gap between two sets of pipes
pipe_velocity = 4  # the velocity of moving pipes
top_pipe_min_height = 100  # the minimum height of the top pipe
top_pipe_max_height = 250  # the maximum height of the top pipe
pipe_starting_x_position = 300  # the starting position