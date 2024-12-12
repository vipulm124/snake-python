
class Settings:
    def __init__(self):
        # Game settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (206, 219, 240)
        self.black  = (0, 0, 0)
        self.border_thickness = 10
        self.game_speed = 10

        # snake settings
        self.snake_default_segments = [(100, 100), (80, 100), (60, 100)] 
        self.snake_color = (5, 60, 150)
        self.snake_cell_size = 20

        # snake will move to right by default
        self.snake_default_direction = (20,0)

        # food settings:
        self.food_color = (230, 42, 39)

        #scoreboard settings
        self.scoreboard_color = (30, 30, 30)