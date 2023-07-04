import pygame

class Controller:
    def __init__(self, game):
        self.game = game

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.end_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.game.snake.change_direction('UP')
                elif event.key == pygame.K_DOWN:
                    self.game.snake.change_direction('DOWN')
                elif event.key == pygame.K_LEFT:
                    self.game.snake.change_direction('LEFT')
                elif event.key == pygame.K_RIGHT:
                    self.game.snake.change_direction('RIGHT')
