# 2d-platform-game-it

A basic game/framework for a 2d-platformer built with python.
The purpose of the project is to be easily modifiable both for people with and without prior coding experience.

---

## Table of Contents

- [2d-platform-game-it](#2d-platform-game-it)
    - [Table of Contents](#table-of-contents)
    - [Installation (Overly explicit)](#installation-overly-explicit)
        - [PyCharm Instructions](#pycharm-instructions)
        - [Unix Instructions (if not runing PyCharm)](#unix-instructions-if-not-runing-pycharm)
            - [General instructions](#general-instructions)
    - [Introduction](#introduction)
    - [General Information](#general-information)
        - [The GameMethods Class](#the-gamemethods-class)
        - [Behaviours](#behaviours)
    - [Simplest modifications](#simplest-modifications)
        - [Level Creation](#level-creation)
            - [Config details](#config-details)
        - [Creating new tiles](#creating-new-tiles)
    - [Intermediate Modifications](#intermediate-modifications)
        - [Creating new entities](#creating-new-entities)
                - [Entities and Behaviours](#entities-and-behaviours)
        - [Creating new Behaviours](#creating-new-behaviours)
        - [Changing the UI](#changing-the-ui)
    - [Advanced Modifications](#advanced-modifications)

---

## Installation (Overly explicit)

1. if you want to use an IDE, we recommend [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows) (We recomend this, especially for Windows users). Which should include a python installation
    - if it does not, install it manually from https://www.python.org/downloads/ or using a package manager 

2. Make sure that you have Git installed on your system if not: 
    - On *Windows* or [Download](https://git-scm.com/downloads) and install using the wizard or install a graphical git client *i.e* [Gitkraken](https://www.gitkraken.com/).
    - On a Linux based system (or Mac) install using your package manager of choice 

3. Clone the project into your prefered folder. 
    - if using GitKraken follow the instructions after installing
    - if using a Terminal

        `cd <Your preffered folder>`

        `git clone https://github.com/cthit/2d-platform-game-it.git`

### PyCharm Instructions
- Launch PyCharm and follow the setup. Open the project using PyCharm

- Click on configure Python interpreter in the top right corner and add a new environment. 

- Add packages pygame, pillow and numpy by clicking on the + and searching for them

Done!

### Unix Instructions (if not runing PyCharm)

- change directive to game directive: `cd 2d-platform-game-it`

- install pip by running `python3 -m pip install pip` (probably requires root access so run with sudo)

- setup a virtual environment by running 

    `python3 -m venv <game environment>` 

    replace \<game environment\> with what your enviroment should be called. (probably also requires sudo) 

    Run `source <game environment>/bin/activate` to activate the virtual environment
- Finally run `pip install pygame pillow numpy`
- You should be now be setup so try running `python3 main.py` if you run into the error no module named src simply run `export PYTHONPATH=.`

Finally if you run into any problem feel free to contact digIT


#### General instructions


## Introduction

The game is built around making it very simple of adding new content to the game and is therefor split into a few different parts:

- Tiles:
  - Basic unmovable block in the game world, basically only an image you can collide with.
- Entities:
  - Anything else in the gameworld, such as the player or the goal flag.
- Behaviours:
  - Entities can have behaviours such as Collide, Jump, Move etc.
- Ui:
  - The ui components are buttons, text, non-entity images that interacts with the player.

All of these are modifiable in different ways which are described below.

---

## General Information

### The GameMethods Class

GameMethods is an object that exposes certain methods of the main Game class:

- `find_entities(name)` returns all entities of the given name
- `go_to_next_level()` clears the current level and loads the next
- `reload_entities()` resets the level to its initial state, might be used for example when the player dies.
- `get_level_dimensions()` returns a tuple with the dimensions of the current level, `(width, height)`.

### Behaviours

Behaviours are used to define the different behaviours of an entity for example some built in behaviours are:

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

```python
from entities.character.Character import Character

class Enemy(Character):
    def __init__(self, x, y, name):
        super().__init__(x, y, name)
        ...
```

Entity also have some default methods that can be overriden to add new features to the game most nobable of these is the update method which is called once every frame and looks like this:

```python
def update(self, delta_time, keys, config, game_methods):
    ...
```

- The **delta_time** parameter is the time passed since the last frame and can be used to make sure things run smooth in any framerate, for example for movement you most likely want to multiply the speed with the delta_time to determine the distance to be moved that frame to make sure the movementspeed is consitent every second.
- The **keys** parameter contains information about which keys are currently pressed and originates from pygame.key.get_pressed() more information can be found [here](https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed)
- The **config** parameter the current levels configuration data from it's config.ini, this is useful for things like getting the current gravity or if you want to add/use your own level-unique configs.
- The **game_methods** object contains methods related to the entire game. More information about the GameMethods class can be found [here](#the-gamemethods-class).

The entity class has the following properties:

- `deletion_pending` a boolean that if set to `True` will remove the entity in the next update.
- `spawn_x` the x spawn position of the entity.
- `spawn_y` the y spawn position of the entity.
- `x` the current x position of the entity.
- `y` the current y position of the entity.
- `width` the width of the entity.
- `height` the height of the entity.
- `velocity` a 2d vector that contains the current frame x and y velocities respectivly (are set to [0, 0] at every update), the x can be accessed through `self.velocity.x` and y through `self.velocity.y`. 
- `behaviours` a list of all the entities behaviours.
- `listeners` a list of all the entities listeners.
- `name` the name of the entity.

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
- `move_right_to(self, x)` sets the x position such that the rightmost part of the entity is at the `x` position.
- `get_right(self)` get the rightmost x position of the entity.
- `clear(self)` Removes the entity from the game
- `__del__(self)` Same as `clear(self)`, called automatically when all references to the object are gone.

##### Entities and Behaviours

Some of these methods are used for adding and getting behaviours so for easy referens, to add a new Behaviour to the entity use the `register_behaviour(self, behaviour)` or `register_behaviours(self, behaviours)` methods (generally called from the constructor, \__init\__). For example, to add the fall behaviour to an entity:

```python
from behaviours.Fall import Fall

...

def __init__(self, x, y, name):
   self.register_behaviour(Fall())
```

If you later want to change something to the behaviour you can access it you can use the ```get_behaviour(self, behaviour_name)``` method. For example to change weather an entity with the collide behaviour is a trigger (get's the collision events but otherwise acts like a ghost) you can do like this:

```python
...
   self.get_behaviour("Collide").is_trigger = True
```

### Creating new Behaviours

To create a new behaviour you simply need to create a python file in the behaviours folder and make inherit from the behaviour class either directly or through another class. The behaviour class constructor takes an optional `owner` parameter which can be used to set the owner of the behaviour at initialization. The Behaviour class also has the following methods:

 - `set_owner(self, new_owner, delta_time, keys, config)` which sets the owner of the behaviour to the `new_owner`.
 - `update(self, delta_time, keys, config)` which by default is called by the base entity class update method once every frame.

You can read more about how to use behaviours with entities [here](#entities-and-behaviours).

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
