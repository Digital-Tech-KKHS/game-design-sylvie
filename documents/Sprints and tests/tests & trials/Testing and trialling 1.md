
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

I changed this code as I realised I had not adjusted it to my new top down perspective. I also still had my jumping/space bar which is not needed in top down.

```python
        def on_key_press(self,symbol: int, modifiers: int):

        if symbol == arcade.key.W:

            self.player.change_y = 3

        if symbol == arcade.key.A:

            self.player.change_x = -3

        if symbol == arcade.key.S:

            self.player.change_y = -3

        if symbol == arcade.key.D:

            self.player.change_x = 3
```

| Test Data          | Expected                                        | Observed |
| ------------------ | ----------------------------------------------- | -------- |
| Character movement | Character moves up/down right/left on key press | Expected |                   |                                                 |          |

## Test 2:
# Getting user input

Date: 6/5/2023

```python
    self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, walls=self.scene['ground'])
```


| Test Data | Expected   | Observed               |    |     |
| --------- | ---------- | ---------------------- | ---  |
| Physics   | No gravity | Player falling off map |              |            |                        |     |     |     |


End user input made me realise that this line was causing complications with my character. My character kept falling off the map and end user input made me realise it was a physics engine problem. This line of code was making my player have gravity and I don't need that in a top down game. At this point in my game, I don't have walls so to fix this problem, I removed my physics engine so I could continue getting input on other aspects of the game.

(After removing)

| Test Data          | Expected                                        | Observed |
| ------------------ | ----------------------------------------------- | -------- |
| No physics | No gravity | Expected |                   |                                                 |    