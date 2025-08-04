import pygame

class Food:
    def __init__(self, game):
        super().__init__()
        self.settings = game.settings
        self.screen = game.screen

    

    def draw_food(self, food):
        pygame.draw.rect(self.screen, self.settings.food_color, pygame.Rect(food[0], food[1], self.settings.snake_cell_size, self.settings.snake_cell_size))

    

