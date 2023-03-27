from logging import root
import arcade
from pathlib import Path
from tkinter import Scale	

root_folder = Path(__file__).parent

#constants
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 845
SCREEN_TITLE = 'Year 13 game'

#scaling to change characters from original size
CHARACTER_SCALING = 0.8

#creating game window
class Window(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.Game_View = MyGame()
        self.show_view(self.Game_View)

#player textures 
class Entity(arcade.Sprite):
    def __init__(self):
        super().__init__(Path(__file__).parent.joinpath(f'tempplayer.png'))
        self.walk_textures = []
        self.idle_textures = arcade.load_texture_pair(Path(__file__).parent.joinpath(f'tempplayer.png'))
        self.face_direction = 0
        self.current_texture = 0
        self.cur_texture_index = 0
        self.odo = 0
        self.scale = CHARACTER_SCALING

class Player(Entity):
    def __init__(self):
        super().__init__()

        self.idle_animating = False
        self.idle_odo = 1
        self.current_chunk_texture = 0        

#gameview window
class MyGame(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.player = None
        self.tilemap = None
        self.scene = None
        self.HUD = None
        self.physics_engine = None
        self.camera = None
        self.HUD_camera = None
        self.score = 0 
        self.level = 0
        self.reset_score = True

        self.setup()
        self.walk_textures =[]
        self.idle_textures = arcade.load_texture_pair(Path(__file__).parent.joinpath(f'tempplayer.png'))
        self.face_direction = 0
        self.current_texture = 0
        self.odo = 0

    def setup(self):
        self.player = Player()

        #where character spawns
        self.player.center_x = 100 
        self.player.center_y = 100 

        #size of character
        self.player.scale = 0.8

        #tilemap
        tilemap_path = Path(__file__).parent.joinpath(f'mvpmapfr.tmx')
        self.tilemap = arcade.load_tilemap(tilemap_path)
        self.scene = arcade.Scene.from_tilemap(self.tilemap)

        self.HUD = arcade.Scene()
        self.scene.add_sprite('player', self.player)

        #scene/camera etc 
        def on_draw(self):
            self.clear()
            self.camera.use()
            self.scene.draw()

            self.HUD_camera.use()
            self.HUD.draw()

        def on_update(self, delta_time: float):
            self.player.update()
            self.player.update_animation()
            self.physics_engine.update()
            self.scene.update()
            self.center_camera_on_player()

    #cameras
    def center_camera_on_player(self):
        camera_x = self.player.center_x - SCREEN_WIDTH /2
        camera_y = self.player.center_y - SCREEN_HEIGHT /2

        if self.player.center_x < SCREEN_WIDTH /2:
            camera_x = 0
        if self.player.center_y < SCREEN_HEIGHT /2:
            camera_y = 0
        self.camera.move_to((camera_x, camera_y))


    #controls
    def on_key_press(self,symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE and self.physics_engine.can_jump():
            self.player.change_y = 5
        if symbol == arcade.key.A:
            self.player.change_x = -3
        if symbol == arcade.key.D:
            self.player.change_x = 3

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.A or symbol == arcade.key.D:
            self.player.change_x = 0



game = Window()
arcade.run()