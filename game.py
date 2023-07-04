from snake import Snake
from food import Food

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food(self)
        self.is_running = True

    def update(self):
        self.snake.move()
        if self.snake.check_collision() or not(0 <= self.snake.body[0][0] < 20 and 0 <= self.snake.body[0][1] < 20):
            self.end_game()
        elif self.snake.eat(self.food):
            self.snake.grow()
            self.food.place()

    def end_game(self):
        self.is_running = False

