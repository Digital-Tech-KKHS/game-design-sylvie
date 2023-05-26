import arcade
from constants import *
from entity import Entity

class Player(Entity):
    def __init__(self):
        path = Path(__file__).parent.joinpath(f'spritefrontfacing.png')
        super().__init__()

        self.idle_animating = False
        self.idle_odo = 1
        self.current_chunk_texture = 0 



class Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__(Path(__file__).parent.joinpath(f'temp_enemy.png'))
        self.walk_textures = []
        self.idle_textures = arcade.load_texture_pair(Path(__file__).parent.joinpath(f'temp_enemy.png'))
        self.face_direction = 0
        self.current_texture = 0
        self.cur_texture_index = 0
        self.odo = 0
        self.scale = CHARACTER_SCALING