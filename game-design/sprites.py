import arcade
from constants import *
from entity import Entity

class Player(Entity):
    def __init__(self):
        path = Path(__file__).parent.joinpath('spritefrontfacing.png')
        super().__init__(path)
        self.idle_animating = False
        self.idle_odo = 1
        self.current_chunk_texture = 0 



class Enemy(Entity):
    def __init__(self):
        path = Path(__file__).parent.joinpath('temp_enemy.png')
        super().__init__(path)
        self.walk_textures = []
        self.idle_textures = path
        self.face_direction = 0
        self.current_texture = 0
        self.cur_texture_index = 0
        self.odo = 0
        self.scale = CHARACTER_SCALING

    def seek(self, target:Player):
        
        if self.center_x > target.center_x:
            self.change_x = -3
        if self.center_x < target.center_x:
            self.change_x = 3
        if self.center_y > target.center_y:
            self.change_y = -3
        if self.center_y < target.center_y:
            self.change_y = 3

