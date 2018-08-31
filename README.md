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
3. Add a config.ini file in the folder containing at least a General tab with a Name and a Index property, (look at an example below)
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

---

## Intermediate Modifications

### Creating new entities

### Changing the UI

---

## Advanced Modifications
