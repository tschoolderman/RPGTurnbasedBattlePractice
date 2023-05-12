import pygame as pg

from entity import Entity


class Bandit(Entity):
    """Creating the player hero."""

    def __init__(self, groups) -> None:
        super().__init__(groups)
        # general setup
        self.display_surface = pg.display.get_surface()
        self.x = None
        self.y = None

        # player stats
        self.name = "Bandit"
        self.max_hp = 20
        self.current_hp = self.max_hp
        self.strength = 6
        self.start_potions = 1

        # graphic
        self.import_graphics("bandit")
        self.image = self.animations[self.action][self.frame_index]

    def draw_bandit(self, x, y):
        # enlarge the image by factor 3
        self.x = x
        self.y = y
        self.image = pg.transform.scale(
            self.image,
            (self.image.get_width() * 3, self.image.get_height() * 3),
        )
        self.rect = self.image.get_rect(center=(x, y))

        self.display_surface.blit(self.image, self.rect)

    def animate(self):
        animation = self.animations[self.action]
        self.image = animation[int(self.frame_index)]

        if pg.time.get_ticks() - self.update_time > self.animation_cooldown:
            self.update_time = pg.time.get_ticks()
            self.frame_index += 1

        if self.frame_index >= len(animation):
            self.frame_index = 0

    def update(self):
        self.animate()
