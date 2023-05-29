from pathlib import Path

ROOT_FOLDER = Path(__file__).parent

SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 845
SCREEN_TITLE = 'Year 13 game'
MOVEMENT_SPEED = 3

# Keep player from going too fast.
PLAYER_MAX_HORIZONTAL_SPEED = 300
PLAYER_MAX_VERTICAL_SPEED = 300
DAMPING = 0.5


# Friction between objects.
PLAYER_FRICTION = 1
WALL_FRICTION = 0.7 

# Mass (defaults to 1)
PLAYER_MASS = 2.0 

# Force applied to player:
PLAYER_MOVE_FORCE = 4000

# Scaling to change characters from original size.
CHARACTER_SCALING = 0.8