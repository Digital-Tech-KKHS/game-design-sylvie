_Name:_ Sylvie McDonald

_Date:_ 6th May

Involved in the trial
>- Grace McDonld
>- Gabby Smythe
>- jasper sharp
>- charley kate
>- simone wu
>- josiah Beale

## Trial goal:
> To find what colour scheme people would prefer to see in the game. Which is most aesthetically pleasing etc.


## Describe the trail
>Before i started creating my tileset, i found a few different colour schemes and art styles that i liked and felt portrayed what the setting is like. to see which people would prefer, I did an A/B test and asked people in my class which they would like playing the most. CAHNGE TO DAMPING PHYSICS ENGINE



A:
![[Pasted image 20230508145601.png]]

B:
![[Pasted image 20230508145221.png]]


## Results
> - Grace, Gabby, Charlie and simone prefered A
> - Jasper and Josiah preferred B
> - the people that prefered a liked that it was brighter and also enojoyed the colour palette
> - the people that prefered B liekd that the darkness of it though thought it might not really fit with my game
>
## Breifly describe the changes you have made based on this trial
> - These results have given me a place to start with my tileset 
> - it has given me a firm idea of what people would prefer to see and what might fit best with the game.
> - the feedback on B has changed my perspective on what would be best because now i agree that it may not be quite right for the game

## Test 2:
# Getting user input

Date: 6/5/2023

```python
    def on_key_release(self, key: int, modifiers: int):

        if key == arcade.key.W:

            self.W_pressed = False

        elif key == arcade.key.A:

            self.A_pressed = False

        elif key == arcade.key.S:

            self.S_pressed = False

        elif key == arcade.key.D:

            self.D_pressed = False
```

| Test Data                    | Expected                        | Observed                       |
| ---------------------------- | ------------------------------- | ------------------------------ |
| Player stops on key release    | on key release, player stops                         | player not stopping                       |

This was a bit of a problem for me as im new to the physics engine im using. I realised that it was because i did not have damping on for my player/physics engine and set it to 0.1..

```python
        self.physics_engine.add_sprite(self.player,

                                friction=PLAYER_FRICTION,

                                mass=PLAYER_MASS,

                                moment=arcade.PymunkPhysicsEngine.MOMENT_INF,

                                damping=DAMPING,

                                collision_type="player",

                                max_horizontal_velocity=PLAYER_MAX_HORIZONTAL_SPEED,

                                max_vertical_velocity=PLAYER_MAX_VERTICAL_SPEED)
```

| Test Data                    | Expected                        | Observed                       |
| ---------------------------- | ------------------------------- | ------------------------------ |
| Player stops on key release  | on key release, player stops    | on key release player stops    |