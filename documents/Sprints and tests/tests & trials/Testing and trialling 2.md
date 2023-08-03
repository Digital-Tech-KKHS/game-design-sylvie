_Name:_ Sylvie McDonald

_Date:_ 6th May

Involved in the trial
>- Grace McDonald
>- Gabby Smythe
>- Jasper Sharp
>- Charley Kate
>- Simone Wu
>- Josiah Beale

## Trial goal:
> To find what colour scheme people would prefer to see in the game. Which is most aesthetically pleasing etc.


## Describe the trail
>The purpose of this trial was to find which colour ways people preferred/found more aesthetically pleasing. I used two photos from different games and got peoples opinions from inside our class. this gave me an idea of where to start for my map.



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

## Test 1:
# Getting user input

Date: 6/5/2023


```python
        self.physics_engine.add_sprite(self.player,

                                friction=PLAYER_FRICTION,

                                mass=PLAYER_MASS,

                                moment=arcade.PymunkPhysicsEngine.MOMENT_INF,

                                collision_type="player",

                                max_horizontal_velocity=PLAYER_MAX_HORIZONTAL_SPEED,

                                max_vertical_velocity=PLAYER_MAX_VERTICAL_SPEED)
```

| Test Data                   | Expected                     | Observed                    |
| --------------------------- | ---------------------------- | --------------------------- |
| Physics engine | On key release, player stops | On key release player does not stop|



## Test 2:

Date: 6/5/2023

```python
    DAMPING = 0.1
    
    self.physics_engine.add_sprite(self.player,

                                friction=PLAYER_FRICTION,

                                mass=PLAYER_MASS,

                                moment=arcade.PymunkPhysicsEngine.MOMENT_INF,

                                damping=DAMPING,

                                collision_type="player",

                                max_horizontal_velocity=PLAYER_MAX_HORIZONTAL_SPEED,

                                max_vertical_velocity=PLAYER_MAX_VERTICAL_SPEED)
    
```

| Test Data       | Expected                           | Observed |
| --------------- | ---------------------------------- | -------- |
|Damping lower for less drifting | Player drifting lessens            | Expected |
| Damping         | player stops moving on key release | Expected |

