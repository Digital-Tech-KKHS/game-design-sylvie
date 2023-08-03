_Date:_ 3rd August

Involved in the trial
>- Grace McDonald
>- Gabby Smythe
>- Charley Kate
>- Simone Wu
>- Josiah Beale

## Trial goal:
>To find out if my enemies are too fast or not.


## Describe the trail
> The trial goal is to test which enemy speed that people prefer. I need feedback on whether my enemies speed is too fast, making the game too hard. I let people play through my final game and give their opinions on whether it should be slowed down to make the game better to play.



A:


B:



## Results
> - Collectively, everyone decided that they were too fast. 
> - Feedback I got from Grace was that the game was too hard to complete and it got frustrating.
>
## Briefly describe the changes you have made based on this trial
> - With the feedback/results I have received I decided to slow the speeds of my enemies down. Instead of having them at 4/5 I set them from 2-4.
> - I made it so that on the first levels they are slower and there are less of them and as the levels increased in difficulty, they got faster and there were more of them. This means you have to be more strategical about getting around them and winning.

## Test 1:
# Getting user input

Date: 6/5/2023


```python
 def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):

        index = (self.dialogue_index + 1) 

        if self.dialogue_active:

            if button == arcade.MOUSE_BUTTON_LEFT:

                self.dialogue_index = index  

        if self.dialogue_index == 4:

            if button == arcade.MOUSE_BUTTON_LEFT:

                self.dialogue_active = None
```

| Test Data      | Expected                              | Observed |
| -------------- | ------------------------------------- | -------- |
| Dialogue index | Dialogue moves forward on left mouse click | Expected |
| Dialogue stops | Dialogue stops when index = 4 and dialogue becomes inactive      | Expected |



## Test 2:


```python
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
```

| Test Data      | Expected                                                       | Observed |
| -------------- | -------------------------------------------------------------- | -------- |
| Enemy seek     | Enemy seeks player at certain distance and incorporates speeds | Expected |
| Locates player | dy/dx maths locates player                                     | Expected |



