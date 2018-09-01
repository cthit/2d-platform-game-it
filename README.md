# 2d-platform-game-it

A basic game/framework for a 2d-platformer built with python.
The purpose of the project is to be easily modifiable both for people with and without prior coding experience.

---

## Table of Contents

1. [Introduction](#introduction)
2. [General Information](#general-information)
   - [The State Class](#the-state-class)
   - [Behaviours](#behaviours)
3. [Simplest Modifications](#simplest-modifications)
   - [Level Creation](#level-creation)
   - [Creating new tiles](#creating-new-tiles)
4. [Intermediate Modifications](#intermediate-modifications)
   - [Creating new entities](#creating-new-entities)
   - [Creating new behaviours](#creating-new-behaviours)
   - [Changing the UI](#changing-the-ui)
5. [Advanced Modifications](#advanced-modifications)

---

## Introduction

The game is built around making it very simple of adding new content to the game. The game is split into a few different parts:

- Tiles:
  - Basic unmovable block in the game world, basically only an image you can collide with.
- Entities:
  - Anything else in the gameworld, such as the player or the goal flag.
- Behaviours:
  - Entities can have behaviours such as Collide, Jump, Move etc.
- Ui:
  - The ui components are buttons, text, non-entity images that interacts with the player.

---

## General Information

### The State Class

The state class is used to pass on the current state of the game to the different entities of the game.
The information contained in the state class is:

- `goal_reached` which is a method that will make the game go to the next level.
- `respawn_player` which is a method that will respawn the player.
- `level_size` contains the level size, you get the width through `level_size[0]` and the height through `level_size[1]`.

### Behaviours

Behaviours are used to define the well... behaviours of an entity for example some built in behaviours are:

- **Collide** which allows the entity to collide with other entities or tiles.
- **Fall** which makes the entity be affected by gravity.
- **Jump** which makes the entity jump (if it is on the ground!) when the `w` key is pressed.
- **Move** which makes it possible to move the entity left and right with the `a` and `d` keys respectivly.

Information about creating new behaviours can be found [here](#creating-new-behaviours).

---

## Simplest modifications

### Level Creation

To create a new level for the game you simply have to do the following steps:

1. Create a folder with a name of your choosing in the levels folder.
2. Create an .bmp image named map.bmp which will be your level. The game will later spawn entities and tiles according to the pixel values of the image.
3. Add a [config.ini](#config-details) file in the folder containing at least a General tab with a Name and a Index property.
4. (optional!) You can also add a color-map.ini file if you want to use custom entities or tiles in your level. This file needs to contain a [Colors] tag and then a property with the hex value of the color you want to assign to the tile/entity which maps to the tile/entity class name you want.
   ex:

```ini
[Colors]
FF0000 = Player
```

#### Config details

```ini
[General]
Name = Grass Level
Index = 2
```

The name property is simply a name for the level and can be whatever you want to name your level.
The index property decides which order the levels come in and can be any number >= 1 (if there are more than one with the same index one of them will be selected by random).

There are also several other properties and tags which are optional and will be using the default settings if not present.
These are:

**Physics**

```ini
[Physics]
Gravity = 5
```

Gravity is the downwards acceleration that is applied to falling entities in the level (default 9.82) can be negative!
$$
gravity = \frac{blockheight}{s^2}
$$
**Camera**

There are several different camera modes to choose from, but only choose one per level.

**Camera(Static)**

Static is the simplest mode it defines a camera that is fixed in place and size.

```ini
[Camera]
; Static camera mode
Mode = Static
Blocksize = 10
X = 50
X-unit = percent
Y = 20
Y-unit = tiles
```

The blocksize attribute defines how big (in pixels) a single tile should be.

X, X-unit, Y and Y-unit are all properties to define how the camera should be positioned.

X-unit and Y-unit is either "percent" or "tiles" and defines how much the camera should be offset from its default position (centered in the upper left corner of the level.)

The "Percent" unit means percent of the level width (for x) and height (for y).

**Camera(Follow)**

The follow mode centers the camera on an entity in the level.

```ini
[Camera]
; Follow camera mode
Mode = Follow
Target = Player
Blocksize = 10
```

"Target" is the name of the entity on the map. Make sure that there are no more than one such entity on the map. (The camera can, for instance, not follow two player entities simultaneously)

**Camera(Tile)**

The Tile mode divides the level into smaller sections, and the camera focuses on the section containing its target. (Think Super Mario)

```ini
[Camera]
; Tile Camera mode
Mode = Tile
X = 0
X-span = 20
Y = 0
Y-span = 10
Target = Player
```

### Creating new tiles

Creating new tiles is probably the easiest modification you can do to the game altough a custom level is probably required to use the new tiles.

In the tile mode. Instead of "blocksize", you define how many tiles should be visible height- and width wise.

This is done using the attributes X-span and Y-span.

The X and Y values are used to offset the tiling grid.

Add some info about Camera and GUI in the README

To create a new tile you simply have to create a new folder with the name of the tile (in lowercase letters only) and then put an image with the name of the tile in that folder.
example for tile named Stone:

```
├── tiles
    ├── stone
        └── Stone.png
```

---

## Intermediate Modifications

### Creating new entities

Creating new entities is similar to creating new tiles you create a folder with the name of the entity (folder name needs to be lowercase only) and it in the /entities folder, then put an image with the name of the entity in that folder. After this you need to put a python file with the name of the entity in the folder.
example for an entity called PowerUp:

```
├── entities
    ├── powerup
        ├── PowerUp.py
        └── PowerUp.png
```

The python file needs to contain a class with the name of the entity and it needs to inherit from the base Entity class or another class that does inherit from the Entity class, for example if you want to create an enemy it's probably a good idea to inherit from the character class. The class constructor also needs to take an x, y and a name which also will need to be passed onto the super constructor.

example for an enemy class:

```
from entities.character.Character import Character

class Enemy(Character):
    def __init__(self, x, y, name):
        super().__init__(x, y, name)
        ...
```

Entity also have some default methods that can be overriden to add new features to the game most nobable of these is the update method which is called once every frame and looks like this:

```
def update(self, delta_time, keys, config, state):
    ...
```

- The **delta_time** parameter is the time passed since the last frame and can be used to make sure things run smooth in any framerate, for example for movement you most likely want to multiply the speed with the delta_time to determine the distance to be moved that frame to make sure the movementspeed is consitent every second.
- The **keys** parameter contains information about which keys are currently pressed and originates from pygame.key.get_pressed() more information can be found [here](https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed)
- The **config** parameter the current levels configuration data from it's config.ini, this is useful for things like getting the current gravity or if you want to add/use your own level-unique configs.
- The **state** contains information about the current game state. More information about the state class can be found [here](#the-state-class).

The entity class also has the following methods:

- `set_x(self, x)` set the x position of the entity.
- `set_y(self, y)` set the y position of the entity.
- `set_width(self, width)` set the width position of the entity.
- `set_height(self, height)` set the height position of the entity.
- `add_listener(self, func_name, callback)` which allows you to define which method (`callback`) to be called with the `func_name` event.
- `remove_listener(self, func_name, callback)` removes that listener from the entity.
- `get_behaviour(self, behaviour_name)` get the behaviour with the `behaviour_name` name.
- `register_behaviour(self, behaviour)` add a behaviour to the entity.
- `register_behaviours(self, behaviours)` add the `behaviours` list of behaviours to the entity.
- `update_position(self, delta_time)` moves the entity according to it's current x and y velocities.
- `move_top_to(self, y` moves the entities upmost y position to the `y` position (default same as the y position).
- `get_top(self)` get the upmost y position of the entity (default same as the y position)
- `move_vertical_center_to(self, y)` sets the y position of the entity so that it's vertical center is at the `y` position.
- `move_bottom_to(self, y)` sets the y position of the entity such that the lowest position of the entity is at the `y` position.
- `get_bottom(self)` get the lowest position of the entity.
- `move_left_to(self, x)` sets the x position of the entity such that the leftmost position of the entity is at the `x` position (default same as the x position).
- `get_left(self)` get the leftmost position of the entity (default the x position).
- `move_horizontal_center_to(self, x)` sets the x position such that the center of the entity is at the `x` position.
- `move_right_to`

### Creating new Behaviours

### Changing the UI

The UI is defined by "Views", and each level can optionally have one view associated with it.
To bind a view to a level, you simply have to add `View = ViewName` under the general tag in your config.ini

All views are located as python scripts in the "views" folder.

Here is an example of a very basic "main menu" view.

```python
from src.gui.elements.button.Button import Button
from src.gui.elements.text.TextBlock import TextBlock

def load_view(gui, game):
    gui.add_gui_element(TextBlock("Welcome to my game!", 100, 100))
    gui.add_gui_element(Button("Start Game", 100, 150, lambda: game.load_level(1)))
```

The name of the view is defined by the name of the view file. So this would be MainMenu.py, and the main menu level would have `View = MainMenu` in its config.

---

## Advanced Modifications
