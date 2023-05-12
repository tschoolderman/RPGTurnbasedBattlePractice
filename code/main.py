import sys

import pygame as pg

from config import BOTTOM_PANEL, FPS, SCREEN_HEIGHT, SCREEN_WIDTH
from level import Level


class Game:
    """Base class to run the game."""

    def __init__(self) -> None:
        # general setup
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + BOTTOM_PANEL))
        pg.display.set_caption("Turn Based Battle")
        self.clock = pg.time.Clock()

        # initializing the game level
        self.level = Level()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.screen.fill("black")
            self.level.run()
            pg.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
