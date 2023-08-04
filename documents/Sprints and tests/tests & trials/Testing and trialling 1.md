
_Name:_ Sylvie McDonald

_Date:_ 3rd April

Involved in the trial
>- Grace McDonld
>- Gabby Smythe
>- Charley Kate
>- Simone Wu
>- Josiah Beale

## Trial goal:
> To find whether people prefer topdown or angled top down.


## Describe the trail
>I created 2 basic tilemaps, using tiles from preious games. I made one topdown and one oblique topdown. I then asked people inside and outside of our class which they prefered and recorded it.



A:
![[Pasted image 20230515144148.png]]

B:
![[Pasted image 20230510105153.png]]


## Results
> - Grace, Gabby, Charlie and simone prefered A
> - Jasper and Josiah preferred B
> - the people that prefered a liked that it was brighter and also enojoyed the colour palette
> - the people that prefered B liekd that the darkness of it though thought it might not really fit with my game
>
## Briefly describe the changes you have made based on this trial
> - These results have told me what perspective people would rather play in. This is a very important aspect of my game so this user input has been very useful.


## Test 1:
# Getting user input

Date: 6/5/2023

```python
    def on_key_press(self,symbol: int, modifiers: int):

        if symbol == arcade.key.SPACE and self.physics_engine.can_jump():

            self.player.change_y = 5

        if symbol == arcade.key.A:

            self.player.change_x = -3

        if symbol == arcade.key.D:

            self.player.change_x = 3
```

| Test Data          | Expected                           | Observed                            |
| ------------------ | ---------------------------------- | ----------------------------------- |
| Character movement | Character moves up/down left/right on key press | Character only moves left and right |       |                                    |                                     |



## Test 2:
# Getting user input

Date: 6/5/2023

```python
    self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, ground=self.scene['ground'])
```


| Test Data      | Expected   | Observed               |
| -------------- | ---------- | ---------------------- |
| Physics engine | No gravity | Player falling off map |

