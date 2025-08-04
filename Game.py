import random
import pygame
import sys
from Settings import Settings
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard


class Game:
    def __init__(self):
        """Int for Snake game"""

        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.font = pygame.font.Font(None, 50)

        self.snake_head = self.settings.snake_default_segments
        self.snake_direction = self.settings.snake_default_direction

        self.new_food = self._get_new_food()
        self.sb = Scoreboard(self)
        

        
        pygame.display.set_caption("Snakes")
        self.bg_color = self.settings.bg_color
    

    def run_game(self):
        """
        start main loop of the game
        """
        while True:
            self._check_events()
            self._update_screen()



    def _check_events(self):
        """Check all event, we are currently only handling key down events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            

            if event.type == pygame.KEYDOWN:
                self._check_key_down_events(event)
    

    def _check_key_down_events(self, event):
        """Contains all the key down events of the game"""
        if event.key == pygame.K_q:
            sys.exit()
        
        if event.key == pygame.K_DOWN and self.snake_direction != (0, -20):
            self.snake_direction = (0, 20)
        if event.key == pygame.K_UP and self.snake_direction != (0, 20):
            self.snake_direction = (0, -20)
        if event.key == pygame.K_LEFT and self.snake_direction != (20, 0):
            self.snake_direction = (-20, 0)
        if event.key == pygame.K_RIGHT and self.snake_direction != (-20, 0):
            self.snake_direction = (20, 0)
    


    def _update_screen(self):
        self.screen.fill(self.bg_color)
        pygame.draw.rect(self.screen,  self.settings.black, pygame.Rect(0, 0, self.settings.screen_width, self.settings.screen_height), self.settings.border_thickness)
        self._create_snake_and_run()
        self._create_food()
        self._check_if_food_eaten()
        self.sb.show_score(self.snake_head)

        pygame.display.flip()
        self.clock.tick(self.settings.game_speed)
        if self._check_collisions():
            self._show_game_over()
            pygame.quit()
            sys.exit()


    
    def _create_snake_and_run(self):
        """create snake with updated size and make sure it is running"""
        snake = Snake(self)
        self.snake_head = snake.run_snake(self.snake_head, self.snake_direction)
        snake.draw_snake(self.snake_head)

    
    def _check_collisions(self):
        """ check if there is any collision with wall or itself"""
        head_x, head_y = self.snake_head[0]

        if (head_x < self.settings.border_thickness or head_y < self.settings.border_thickness or
            head_x >= self.settings.screen_width - self.settings.border_thickness or
            head_y >= self.settings.screen_height - self.settings.border_thickness):
            # we have collided to a wall
            return True
        
        if self.snake_head[0] in self.snake_head[1:]:
            # snake collided to itself
            return True
        
        # no collision
        return False
    

    def _create_food(self):
        """create a new food object, only if previous one is completed"""
        food = Food(self)
        food.draw_food(self.new_food)
    

    def _check_if_food_eaten(self):
        """check if the current food object is consumed by the snake"""
        if self.snake_head[0] == self.new_food:
            # food is eaten
            self.snake_head.append(self.snake_head[-1])
            self.new_food = self._get_new_food()



    def _get_new_food(self):
        """create a new food object at a random location"""
        return (random.randint(1, (self.settings.screen_width // self.settings.snake_cell_size) - 2) * self.settings.snake_cell_size,
                random.randint(1, (self.settings.screen_height // self.settings.snake_cell_size) - 2) * self.settings.snake_cell_size)
        

    def _show_game_over(self):
        """Game over text"""
        game_over_text = self.font.render("GAME OVER", True, self.settings.food_color)
        text_rect = game_over_text.get_rect(center=(self.settings.screen_width // 2, self.settings.screen_height // 2))
        self.screen.blit(game_over_text, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)



if __name__ == "__main__":
    """Create instance of game and start"""
    game = Game()
    game.run_game()