import pygame

class Backdrop(pygame.sprite.Sprite):
    """Coral reef backdrop"""
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("assets/coralreef.jpg")

        self.rect = self.image.get_rect()

