import pygame
from constants import *

class Backdrop(pygame.sprite.Sprite):
    """Coral reef backdrop"""
    def __init__(self, backdrop_type):
        super().__init__()

        self.images = {}
        self.images[INSTRUCTIONS_BACKDROP] = pygame.image.load(
            "assets/instructions_backdrop.jpg"
        )
        self.images[BACKDROP] = pygame.image.load(
            "assets/standard_backdrop.jpg"
        )
        
        self.image = self.images[backdrop_type]

        self.rect = self.image.get_rect()

