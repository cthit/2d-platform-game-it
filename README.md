# 2d-platform-game-it

A basic game/framework for a 2d-platformer built with python. 
The purpose of the project is to be easily modifiable both for people with and without prior coding experience.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Simplest Modifications](#simplest-modifications)
    - [Level Creation](#level-creation)
    - [Creating new tiles](#creating-new-tiles)
3. [Intermediate Modifications](#intermediate-modifications)
    - [Creating new entities](#creating-new-entities)
    - [Changing the UI](#changing-the-ui)
4. [Advanced Modifications](#advanced-modifications)

---

## Introduction

---

## Simplest modifications

### Level Creation
To create a new level for the game you simply have to do the following steps:
1. Create a folder with a name of your choosing in the levels folder.
2. Create an .bmp image named map.bmp which will be your level. The game will later spawn entities and tiles according to the pixel values of the image.
3. Add a [config.ini](#config-details) file in the folder containing at least a General tab with a Name and a Index property.
4. (optional!) You can also add a color-map.ini file if you want to use custom entities or tiles in your level. This file needs to contain a [Colors] tag and then a property with the hex value of the color you want to assign to the tile/entity which maps to the tile/entity class name you want.
ex:
```
[Colors]
FF0000 = Player
```

#### Config details

```
[General]
Name = Grass Level
Index = 2
```
The name property is simply a name for the level and can be whatever you want to name your level.
The index property decides which order the levels come in and can be any number >= 1 (if there are more than one with the same index one of them will be selected by random).

There are also several other properties and tags which are optional and will be using the default settings if not present.
These are:
```
[Physics]
Gravity

[Camera]
; Static camera mode
Mode = Static
Blocksize
X
Y
X-unit
Y-unit

; Follow camera mode
Mode = Follow
Target = Player

; Tile Camera mode
Mode = Tile
; X
; Y
; X-span
; Y-span
; Target = Player
```

Gravity is the downwards acceleration present in the level (default 9.82) can be negative!

### Creating new tiles

Creating new tiles is probably the easiest modification you can do to the game altough a custom level is probably required to use the new tiles.

To create a new tile you simply have to create a new folder with the name of the tile (in lowercase letters only) and then put an image with the name of the tile in that folder.
example for tile named Stone:
```
├── tiles
    ├── stone
        └── Stone.png
```

(What follows is not yet implemented!)
If you want to add new functionality to the tile you can also put a python script with the name of the tile as a name. In that python file create a class with the name of the tile and make sure it inherits from the tiles/base/Tile.py Tile class in some way (either directly or through other tile classes). Also make sure the constructor looks like this:

```
def __init__(self, x, y, name):
    super().__init__(x, y, name)
    ...
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

### Changing the UI

---

## Advanced Modifications
