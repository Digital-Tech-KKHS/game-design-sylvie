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
        self.walk_textures = []

        # for i in range(6):
        #     texture = arcade.load_texture_pair(Path(__file__).parent.joinpath(f'animation{i}.png'))
        #     self.walk_textures.append(texture)

class Npc(Entity):
    def __init__(self, properties=None):
        path = Path(__file__).parent.joinpath('tempnpc.png')
        super().__init__(path)



class Enemy(Entity):
    def __init__(self, properties=None):
        path = Path(__file__).parent.joinpath('enemy2.png')
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
        

    

        
        

