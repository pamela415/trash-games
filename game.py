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

        # BACKDROPS

        self.backdrops = pygame.sprite.Group()
        self.instructions_backdrops = pygame.sprite.Group()

        self.standard_backdrop = Backdrop(BACKDROP)
        self.backdrops.add(self.standard_backdrop)

        self.instructions_backdrop = Backdrop(INSTRUCTIONS_BACKDROP)
        self.instructions_backdrops.add(self.instructions_backdrop)

        # BUTTONS
        self.start_button = Button(START_BUTTON)
        self.start_button.set_pos(WIDTH / 2, HEIGHT / 2 + 150)

        self.instructions_button = Button(INSTRUCTIONS_BUTTON)
        self.instructions_button.set_pos(WIDTH / 2, HEIGHT / 2 + 200)

        self.beginning_buttons = pygame.sprite.Group()
        self.beginning_buttons.add(self.start_button)
        self.beginning_buttons.add(self.instructions_button)

        self.play_again = Button(PLAY_AGAIN)
        self.play_again.set_pos(WIDTH / 2, HEIGHT / 2 + 200)

        self.end_buttons = pygame.sprite.Group()
        self.end_buttons.add(self.play_again)

        self.back_button = Button(BACK)
        self.back_button.set_pos(WIDTH / 2, HEIGHT / 2 +150)

        self.back_buttons = pygame.sprite.Group()
        self.back_buttons.add(self.back_button)
        
        self.titles = Button(TITLE)
        self.titles.set_pos(WIDTH / 2, HEIGHT / 2)

        self.title_button = pygame.sprite.Group()
        self.title_button.add(self.titles)

        self.good_job = Button(PASSED_SCREEN)
        self.good_job.set_pos(WIDTH / 2, HEIGHT / 2)

        self.game_passed = pygame.sprite.Group()
        self.game_passed.add(self.good_job)

        self.try_again = Button(GAME_FAILED)
        self.try_again.set_pos(WIDTH / 2, HEIGHT / 2)

        self.game_failed = pygame.sprite.Group()
        self.game_failed.add(self.try_again)

        # TRASH

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

    # DISPLAYED SCORE

    def draw_text(self, surf, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True,(250,250,250))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    def check_status(self):
        self.count_down -= 1

        if self.score == 50:
            self.game_section = PASSED
        elif self.count_down == 0:
            self.game_section = FAILED

    def update(self):
        self.clock.tick(FPS)

        self.handle_input()

    #DESCRIPTION OF GAME SECTIONS

        if self.game_section == START:
            self.backdrops.update()
            self.backdrops.draw(self.screen)

            self.title_button.update()
            self.title_button.draw(self.screen)
            
            self.beginning_buttons.update()
            self.beginning_buttons.draw(self.screen)

        elif self.game_section == PLAY:
            self.check_status()

            self.backdrops.update()
            self.backdrops.draw(self.screen)

            self.trash_pieces.update()
            self.trash_pieces.draw(self.screen)

            self.draw_text(self.screen, str(self.count_down // FPS), 90, WIDTH / 12 , 10)

        elif self.game_section == INSTRUCTIONS:
            self.instructions_backdrops.update()
            self.instructions_backdrops.draw(self.screen)

            self.back_buttons.update()
            self.back_buttons.draw(self.screen)

        elif self.game_section == PASSED:
            self.backdrops.update()
            self.backdrops.draw(self.screen)

            self.end_buttons.update()
            self.end_buttons.draw(self.screen)

            self.game_passed.update()
            self.game_passed.draw(self.screen)

        elif self.game_section == FAILED:
            self.backdrops.update()
            self.backdrops.draw(self.screen)

            self.end_buttons.update()
            self.end_buttons.draw(self.screen)

            self.game_failed.update()
            self.game_failed.draw(self.screen)

        pygame.display.flip()

    # CONTROLS

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

    # WHEN GAME SECTION OCCURS

                if self.game_section == START:
                    for button in self.beginning_buttons:
                        if button.rect.collidepoint(pos):
                            if button.button_type == START_BUTTON:
                                self.game_section = PLAY
                            elif button.button_type == INSTRUCTIONS_BUTTON:
                                self.game_section = INSTRUCTIONS
                                print("hi") 

                elif self.game_section == INSTRUCTIONS:
                    for button in self.back_buttons:
                        if button.rect.collidepoint(pos):

                            if button.button_type == BACK:
                                self.game_section = START
                    
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