import pygame
from backdrop import Backdrop

class Instructions():
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("assets/coralreef.jpg")

        self.rect = self.image.get_rect()