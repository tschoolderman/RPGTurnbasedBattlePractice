import pygame as pg

from support import import_folder


class Entity(pg.sprite.Sprite):
    def __init__(self, groups) -> None:
        super().__init__(groups)
        # check entity status
        self.alive = True
        self.action = "idle"

        # movement
        self.frame_index = 0
        self.update_time = pg.time.get_ticks()
        self.animation_cooldown = 100

    def import_graphics(self, name):
        image_path = f"../graphic/{name}/"
        self.animations = {
            "idle": [],
            "attack": [],
            "hurt": [],
            "death": [],
        }
        for animation in self.animations.keys():
            main_path = image_path + animation
            self.animations[animation] = import_folder(main_path)

    def idle(self):
        self.action = "idle"
        self.animate()

    def attack(self):
        self.action = "attack"
        self.animate()

    def hurt(self):
        self.action = "hurt"
        self.animate()

    def death(self):
        self.action = "death"
        self.animate()
