import random

class Food:
    def __init__(self, game):
        self.position = (0, 0)
        self.game = game
        self.place()

    def place(self):
        while True:
            self.position = (random.randint(0, 19), random.randint(0, 19))
            if self.position not in self.game.snake.body:
                break