import pygame


class ImageLoader:
    def __init__(self):
        self.game_images = {}

    def load_images(self, config):
        # Load all the game images required
        self.game_images['scoreimages'] = [pygame.image.load(
            f'images/{i}.png').convert_alpha() for i in range(10)]
        self.game_images['flappybird'] = pygame.image.load(
            config.bird_image).convert_alpha()
        self.game_images['sea_level'] = pygame.image.load(
            config.sea_level_image).convert_alpha()
        self.game_images['background'] = pygame.image.load(
            config.background_image).convert_alpha()
        self.game_images['pipeimage'] = (
            pygame.transform.rotate(pygame.image.load(
                config.pipe_image).convert_alpha(), 180),
            pygame.image.load(config.pipe_image).convert_alpha()
        )

    def get_image(self, key):
        return self.game_images.get(key)
