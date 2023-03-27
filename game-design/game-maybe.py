from logging import root
from tkinter import Scale
import arcade
from pathlib import Path

root_folder = Path(__file__).parent

#constants
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 845
SCREEN_TITLE = 'My game'

#animation speed
UPDATES_PER_FRAME = 12

#scaling to change characters from original size
CHARACTER_SCALING = 0.8

#facing direction
RIGHT_FACING = 0
LEFT_FACING = 1

#creating game window
class Window(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.End_View = EndView()
        self.Game_View = MyGame()
        self.Start_View = StartView()
        self.show_view(self.Start_View)

#starting screen
class StartView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)
        arcade.set_viewport(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)

    #writing on starting screen
    def on_draw(self):
        self.clear()
        arcade.draw_text("Click anywhere to start", SCREEN_WIDTH / 2, SCREEN_WIDTH / 2, arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Collect all the potions!!", self.window.width / 2, self.window.height / 2-75, arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text("Dont touch the lava and water!!", self.window.width / 2, self.window.height / 3, arcade.color.WHITE, font_size=20, anchor_x="center")

    #when clicking it sends to first level
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        Game_View = MyGame()
        self.window.show_view(Game_View)



#ending screen
class EndView(arcade.View):
    def on_show_view(self):
        super().__init__()
        arcade.set_background_color(arcade.color.BLACK)
        arcade.set_viewport(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)

    #writing on ending screen
    def on_draw(self):
        self.clear()
        arcade.draw_text("Click anywhere to play again!!", SCREEN_WIDTH / 2, SCREEN_WIDTH / 2, arcade.color.WHITE, font_size=50, anchor_x="center")

    #sending back to first level if clicking screen
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        Game_View = MyGame()
        self.window.show_view(Game_View)

#player textures 
class Entity(arcade.Sprite):
    def __init__(self):
        super().__init__(Path(__file__).parent.joinpath(f'idle.png'))
        self.walk_textures = []
        self.idle_textures = arcade.load_texture_pair(Path(__file__).parent.joinpath(f'idle.png'))
        self.face_direction = 0
        self.current_texture = 0
        self.cur_texture_index = 0
        self.odo = 0
        self.scale = CHARACTER_SCALING

        #character animation textures
        for i in range(4):
            texture = arcade.load_texture_pair(Path(__file__).parent.joinpath(f'animation{i}.png'))
            self.walk_textures.append(texture)


class Player(Entity):
    def __init__(self):
        super().__init__()

        self.idle_animating = False
        self.idle_odo = 1
        self.current_chunk_texture = 0
        
        
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
            if self.current_texture == 4 * UPDATES_PER_FRAME:
                self.current_texture = 0
            frame = self.current_texture // UPDATES_PER_FRAME
            direction = self.face_direction
            self.texture = self.walk_textures[frame][direction]
        

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
        self.idle_textures = arcade.load_texture_pair(Path(__file__).parent.joinpath(f'idle.png'))
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
        tilemap_path = Path(__file__).parent.joinpath(f'Tilemap{self.level}.tmx')
        self.tilemap = arcade.load_tilemap(tilemap_path)
        self.scene = arcade.Scene.from_tilemap(self.tilemap)

        self.HUD = arcade.Scene()
        self.scene.add_sprite('player', self.player)
        self.HUD.add_sprite_list('health')
        if self.reset_score:
            self.score = 0
        self.reset_score = False

    
        
    #adding health
        self.scene.add_sprite_list('health')
        for i in range(5):
            x = 45 + 40 * i
            y = SCREEN_HEIGHT - 25
            health = arcade.Sprite(root_folder.joinpath('Healthbar.png'), 2.5, center_x=x, center_y=y)
            self.HUD['health'].append(health)

        
    #camera and physics
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, walls=self.scene['ground'])
        self.camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.HUD_camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        

    #how many potions have beeen collected 
    def on_draw(self):
        self.clear()
        self.camera.use()
        self.scene.draw()

        self.HUD_camera.use()
        self.HUD.draw()
        arcade.draw_text(f"Potions: {self.score}", SCREEN_WIDTH-100, SCREEN_HEIGHT-50)

    
    #potion collision/collecting and adding to score
    def on_update(self, delta_time: float):
        self.player.update()
        self.player.update_animation()
        self.physics_engine.update()
        self.scene.update()
        self.center_camera_on_player()

        for coin in self.scene['potion']:
            coin.on_update()
            
            colliding = arcade.check_for_collision_with_list(self.player, self.scene['potion'])
            for coin in colliding:
                coin.kill()
                self.score += 1

        if self.player.center_y < 0:
            self.setup()

        #next level on collision with nextlevel layer
        colliding = arcade.check_for_collision_with_list(self.player, self.scene['nextlevel'])
        if colliding:
            self.level += 1
            self.setup()
        if self.level == 1:

        #background colour for each level
            arcade.set_background_color(arcade.color.JET)
        else:
            arcade.set_background_color(arcade.color.SKY_BLUE)
            

        #removing 1 health on collision with anything on enemy layer
        colliding = arcade.check_for_collision_with_list(self.player, self.scene['donttouch'])
        if colliding:
            self.HUD['health'][-1].kill()
            self.player.center_x = 100
            self.player.center_y = 100

        #if losing all health: send to ending screen
        if len(self.HUD['health']) == 0:
            end_view = EndView()
            self.window.show_view(end_view)

        #going to end screen at the ending of final level
        colliding = arcade.check_for_collision_with_list(self.player, self.scene["win"])
        if colliding:
            end_view = EndView()
            self.window.show_view(end_view)
            
             
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