import pygame

class View:
    def __init__(self, game):
        self.game = game
        pygame.init()
        self.window = pygame.display.set_mode((400, 400))

    def draw(self):
        self.window.fill((0, 0, 0))

        for segment in self.game.snake.body:
            pygame.draw.rect(self.window, (0, 255, 0), (segment[0]*20, segment[1]*20, 20, 20))

        pygame.draw.rect(self.window, (255, 0, 0), (self.game.food.position[0]*20, self.game.food.position[1]*20, 20, 20))
        pygame.display.flip()
