import random
import sys
import pygame
from pygame.locals import *


class FlappyBirdGame:
    def __init__(self, config, image_loader):
        self.config = config
        self.image_loader = image_loader

        # Initialize the game window dimensions and other settings
        self.window_width = 600
        self.window_height = 600
        self.elevation = self.window_height * 0.8
        self.fps = 32
        self.pipeimage = 'images/pipe.png'
        self.background_image = 'images/background.jpg'
        self.birdplayer_image = 'images/bird.png'
        self.sealevel_image = 'images/base.jfif'
        self.game_images = {}

    def initialize_game(self):
        pygame.init()
        self.fps_clock = pygame.time.Clock()
        self.window = pygame.display.set_mode(
            (self.config.window_width, self.config.window_height))
        pygame.display.set_caption('Flappy Bird Clone')
        self.image_loader.load_images(self.config)
        self.game_images = self.image_loader.game_images
        self.fps_clock = pygame.time.Clock()
        self.window = pygame.display.set_mode(
            (self.window_width, self.window_height))
        pygame.display.set_caption('Flappy Bird Clone')

    def run(self):
        self.initialize_game()
        while True:
            self.start_game_loop()

    def start_game_loop(self):
        horizontal = int(self.window_width / 5)
        vertical = int(
            (self.window_height - self.game_images['flappybird'].get_height()) / 2)
        ground = 0

        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                    self.flappy_game()
                else:
                    self.window.blit(self.game_images['background'], (0, 0))
                    self.window.blit(
                        self.game_images['flappybird'], (horizontal, vertical))
                    self.window.blit(
                        self.game_images['sea_level'], (ground, self.elevation))
                    pygame.display.update()
                    self.fps_clock.tick(self.fps)

    def flappy_game(self):
        your_score = 0
        horizontal = int(self.window_width / 5)
        vertical = int(self.window_width / 2)
        ground = 0
        mytempheight = 100

        first_pipe = self.create_pipe()
        second_pipe = self.create_pipe()

        down_pipes = [
            {'x': self.window_width + 300 -
                mytempheight, 'y': first_pipe[1]['y']},
            {'x': self.window_width + 300 - mytempheight +
                (self.window_width / 2), 'y': second_pipe[1]['y']}
        ]

        up_pipes = [
            {'x': self.window_width + 300 -
                mytempheight, 'y': first_pipe[0]['y']},
            {'x': self.window_width + 200 - mytempheight +
                (self.window_width / 2), 'y': second_pipe[0]['y']}
        ]

        pipe_velocity_x = -4
        bird_velocity_y = -9
        bird_max_vel_y = 10
        bird_min_vel_y = -8
        bird_vertical_accel = 1
        bird_flap_velocity = -8
        bird_flapped = False

        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                    if vertical > 0:
                        bird_velocity_y = bird_flap_velocity
                        bird_flapped = True

            game_over = self.is_game_over(
                horizontal, vertical, up_pipes, down_pipes)
            if game_over:
                if your_score < 3:
                    print(f"{your_score} points? Did you even try?")
                else:
                    print(f"Game over! Your score was {your_score}!")
                return

            player_mid_pos = horizontal + \
                self.game_images['flappybird'].get_width() / 2
            for pipe in up_pipes:
                pipe_mid_pos = pipe['x'] + \
                    self.game_images['pipeimage'][0].get_width() / 2
                if pipe_mid_pos <= player_mid_pos < pipe_mid_pos + 4:
                    your_score += 1
                    if your_score == 50:
                        print(f"{your_score}? You're better than most.")
                    elif your_score == 25:
                        print(f"Wow! You went through {your_score} pipes!")
                    elif your_score % 10 == 0:
                        print(f"Your score is {your_score}!")

            if bird_velocity_y < bird_max_vel_y and not bird_flapped:
                bird_velocity_y += bird_vertical_accel

            if bird_flapped:
                bird_flapped = False

            playerHeight = self.game_images['flappybird'].get_height()
            vertical = vertical + \
                min(bird_velocity_y, self.elevation - vertical - playerHeight)

            for upperPipe, lowerPipe in zip(up_pipes, down_pipes):
                upperPipe['x'] += pipe_velocity_x
                lowerPipe['x'] += pipe_velocity_x

            if 0 < up_pipes[0]['x'] < 5:
                newpipe = self.create_pipe()
                up_pipes.append(newpipe[0])
                down_pipes.append(newpipe[1])

            if up_pipes[0]['x'] < -self.game_images['pipeimage'][0].get_width():
                up_pipes.pop(0)
                down_pipes.pop(0)

            self.window.blit(self.game_images['background'], (0, 0))
            for upperPipe, lowerPipe in zip(up_pipes, down_pipes):
                self.window.blit(
                    self.game_images['pipeimage'][0], (upperPipe['x'], upperPipe['y']))
                self.window.blit(
                    self.game_images['pipeimage'][1], (lowerPipe['x'], lowerPipe['y']))

            self.window.blit(
                self.game_images['sea_level'], (ground, self.elevation))
            self.window.blit(
                self.game_images['flappybird'], (horizontal, vertical))

            numbers = [int(x) for x in list(str(your_score))]
            width = 0
            for num in numbers:
                width += self.game_images['scoreimages'][num].get_width()
            x_offset = (self.window_width - width) / 1.1
            for num in numbers:
                self.window.blit(
                    self.game_images['scoreimages'][num], (x_offset, self.window_width * 0.02))
                x_offset += self.game_images['scoreimages'][num].get_width()

            pygame.display.update()
            self.fps_clock.tick(self.fps)

    def create_pipe(self):
        # Create a pair of pipes with random heights
        offset = self.window_height / 3
        pipe_height = self.game_images['pipeimage'][0].get_height()
        y2 = offset + random.randrange(0, int(self.window_height -
                                       self.game_images['sea_level'].get_height() - 1.2 * offset))
        pipe_x = self.window_width + 10
        y1 = pipe_height - y2 + offset
        pipe = [
            {'x': pipe_x, 'y': -y1},  # Upper Pipe
            {'x': pipe_x, 'y': y2}    # Lower Pipe
        ]
        return pipe

    def is_game_over(self, horizontal, vertical, up_pipes, down_pipes):
        # Check if the game is over (collision with pipes or ground)
        if vertical > self.elevation - 25 or vertical < 0:
            return True
        for pipe in up_pipes:
            pipe_height = self.game_images['pipeimage'][0].get_height()
            if (vertical < pipe_height + pipe['y'] and abs(horizontal - pipe['x']) < self.game_images['pipeimage'][0].get_width()):
                return True
        for pipe in down_pipes:
            if (vertical + self.game_images['flappybird'].get_height() > pipe['y']) and abs(horizontal - pipe['x']) < self.game_images['pipeimage'][0].get_width():
                return True
        return False
