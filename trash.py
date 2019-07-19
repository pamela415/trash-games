import pygame
import random
from constants import WIDTH, HEIGHT

class Trash(pygame.sprite.Sprite):
    """pieces of trash"""
    def __init__(self, trash_type):
        super().__init__()

        self.images = {}
        self.images["bag"] = pygame.image.load(
            "assets/plasticbag.png"
        )
        self.images["bottle"] = pygame.image.load(
            "assets/bottle.png"
        )

        self.image = self.images[trash_type]

        self.rect = self.image.get_rect()

        self.rect.x = random.randint(30, WIDTH - 70)
        self.rect.y = random.randint(30, HEIGHT - 70)