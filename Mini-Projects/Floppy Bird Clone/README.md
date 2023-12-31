# Flappy Bird Clone in Python
This Python program emulates the popular Flappy Bird game using the Pygame library. The code encompasses functions for initializing the game, rendering graphical elements, and handling player input. Throughout the game loop, the player guides a bird through a series of pipes while avoiding collisions. The game runs continuously until it determines that the game is over, at which point the player's score is displayed. The code also incorporates image loading, game parameter configuration, and a simple start screen that starts the game when the player presses the spacebar key.

![Floppy Bird Clone Screenshot](https://github.com/c0olade/Software-Engineering-Journey/blob/main/Mini-Projects/Floppy%20Bird%20Clone/images/Flappy.gif)

## Planning and Implementing the Code
This project was based off of a Geeksforgeeks article on how to build the [flappy bird game](https://www.geeksforgeeks.org/how-to-make-flappy-bird-game-in-pygame/). 

The original code only had functions (refer to [original.py](https://github.com/c0olade/Software-Engineering-Journey/blob/main/Mini-Projects/Floppy%20Bird%20Clone/original.py)). I spent time to understand what was going on and decided to break it out into classes for the game, the config, and loading images. After I made the class updates, I decided to split up the classes into separate files instead:
- config.py
- game.py
- image_loader.py
- main.py
- requirements.txt

The files you see are the updates as of 10/17/2023. Thinking back, I should've have created additional classes within the game file. If I were to do it again, I would create the following classes and the associated methods in the game.py file:
- FlappyBird
  - initialize_game
  - run
  - start_game_loop
  - is_game_over
  - end_game
- Bird
  - flap
  - update
  - draw
  - is_colliding
- Pipe
  - update
  - draw

## Getting Started

1. **Prerequisites:**
   - Python: Ensure you have Python installed on your system.
   - Pygame: Install the Pygame library by running `pip install pygame`.

2. **Clone the Repository:**
   ```shell
   git clone https://github.com/your-username/flappy-bird-clone.git
   cd flappy-bird-clone
3. **Run the Game:**
   ```shell
   python main.py
   ```

## License
This project is licensed under the MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Thank you
Thank you to bansalshubhamcse21 who wrote the article on Geeksforgeeks.
