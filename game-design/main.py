from logging import root
import arcade
from pathlib import Path
from arcade.pymunk_physics_engine import PymunkPhysicsEngine
from constants	import *
from sprites import Player, Enemy
from entity import Entity

# Creating game window.
class Window(arcade.Window):
    """Main game window."""

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.game_view = MyGame()
        self.Start_View = StartView()
        self.show_view(self.Start_View)

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
        self.wall_list = None
        self.enemy_list = None
   
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
        enemy = Enemy()
        self.wall_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()

        # Where sprites spawns.
        enemy.center_x = 100
        enemy.center_y = 150

        self.player.center_x = 100 
        self.player.center_y = 100 

        # Size of sprites.
        self.player.scale = 0.8
        enemy.scale = 1.5

        # Set boundaries on the left/right the enemy can't cross
        enemy.boundary_right = CHARACTER_SCALING * 8
        enemy.boundary_left = CHARACTER_SCALING * 3
        enemy.change_x = 2

        self.enemy_list.append(enemy) 



        # Tilemap.
        tilemap_path = Path(__file__).parent.joinpath(f'citymapdesign.tmx')
        self.tilemap = arcade.load_tilemap(tilemap_path)

        # Pull the sprite layers out of the tile map.
        self.wall_list = self.tilemap.sprite_lists["walls"]

        self.scene = arcade.Scene.from_tilemap(self.tilemap) 

        self.HUD = arcade.Scene()
        self.scene.add_sprite('player', self.player)
        self.scene.add_sprite('enemy', enemy)
      


    # Camera&physics.
        gravity = (0, 0)
        self.physics_engine = PymunkPhysicsEngine(gravity=gravity)
        self.camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.HUD_camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.physics_engine.add_sprite(enemy,
            friction=PLAYER_FRICTION,
            mass=PLAYER_MASS,
            moment=arcade.PymunkPhysicsEngine.MOMENT_INF,
            damping=DAMPING,
            collision_type="enemy",
            max_horizontal_velocity=PLAYER_MAX_HORIZONTAL_SPEED,
            max_vertical_velocity=PLAYER_MAX_VERTICAL_SPEED
        )

        self.physics_engine.add_sprite(self.player,
            friction=PLAYER_FRICTION,
            mass=PLAYER_MASS,
            moment=arcade.PymunkPhysicsEngine.MOMENT_INF,
            damping=DAMPING,
            collision_type="player",
            max_horizontal_velocity=PLAYER_MAX_HORIZONTAL_SPEED,
            max_vertical_velocity=PLAYER_MAX_VERTICAL_SPEED
        )

        # Create the walls.
        # By setting the body type to PymunkPhysicsEngine.STATIC the walls can't
        # move.
        # Movable objects that respond to forces are PymunkPhysicsEngine.DYNAMIC
        # PymunkPhysicsEngine.KINEMATIC objects will move, but are assumed to be
        # repositioned by code and don't respond to physics forces.
        # Dynamic is default.
        self.physics_engine.add_sprite_list(self.wall_list,
            friction=WALL_FRICTION,
            collision_type="wall",
            body_type=arcade.PymunkPhysicsEngine.STATIC
        )

        # Scene/camera etc.
    def on_draw(self):
        self.clear()
        self.camera.use()
        self.scene.draw()
        self.HUD_camera.use()
        self.HUD.draw()


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

    def on_update(self, delta_time: float):

        colliding = arcade.check_for_collision_with_list(self.player, self.scene['enemy'])
        if colliding:
            end_view = EndView()
            self.window.show_view(end_view)

        # Calculate speed based on the keys pressed.
        self.player.change_x = 0
        self.player.change_y = 0

        if self.W_pressed and not self.S_pressed:
            force = (0, PLAYER_MOVE_FORCE)
            self.physics_engine.apply_force(self.player, force)
        elif self.S_pressed and not self.W_pressed:
            force = (0, -PLAYER_MOVE_FORCE)
            self.physics_engine.apply_force(self.player, force)
        if self.A_pressed and not self.D_pressed:
            self.player.change_x = -MOVEMENT_SPEED
            force = (-PLAYER_MOVE_FORCE, 0)
            self.physics_engine.apply_force(self.player, force)
        elif self.D_pressed and not self.A_pressed:
            force = (PLAYER_MOVE_FORCE, 0)
            self.physics_engine.apply_force(self.player, force)


        self.player.update()
        self.player.update_animation()
        # self.scene.update()
        self.physics_engine.step()
        self.center_camera_on_player()

game = Window()
arcade.run()