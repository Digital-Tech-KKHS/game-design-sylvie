_Date:_ 2nd June

Involved in the trial
>- Grace McDonald
>- Gabby Smythe
>- Simone Wu
>- Josiah Beale
>- Jasper Sharp

## Trial goal:
> To find out which character movement people prefer using two different physics engines.
>

## Describe the trail
>I set up a trial for each option, the first was the movement with pymunk physics engine and the next was with arcades simple physics engine. I had test users within my class play on each and tell me which they preferred.


A:
https://youtu.be/NrO8iwRoRB8

B:
https://youtu.be/bokRNTz14HM


## Results
> - Everyone preferred the movement using the simple physics engine
> - The feedback I got was that the pymunk one didn't stop immediately and had ice skater like motion.
>
## Briefly describe the changes you have made based on this trial
> - I changed my physics engine from pymunk physics engine to python arcade simple physics engine.
> - I decided that because my game was not collision based it probably did not need such a complicated physics engine.

## Test 1:
# Getting user input

Date: 6/5/2023

```python
   colliding = arcade.check_for_collision_with_list(self.player, self.scene['enemies'])

        if colliding:

            end_view = EndView()

            self.window.show_view(end_view)
```

| Test Data                    | Expected                        | Observed                       |
| ---------------------------- | ------------------------------- | ------------------------------ |
| Lose function    | On collision with enemy, end screen pops up                        | Expected                     |

## Test 2:


```python
        for enemy in self.scene'[enemy_layer]':
	        if 6 player.center_x enemy.center_x < 500: 
		        enemy.seek(player) 
		        enemy.attacking = True 
		    elif -6 > player.center_x - enemy.center_x > -500: 
			    enemy.seek(player) 
			    enemy.attacking = True 
			else: 
				enemy.change_x = 0 
				enemy.attacking = False
```

| Test Data                    | Expected                        | Observed                       |
| ---------------------------- | ------------------------------- | ------------------------------ |
| Seek function  | Enemy seeks player     | Enemy did not seek player    |