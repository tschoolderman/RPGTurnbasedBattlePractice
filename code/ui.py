import pygame as pg

from config import (
    BAR_HEIGHT,
    BAR_WIDTH,
    HEALTH_COLOR,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    UI_BG_COLOR,
    UI_BORDER_COLOR,
    UI_FONT,
    UI_FONT_SIZE,
)


class UI:
    """Class for creating the user interface."""

    def __init__(self) -> None:
        self.display_surface = pg.display.get_surface()

        self.font = pg.font.Font(UI_FONT, UI_FONT_SIZE)

        self.health_bar_rect = pg.Rect(
            (SCREEN_WIDTH // 16),
            (SCREEN_HEIGHT + 40),
            BAR_WIDTH,
            BAR_HEIGHT,
        )

    def draw_text(self, text, x, y):
        text_surface = self.font.render(text, False, HEALTH_COLOR)
        self.display_surface.blit(text_surface, (x, y))

    def draw_party_healthbar(self, current_hp, max_hp, bg_rect, color):
        """Defining the party healthbars."""
        pg.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)

        ratio = current_hp / max_hp
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        pg.draw.rect(self.display_surface, color, current_rect)

        pg.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)

    def draw_enemy_healthbar(self, current_hp, max_hp, bg_rect, color):
        """Defining the enemy healthbars."""
        pg.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)

        current_width = bg_rect.width * (current_hp / max_hp)
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        pg.draw.rect(self.display_surface, color, current_rect)

        pg.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)

    def display_party(self, party):
        """Displaying the party healthbars."""
        self.draw_party_healthbar(
            party.current_hp, party.max_hp, self.health_bar_rect, HEALTH_COLOR
        )
        self.draw_text(
            f"{party.name} HP: {party.current_hp}",
            (SCREEN_WIDTH // 16),
            (SCREEN_HEIGHT + 10),
        )

    def display_enemy(self, enemy, offset):
        """Displaying the enemy healthbars."""
        self.enemy_health_rect = pg.Rect(
            (SCREEN_WIDTH // 1.8), (SCREEN_HEIGHT + offset), BAR_WIDTH, BAR_HEIGHT
        )
        self.draw_enemy_healthbar(
            enemy.current_hp,
            enemy.max_hp,
            self.enemy_health_rect,
            HEALTH_COLOR,
        )
        self.draw_text(
            f"{enemy.name} HP: {enemy.current_hp}",
            (SCREEN_WIDTH // 1.8),
            ((SCREEN_HEIGHT - 30) + offset),
        )
