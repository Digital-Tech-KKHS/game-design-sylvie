import arcade
from constants import *
from entity import Entity

class Player(Entity):
    def __init__(self):
        path = Path(__file__).parent.joinpath('spritefrontfacing.png')
        super().__init__(path)
        self.idle_animating = False
        self.idle_odo = 1
        self.current_texture = 0
        self.face_direction = 0
        self.current_chunk_texture = 0 
        self.idle_textures = arcade.load_texture_pair(Path(__file__).parent.joinpath(f'spritefrontfacing.png'))
        self.walk_textures = []
        self.scale = CHARACTER_SCALING

    def update_animation(self, delta_time: float = 1 / 30):
    #Figure out if we need to flip face left or right
        if self.change_x < 0 and self.face_direction == RIGHT_FACING:
            self.face_direction = LEFT_FACING
        elif self.change_x > 0 and self.face_direction == LEFT_FACING:
            self.face_direction = RIGHT_FACING

    #idle 
        if self.change_x == 0:
            self.texture = self.idle_textures[self.face_direction]
            return

        #walking animation and speed
        if self.change_x != 0:
            self.current_texture += 1
        if self.current_texture == 6 * UPDATES_PER_FRAME:
            self.current_texture = 0
        frame = self.current_texture // UPDATES_PER_FRAME
        direction = self.face_direction
        

        for i in range(6):
            texture = arcade.load_texture_pair(Path(__file__).parent.joinpath(f'spriteanimationrunning{i}.png'))
            self.walk_textures.append(texture)

        self.texture = self.walk_textures[frame][direction]

class Npc(Entity):
    def __init__(self, properties=None):
        path = Path(__file__).parent.joinpath('npc1.png')
        super().__init__(path)
        self.scale = NPC_SCALING



class Enemy(Entity):
    def __init__(self, properties=None):
        path = Path(__file__).parent.joinpath('drone.png')
        super().__init__(path)

        print(properties)
        if properties is not None:
            for key, value in properties.items():
                setattr(self, key, value)
        else:
            print('no properties')

        try:
            self.speed
        except:
            raise KeyError("Enemy without speed custom property found. Check tilemap")
        
        # for i in range(6):
        #     texture = arcade.load_texture_pair(Path(__file__).parent.joinpath(f'enemy_animation{i}.png'))
        #     self.walk_textures.append(texture)
        

    

        
        

