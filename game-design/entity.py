import arcade
from constants import *

# Player textures.
class Entity(arcade.Sprite):
    def __init__(self, path):
        super().__init__(path)
        self.walk_textures = []
        self.face_direction = 0
        self.current_texture = 0
        self.cur_texture_index = 0
        self.odo = 0
        
        

        