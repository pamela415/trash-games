import pygame
import random
import time
from backdrop import Backdrop
from trash import Trash
from constants import *
from button import Button


class Game():
    def __init__(self):
        pygame.init()
        self.font_name = pygame.font.match_font('arial')

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.running = True

        self.game_section = START

        self.score = 0

        self.count_down = COUNT_DOWN

        self.backdrop = Backdrop()

        self.backdrops = pygame.sprite.Group()
        self.backdrops.add(self.backdrop)

        self.start_button = Button(START_BUTTON)
        self.start_button.set_pos(WIDTH / 2, HEIGHT / 2 - 30)

        self.instructions_button = Button(INSTRUCTIONS_BUTTON)
        self.instructions_button.set_pos(WIDTH / 2, HEIGHT / 2 + 30)

        self.beginning_buttons = pygame.sprite.Group()
        self.beginning_buttons.add(self.start_button)
        self.beginning_buttons.add(self.instructions_button)

        self.play_again = Button(PLAY_AGAIN)
        self.play_again.set_pos(WIDTH / 2, HEIGHT / 2 + 200)

        self.end_buttons = pygame.sprite.Group()
        self.end_buttons.add(self.play_again)

        self.trash_types = ["bag", "bottle"]
        self.trash_pieces = pygame.sprite.Group()

        self.restart_game()

    def restart_game(self):
        self.score = 0
        self.count_down = COUNT_DOWN

        self.trash_pieces.empty()

        print("Restart")

        for x in range(50):
            trash_piece = Trash(random.choice(self.trash_types))
            self.trash_pieces.add(trash_piece)

    def draw_text(self, surf, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True,(250,250,250))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    # def text_objects(self, text, font):
    #     textSurface = font.render(text, True, black)
    #     return textSurface, textSurface.get_rect()

    # def message_display(self, text):
    #     largeText = pygame.font.Font('freesansbold.ttf',115)
    #     TextSurf, TextRect = text_objects(text, largeText)
    #     # TextRect.center = ((display_width/2),(display_height/2))
    #     # gameDisplay.blit(TextSurf, TextRect)

    def check_status(self):
        self.count_down -= 1

        if self.score == 50:
            self.game_section = PASSED
        elif self.count_down == 0:
            self.game_section = FAILED

    def update(self):
        self.clock.tick(FPS)

        self.handle_input()

        if self.game_section == START:
            self.backdrops.update()
            self.backdrops.draw(self.screen)
            
            self.beginning_buttons.update()
            self.beginning_buttons.draw(self.screen)

        elif self.game_section == PLAY:
            self.check_status()

            self.backdrops.update()
            self.backdrops.draw(self.screen)

            self.trash_pieces.update()
            self.trash_pieces.draw(self.screen)

            self.draw_text(self.screen, str(self.score), 48, WIDTH / 2, 10)

        elif self.game_section == INSTRUCTIONS:
            self.backdrops.update()
            self.backdrops.draw(self.screen)

        elif self.game_section == PASSED:
            self.backdrops.update()
            self.backdrops.draw(self.screen)

            self.end_buttons.update()
            self.end_buttons.draw(self.screen)

        elif self.game_section == FAILED:
            self.backdrops.update()
            self.backdrops.draw(self.screen)

            self.end_buttons.update()
            self.end_buttons.draw(self.screen)

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

                if self.game_section == START:
                    for button in self.beginning_buttons:
                        if button.rect.collidepoint(pos):
                            if button.button_type == START_BUTTON:
                                self.game_section = PLAY
                            elif button.button_type == INSTRUCTIONS_BUTTON:
                                self.game_section = INSTRUCTIONS
                                print("hi") 

                elif self.game_section == INSTRUCTIONS:
                    pass
                    
                elif self.game_section == PLAY:
                    for trash_piece in self.trash_pieces:
                        if trash_piece.rect.collidepoint(pos):
                            self.score += 1
                            self.trash_pieces.remove(trash_piece)
                            
                elif self.game_section == PASSED:
                    for button in self.end_buttons:
                        if button.rect.collidepoint(pos):
                            if button.button_type == PLAY_AGAIN:
                                self.restart_game()
                                self.game_section = PLAY

                elif self.game_section == FAILED:
                    for button in self.end_buttons:
                        if button.rect.collidepoint(pos):
                            if button.button_type == PLAY_AGAIN:
                                self.restart_game()
                                self.game_section = PLAY
    
    


def main():
    """Main entry point for script"""
    game = Game()

    while game.running:
        game.update()


if __name__ == "__main__":
    main()