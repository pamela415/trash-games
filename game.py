import pygame
import random
import time

FPS = 50
WIDTH, HEIGHT = 800, 600
TOTAL_TRASH = 50

class Backdrop(pygame.sprite.Sprite):
    """Coral reef backdrop"""
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("assets/coralreef.jpg")

        self.rect = self.image.get_rect()


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




class Game():
    def __init__(self):
        pygame.init()
        self.font_name = pygame.font.match_font('arial')

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.running = True

        self.score = 0

        self.count_down = 3200

        self.backdrop = Backdrop()

        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.backdrop)

        self.trash_types = ["bag", "bottle"]
        self.trash_pieces = pygame.sprite.Group()

        for x in range(50):
            trash_piece = Trash(random.choice(self.trash_types))
            self.trash_pieces.add(trash_piece)
    
    
    def draw_text(self, surf, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True,(250,250,250))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    def check_status(self):
        self.count_down -= 1

        print(self.count_down)

        if self.score == 50:
            print("Good Job")
            self.running = False
        elif self.count_down == 0:
            print("try again")
            self.running = False



    def update(self):
        self.clock.tick(FPS)

        self.handle_input()

        self.check_status()

        self.sprites.update()
        self.sprites.draw(self.screen)

        self.trash_pieces.update()
        self.trash_pieces.draw(self.screen)

        self.draw_text(self.screen, str(self.score), 48, WIDTH / 2, 10)

        pygame.display.flip()

    def handle_input(self):
        """Updates the input dictionary"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                for trash_piece in self.trash_pieces:
                    if trash_piece.rect.collidepoint(pos):
                        self.score += 1
                        self.trash_pieces.remove(trash_piece)
                        print(self.score)
    
    


def main():
    """Main entry point for script"""
    game = Game()

    while game.running:
        game.update()


if __name__ == "__main__":
    main()