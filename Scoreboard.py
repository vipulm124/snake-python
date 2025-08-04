import pygame.font

class Scoreboard:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings

        self.text_color = self.settings.scoreboard_color
        self.font = pygame.font.SysFont(None, 48)
        # self.prep_score()
    

    def prep_score(self, snake_head):
        # removing 3, as it was there by default
        snake_length = str(int(len(snake_head)) - 3)
        self.score_image = self.font.render(snake_length, True, self.text_color, self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.settings.screen_width - 20
        self.score_rect.top = 20
        
    def show_score(self, snake_head):
        self.prep_score(snake_head)
        self.screen.blit(self.score_image, self.score_rect)