from logging import root
import arcade
from pathlib import Path
from constants	import *
from sprites import Player, Enemy, Npc
from entity import Entity
import math 

# Creating game window.
class Window(arcade.Window):
    """Main game window."""

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.game_view = MyGame()
        self.Start_View = StartView()
        self.show_view(self.Start_View)

class DialogueBox:
    """To handle the message boxes fom npcs"""
    def __init__(self):
        pass

# Starting screen.
class StartView(arcade.View):
    """Creates startscreen."""

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)
        arcade.set_viewport(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)

    # Writing on starting screen
    def on_draw(self):
        self.clear()
        arcade.draw_text("Click anywhere to start", 
            SCREEN_WIDTH / 2, 
            SCREEN_WIDTH / 2, 
            arcade.color.WHITE, 
            font_size=50, 
            anchor_x="center"
        )

    # When clicking it sends to first level
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        Game_View = MyGame()
        self.window.show_view(Game_View)

# Ending screen
class EndView(arcade.View):
    def on_show_view(self):
        super().__init__()
        arcade.set_background_color(arcade.color.BLACK)
        arcade.set_viewport(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)

    # Writing on ending screen
    def on_draw(self):
        self.clear()
        arcade.draw_text("You've been arrested >:(",
            SCREEN_WIDTH / 2, 
            SCREEN_WIDTH / 2, 
            arcade.color.WHITE, 
            font_size=50, 
            anchor_x="center"
        )
        arcade.draw_text("Click anywhere to play again", 
            self.window.width / 2, 
            self.window.height / 2-75, 
            arcade.color.WHITE, 
            font_size=20, 
            anchor_x="center"
        )
        
    # Sending back to first level if clicking screen
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        Game_View = MyGame()
        self.window.show_view(Game_View)
    

