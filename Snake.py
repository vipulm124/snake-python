import pygame

# from Game import Game

class Snake:
    def __init__(self, game):
        super().__init__()
        self.settings = game.settings
        self.screen = game.screen


    def draw_snake(self, snake_head):
        for segment in snake_head:
             pygame.draw.rect(self.screen, self.settings.snake_color, pygame.Rect(segment[0], segment[1], self.settings.snake_cell_size, self.settings.snake_cell_size))
    
    
    def run_snake(self, current_snake_head, snake_direction):
        head_x, head_y = current_snake_head[0]
        new_head = (head_x + snake_direction[0] , head_y + snake_direction[1])
        return [new_head] + current_snake_head[:-1]