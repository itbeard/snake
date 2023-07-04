import pygame
from controller import Controller
from game import Game
from view import View

def main():
    pygame.init()
    clock = pygame.time.Clock()  # create a clock object
    game = Game()
    controller = Controller(game)
    view = View(game)

    while game.is_running:
        controller.process_input()
        game.update()
        view.draw()
        clock.tick(10)  # set your game to run at 10 frames per second

    pygame.quit()

if __name__ == "__main__":
    main()