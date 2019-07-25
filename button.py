import pygame
from constants import *

class Button(pygame.sprite.Sprite):
    """buttons"""
    def __init__(self, button_type):
        super().__init__()

        self.images = {}
        self.images[START_BUTTON] = pygame.image.load(
            "assets/start_button.png"
        )
        self.images[INSTRUCTIONS_BUTTON] = pygame.image.load(
            "assets/instructions_button.png"
        )
        self.images[PLAY_AGAIN] = pygame.image.load(
            "assets/play_again.png"
        )
        self.images[TITLE] = pygame.image.load(
            "assets/title.png"
        )
        self.images[BACK] = pygame.image.load(
            "assets/back_button.png"
        )
        self.images[PASSED_SCREEN] = pygame.image.load(
            "assets/passed.png"
        )
        self.images[GAME_FAILED] = pygame.image.load(
            "assets/failed.png"
        )
        self.image = self.images[button_type]

        self.rect = self.image.get_rect()

        self.button_type = button_type

    def set_pos(self, x, y):
        self.x = x
        self.y = y
        self.rect.x = self.x - self.rect.w / 2
        self.rect.y = self.y - self.rect.h / 2
