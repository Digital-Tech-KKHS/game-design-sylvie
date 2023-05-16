# code review 17/5

Import Statements:

```python

from logging import root
import arcade
from pathlib import Path
from tkinter import Scale	
from arcade.pymunk_physics_engine import PymunkPhysicsEngine
```
All imports are from standard or third-party libraries. They are correctly grouped. However, 'root' from 'logging' and 'Scale' from 'tkinter' aren't used in the script. Remove unused imports.

Whitespace:
Whitespace between classes and methods is generally good, but there are a few places where it could be improved for consistency. For example, there should be two blank lines between top-level classes or functions:

```python

# From this:
class Window(arcade.Window):
    ...

#starting screen
class StartView(arcade.View):
    ...
```
# To this:
```python
class Window(arcade.Window):
    ...


# Starting screen
class StartView(arcade.View):
    ...

```
Comments:
Make sure to start comments with a # and a single space. Capitalize the first letter of the comment and end with a period. For example:


# From this:
```python
#starting screen
```
# To this:
```python
# Starting screen.
```
Docstrings:
There are no docstrings in the code. They should be added to describe what classes and methods do. For example:

```python

class Window(arcade.Window):
    """Main window of the game."""
    ...

```
Naming Conventions:
The class names follow the CapWords convention and seem informative, which is good.

Indentation:
The indentation seems to be consistent throughout the code.

Line Length:
It appears that all lines fit within the 79 character limit, which is good.

Spaces around Operators:
There are a few places where additional spaces are needed for readability. For example:

```python

    # From this:
    camera_x = self.player.center_x - SCREEN_WIDTH /2
    # To this:
    camera_x = self.player.center_x - SCREEN_WIDTH / 2

```
Variable Naming:
Variable names follow the lowercase with words separated by underscores convention, which is good.

Consistent Quotes:
The code seems to consistently use single quotes for strings, which is good.

Unused imports:
Remove unused imports, for example 'root' from 'logging' and 'Scale' from 'tkinter' are not being used.

Code Complexity:
The classes in the code seem to have clear, singular responsibilities, which is good.

Code Duplication:
There is some duplication in the code. For example, the Entity and Player classes have similar attributes. This might be a place where you could use inheritance or composition to reduce duplication.

Method and Function Calls:
The method and function calls have few parameters, and none of the lines are overly long, which is good.

These are the areas in the code that could use some improvement. By making these changes, the code will adhere more closely to PEP8 standards and be more readable.
