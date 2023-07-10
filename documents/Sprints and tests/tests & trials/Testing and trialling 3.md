_Date:_ 6th May

Involved in the trial
>- Grace McDonld
>- Gabby Smythe
>- jasper sharp
>- charley kate
>- simone wu
>- josiah Beale

## Trial goal:
> To find out whether users prefer the enemy to stay still or have a seek function. The enemies function effects the difficulty of the game.

## Describe the trail
>I set up a trial for each option, the first one had an enemy with a seek function and the second had an enemy with no seek function. I then gave it to end users and they played on each and told me which they preferred. Whichever people liked more would be the one implemented into the game.



A:
![[Pasted image 20230508145601.png]]

B:
![[Pasted image 20230508145221.png]]


## Results
> - Everyone preferred the enemies with the seek function. 
> - Feedback was it added a level of complexity to the game and it would be too easy if the enemies stayed still.
>
## Briefly describe the changes you have made based on this trial
> - These results have given me info on what people prefer with the enemies.
> - Everyone liked the enemies with a seek function though said having it within a certain distance would be good to have it within a certain distance so you weren't worried about the enemies the entire time while trying to do other things within the game.

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