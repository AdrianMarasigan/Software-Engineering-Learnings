from config import Config
from image_loader import ImageLoader
from game import FlappyBirdGame

if __name__ == "__main__":
    config = Config()
    image_loader = ImageLoader(config)
    game = FlappyBirdGame(config, image_loader)
    game.run()
