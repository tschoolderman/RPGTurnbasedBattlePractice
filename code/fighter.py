import pygame as pg

from entity import Entity


class Fighter(Entity):
    """Creating the player hero."""

    def __init__(self, groups) -> None:
        super().__init__(groups)
        # general setup
        self.display_surface = pg.display.get_surface()

        # player stats
        self.name = "Hero"
        self.max_hp = 30
        self.current_hp = self.max_hp
        self.strength = 10
        self.start_potions = 3

        # graphic
        self.import_graphics("knight")
        self.image = self.animations[self.action][self.frame_index]
        self.rect = self.image.get_rect(center=(150, 205))

    def draw_fighter(self):
        # enlarge the image by factor 3
        self.image = pg.transform.scale(
            self.image,
            (self.image.get_width() * 3, self.image.get_height() * 3),
        )

        self.display_surface.blit(self.image, self.rect)

    def animate(self):
        animation = self.animations[self.action]
        self.image = animation[int(self.frame_index)]

        if pg.time.get_ticks() - self.update_time > self.animation_cooldown:
            self.update_time = pg.time.get_ticks()
            self.frame_index += 1

        if self.frame_index >= len(animation):
            self.frame_index = 0

        # after certain action set back to idle or fixed image (death)

    def update(self):
        self.animate()