# Gameview window.
class MyGame(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.BLACK)
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
        self.wall_list = None
        self.enemy_list = None
        self.dialogue_active = True
        
        # Track the current state of what key is pressed.
        self.A_pressed = False
        self.D_pressed = False
        self.W_pressed = False
        self.S_pressed = False

        self.setup()
        self.walk_textures =[]
        self.idle_textures = arcade.load_texture_pair(Path(__file__).parent.joinpath(f'spritefrontfacing.png'))
        self.face_direction = 0
        self.current_texture = 0
        self.odo = 0

    def setup(self):
        self.player = Player()
        self.wall_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.npc_list = arcade.SpriteList()

        self.player.center_x = 100 
        self.player.center_y = 100 

        # Size of sprites.
        self.player.scale = 0.8
        
        # Tilemap.
        tilemap_path = Path(__file__).parent.joinpath(f'map0.tmx')
        self.tilemap = arcade.load_tilemap(tilemap_path)

        # Pull the sprite layers out of the tile map.
        self.wall_list = self.tilemap.sprite_lists["walls"]

        self.scene = arcade.Scene.from_tilemap(self.tilemap)
        self.scene.add_sprite_list('enemies')
        self.scene.add_sprite_list('npc')

        self.HUD = arcade.Scene()
        self.HUD.add_sprite_list('money')
        self.scene.add_sprite('player', self.player)
        
        # Adding money icon.
        self.scene.add_sprite_list('money')
        for i in range(1):
            x = 45 + 40 * i
            y = SCREEN_HEIGHT - 25
            money = arcade.Sprite(ROOT_FOLDER.joinpath('money.png'), 2.5, center_x=x, center_y=y)
            self.HUD['money'].append(money)

        for enemy in self.scene["enemy_layer"]:
            enemy.scale = 0.5

        # Adding enemy/png to scene.
        for enemy in self.scene["enemy_layer"]:
            new_enemy = Enemy(enemy.properties)
            new_enemy.center_x = enemy.center_x
            new_enemy.center_y = enemy.center_y
            self.scene["enemies"].append(new_enemy)
            enemy.kill()
        
        for enemy in self.scene["enemy_layer"]:
            new_enemy = Enemy(enemy.properties)
            new_enemy.center_x = enemy.center_x
            new_enemy.center_y = enemy.center_y
            self.scene["enemies"].append(new_enemy)
            enemy.kill()

        # Adding npc to scene. 
        for npc in self.scene["npc_layer"]:
            new_npc = Npc()
            new_npc.center_x = npc.center_x
            new_npc.center_y = npc.center_y
            self.scene["npc"].append(new_npc)
            npc.kill()
           

    # Camera&physics.
        gravity = (0, 0)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player, self.scene['walls'])
        self.camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.HUD_camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    #NPC dialogue
        self.dialogue_messages = [
            "So you want to get home on my train...? Usually I dont allow thieves on.",
            "But maybe I could make use of you, in return I'll let you on my train.",
            "Get me 5 bottles of water and leave it in this box next to me, then you'll move onto the next trial..."
        ]

        self.dialogue_index = 0  

        # Scene/camera etc.
    def on_draw(self):
        self.clear()
        self.camera.use()
        self.scene.draw()
        self.HUD_camera.use()
        self.HUD.draw()

        colliding = arcade.check_for_collision_with_list(self.player, self.scene['npc'])
        if colliding:
            arcade.draw_rectangle_filled(
                SCREEN_WIDTH // 2, 
                SCREEN_HEIGHT // 2, 
                800, 
                100, 
                arcade.color.WHITE
            )
        
            arcade.draw_text(
                self.dialogue_messages[self.dialogue_index], 
                SCREEN_WIDTH // 2, 
                SCREEN_HEIGHT // 2 + 20, 
                arcade.color.BLACK, 
                font_size=16, 
                anchor_x="center", 
                anchor_y="center"
            )


    # Cameras.
    def center_camera_on_player(self):
        camera_x = self.player.center_x - SCREEN_WIDTH / 2
        camera_y = self.player.center_y - SCREEN_HEIGHT / 2

        if self.player.center_x < SCREEN_WIDTH /2:
            camera_x = 0
        if self.player.center_y < SCREEN_HEIGHT /2:
            camera_y = 0
        self.camera.move_to((camera_x, camera_y))

    
    
    # Controls.
    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.W:
            self.W_pressed = True
        elif key == arcade.key.A:
            self.A_pressed = True
        elif key == arcade.key.S:
            self.S_pressed = True
        elif key == arcade.key.D:
            self.D_pressed = True

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.W:
            self.W_pressed = False 
        elif key == arcade.key.A:
            self.A_pressed = False
        elif key == arcade.key.S:
            self.S_pressed = False
        elif key == arcade.key.D:
            self.D_pressed = False

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        index = (self.dialogue_index + 1) 
        
        if self.dialogue_active:
            if button == arcade.MOUSE_BUTTON_LEFT:
                self.dialogue_index = index  
        
        # if self.dialogue_index =
            

    def on_update(self, delta_time: float):

        for enemy in self.scene['enemies']:
            dx = self.player.center_x - enemy.center_x
            dy = self.player.center_y - enemy.center_y
            theta = math.atan2(dy, dx)
            if math.dist(self.player.position, enemy.position) < 300:
                enemy.change_x = math.cos(theta)*enemy.speed
                enemy.change_y = math.sin(theta)*enemy.speed
            else:
                enemy.change_x = 0
                enemy.change_y = 0

        colliding = arcade.check_for_collision_with_list(self.player, self.scene['enemies'])
        if colliding:
            end_view = EndView()
            self.window.show_view(end_view)

        colliding = arcade.check_for_collision_with_list(self.player, self.scene['nextlevel'])
        if colliding:
            self.level += 1
            self.setup()

        
        # Calculate speed based on the keys pressed.
        self.player.change_x = 0
        self.player.change_y = 0

        if self.W_pressed and not self.S_pressed:
            self.player.change_y = PLAYER_SPEED
        elif self.S_pressed and not self.W_pressed:
            self.player.change_y = -PLAYER_SPEED

        if self.A_pressed and not self.D_pressed:
            self.player.change_x = -PLAYER_SPEED
        elif self.D_pressed and not self.A_pressed:
            self.player.change_x = PLAYER_SPEED
            

        self.player.update()
        self.player.update_animation()
        self.scene.update()
        self.physics_engine.update()
        self.center_camera_on_player()


game = Window()
arcade.run()