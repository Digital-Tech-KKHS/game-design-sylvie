_Date:_ 6th May

Involved in the trial
>- Grace McDonald
>- Gabby Smythe
>- Charley Kate
>- Simone Wu
>- Josiah Beale
>- Jasper sharp

## Trial goal:
> Find out which enemy design people preferred more.


## Describe the trail
>I asked people from inside and outside my class which character they preferred. I told them B was ai and A was original. the people doing this test knew what the rest of my game looked like so were able to make a judgement on which suited it more.



A:
![[Pasted image 20230723150724.png | 100]]

B:
![[Pasted image 20230723160503.png | 100]]


## Results
> - Charley, Josiah, Simone and Jasper both liked B more but as they have seen my game before, told me that it would look out of place and to use my own design.
> - The rest preferred mine and knew it would fit the game more and said to use that as it would be more simple to animate.
>
## Briefly describe the changes you have made based on this trial
> - These results have told me which is the best option to go with. I do not want my characters to look out of place in my games world so I will take their advice.
> - I chose to use my own design over AI design.

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