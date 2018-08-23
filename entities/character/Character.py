from entities.base.Entity import Entity
import pygame

class Character(Entity):

    def __init__(self, x, y, name, movement_speed):
        Entity.__init__(self, x, y, name)
        self.movementSpeed = movement_speed
