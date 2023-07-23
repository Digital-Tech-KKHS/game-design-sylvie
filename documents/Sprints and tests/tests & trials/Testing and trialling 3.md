_Date:_ 6th May

Involved in the trial
>- Grace McDonald
>- Gabby Smythe
>- Charley Kate
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

## Test 1:
# Getting user input

Date: 6/5/2023

```python
   def seek(self, target:Player):

  

        if self.center_x > target.center_x:

            self.change_x = -3

        if self.center_x < target.center_x:

            self.change_x = 3

        if self.center_y > target.center_y:

            self.change_y = -3

        if self.center_y < target.center_y:

            self.change_y = 3
```

| Test Data                    | Expected                        | Observed                       |
| ---------------------------- | ------------------------------- | ------------------------------ |
| Seek function    | Enemy seeks player target                        | Enemy did not seek Player                     |

## Test 2:


```python
        for enemy in self.scene["enemy_layer"]:

            new_enemy = Enemy(enemy.properties)

            new_enemy.center_x = enemy.center_x

            new_enemy.center_y = enemy.center_y

            self.scene["enemies"].append(new_enemy)

            enemy.kill()
```

| Test Data                    | Expected                        | Observed                       |
| ---------------------------- | ------------------------------- | ------------------------------ |
| Enemy functions  | Enemy object in map replaced by PNG    | Expected    |