import random
import sys
import pygame
from pygame.locals import *

# Game window dimensions
window_width = 600
window_height = 499

# Initialize the game window
window = pygame.display.set_mode((window_width, window_height))
elevation = window_height * 0.8  # Set the elevation for the ground
game_images = {}  # Dictionary to store game images
framepersecond = 32  # Frames per second for the game
pipeimage = 'images/pipe.png'  # Path to the pipe image
background_image = 'images/background.jpg'  # Path to the background image
birdplayer_image = 'images/bird.png'  # Path to the bird player image
sealevel_image = 'images/base.jfif'  # Path to the ground (sea level) image

# Define the main game function


def flappygame():
    your_score = 0
    horizontal = int(window_width / 5)
    vertical = int(window_width / 2)
    ground = 0
    mytempheight = 100

    # Generate two pipes for blitting on the window
    first_pipe = createPipe()
    second_pipe = createPipe()

    # Lists containing lower and upper pipes
    down_pipes = [
        {'x': window_width + 300 - mytempheight,
         'y': first_pipe[1]['y']},
        {'x': window_width + 300 - mytempheight + (window_width / 2),
         'y': second_pipe[1]['y']},
    ]
    up_pipes = [
        {'x': window_width + 300 - mytempheight,
         'y': first_pipe[0]['y']},
        {'x': window_width + 200 - mytempheight + (window_width / 2),
         'y': second_pipe[0]['y']},
    ]

    # Pipe velocity along x
    pipeVelX = -4

    # Bird velocity and parameters
    bird_velocity_y = -9
    bird_Max_Vel_Y = 10
    bird_Min_Vel_Y = -8
    birdAccY = 1
    bird_flap_velocity = -8
    bird_flapped = False

    while True:
        # Iterate through the list of events that have occurred
        for event in pygame.event.get():
            # Check if the event type is a window close event (e.g., clicking the 'X' button)
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                # If the window close event is detected, exit the game
                pygame.quit()  # Terminate the Pygame engine
                sys.exit()  # Terminate the script

            # Check if the event type is a key press event
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                # If the player presses the spacebar or the up arrow key
                if vertical > 0:
                    # Check if the bird's vertical position is above the screen (not at the top)
                    # Set the bird's vertical velocity to flap upwards
                    bird_velocity_y = bird_flap_velocity
                    bird_flapped = True  # Mark that the bird has flapped

        # Check if the game is over
        game_over = isGameOver(horizontal, vertical, up_pipes, down_pipes)
        if game_over:
            return

        # Check for your_score
        playerMidPos = horizontal + game_images['flappybird'].get_width() / 2
        for pipe in up_pipes:
            pipeMidPos = pipe['x'] + \
                game_images['pipeimage'][0].get_width() / 2
            if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                your_score += 1
                print(f"Your your_score is {your_score}")

        if bird_velocity_y < bird_Max_Vel_Y and not bird_flapped:
            bird_velocity_y += birdAccY

        if bird_flapped:
            bird_flapped = False
        playerHeight = game_images['flappybird'].get_height()
        vertical = vertical + \
            min(bird_velocity_y, elevation - vertical - playerHeight)

        # Move pipes to the left
        for upperPipe, lowerPipe in zip(up_pipes, down_pipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX

        # Add a new pipe when the first is about to cross the leftmost part of the screen
        if 0 < up_pipes[0]['x'] < 5:
            newpipe = createPipe()
            up_pipes.append(newpipe[0])
            down_pipes.append(newpipe[1])

        # If the pipe is out of the screen, remove it
        if up_pipes[0]['x'] < -game_images['pipeimage'][0].get_width():
            up_pipes.pop(0)
            down_pipes.pop(0)

        # Blit game images on the window
        window.blit(game_images['background'], (0, 0))
        for upperPipe, lowerPipe in zip(up_pipes, down_pipes):
            window.blit(game_images['pipeimage'][0],
                        (upperPipe['x'], upperPipe['y']))
            window.blit(game_images['pipeimage'][1],
                        (lowerPipe['x'], lowerPipe['y']))

        window.blit(game_images['sea_level'], (ground, elevation))
        window.blit(game_images['flappybird'], (horizontal, vertical))

        # Fetch the digits of the score
        numbers = [int(x) for x in list(str(your_score))]
        width = 0

        # Find the width of score images from numbers
        for num in numbers:
            width += game_images['scoreimages'][num].get_width()
        Xoffset = (window_width - width) / 1.1

        # Blit the score images on the window
        for num in numbers:
            window.blit(game_images['scoreimages'][num],
                        (Xoffset, window_width * 0.02))
            Xoffset += game_images['scoreimages'][num].get_width()

        # Refresh the game window and display the score
        pygame.display.update()
        framepersecond_clock.tick(framepersecond)

# Function to check if the game is over


def isGameOver(horizontal, vertical, up_pipes, down_pipes):
    if vertical > elevation - 25 or vertical < 0:
        return True

    for pipe in up_pipes:
        pipeHeight = game_images['pipeimage'][0].get_height()
        if (vertical < pipeHeight + pipe['y'] and abs(horizontal - pipe['x']) < game_images['pipeimage'][0].get_width()):
            return True

    for pipe in down_pipes:
        if (vertical + game_images['flappybird'].get_height() > pipe['y']) and abs(horizontal - pipe['x']) < game_images['pipeimage'][0].get_width():
            return True
    return False

# Function to create a pair of pipes


def createPipe():
    offset = window_height / 3
    pipeHeight = game_images['pipeimage'][0].get_height()
    y2 = offset + random.randrange(0, int(window_height -
                                   game_images['sea_level'].get_height() - 1.2 * offset))
    pipeX = window_width + 10
    y1 = pipeHeight - y2 + offset
    pipe = [
        # Upper Pipe
        {'x': pipeX, 'y': -y1},
        # Lower Pipe
        {'x': pipeX, 'y': y2}
    ]
    return pipe


# Entry point of the program
if __name__ == "__main__":
    pygame.init()  # Initialize pygame

    # Initialize the Pygame clock for controlling frame rate
    framepersecond_clock = pygame.time.Clock()

    # Set the title on top of the game window
    pygame.display.set_caption('Flappy Bird Clone')

    # Load all the images required for the game

    # Load images for displaying the score
    game_images['scoreimages'] = (
        pygame.image.load('images/0.png').convert_alpha(),
        pygame.image.load('images/1.png').convert_alpha(),
        pygame.image.load('images/2.png').convert_alpha(),
        pygame.image.load('images/3.png').convert_alpha(),
        pygame.image.load('images/4.png').convert_alpha(),
        pygame.image.load('images/5.png').convert_alpha(),
        pygame.image.load('images/6.png').convert_alpha(),
        pygame.image.load('images/7.png').convert_alpha(),
        pygame.image.load('images/8.png').convert_alpha(),
        pygame.image.load('images/9.png').convert_alpha()
    )

    # Load the image of the flappy bird player
    game_images['flappybird'] = pygame.image.load(
        birdplayer_image).convert_alpha()

    # Load the image of the ground (sea level)
    game_images['sea_level'] = pygame.image.load(
        sealevel_image).convert_alpha()

    # Load the background image
    game_images['background'] = pygame.image.load(
        background_image).convert_alpha()

    # Load the image of the pipe
    game_images['pipeimage'] = (pygame.transform.rotate(pygame.image.load(
        pipeimage).convert_alpha(), 180), pygame.image.load(
        pipeimage).convert_alpha())

    print("WELCOME TO THE FLAPPY BIRD GAME")
    print("Press space or enter to start the game")

    # Main game loop
    while True:

        # Set the initial coordinates of the flappy bird
        horizontal = int(window_width / 5)
        vertical = int(
            (window_height - game_images['flappybird'].get_height()) / 2)
        ground = 0

        # Game start event loop
        while True:
            for event in pygame.event.get():
                # If the user clicks on the close button, exit the game
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                # If the user presses space or up key, start the game
                elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                    flappygame()
                # If the user doesn't press any key, do nothing
                else:
                    window.blit(game_images['background'], (0, 0))
                    window.blit(game_images['flappybird'],
                                (horizontal, vertical))
                    window.blit(game_images['sea_level'], (ground, elevation))
                    pygame.display.update()
                    framepersecond_clock.tick(framepersecond)
