import pygame as pg

from bandit import Bandit
from config import BG_IMAGE, PANEL_IMAGE, SCREEN_HEIGHT
from fighter import Fighter
from ui import UI


class Level:
    """Basic class for running the game."""

    def __init__(self) -> None:
        # get the display surface
        self.display_surface = pg.display.get_surface()

        # sprite group setup
        self.visible_sprites = pg.sprite.Group()

        self.fighter = Fighter([self.visible_sprites])
        self.bandit = Bandit([self.visible_sprites])
        self.bandit1 = Bandit([self.visible_sprites])

        # define ui
        self.ui = UI()

    def draw_background(self):
        """Drawing the background."""
        background = pg.image.load(BG_IMAGE).convert_alpha()
        self.display_surface.blit(background, (0, 0))

    def draw_panel(self):
        """Putting a panel beneath the background image."""
        panel = pg.image.load(PANEL_IMAGE).convert_alpha()
        self.display_surface.blit(panel, (0, SCREEN_HEIGHT))

    def draw_sprites(self):
        self.fighter.draw_fighter()
        self.bandit.draw_bandit(550, 270)
        self.bandit1.draw_bandit(700, 270)

    def run(self):
        self.draw_background()
        self.draw_panel()
        self.ui.display_party(self.fighter)
        self.ui.display_enemy(self.bandit, 40)
        self.ui.display_enemy(self.bandit1, 100)
        self.fighter.idle()
        self.bandit.idle()
        self.bandit1.idle()
        self.draw_sprites()
