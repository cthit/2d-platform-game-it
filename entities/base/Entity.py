import os
from pdb import set_trace

import pygame

from behaviours import Collide


class Entity:

    def __init__(self, x, y, name):
        self.x = x  # do not modify directly, use self.set_x
        self.y = y  # do not modify directly, use self.set_y
        self.width = 1  # do not modify directly, use self.set_width
        self.height = 1  # do not modify directly, use self.set_height
        self.velocity = pygame.math.Vector2(0, 0)
        self.behaviours = { }
        self.listeners = {}
        self.name = name
        self.velocity = pygame.math.Vector2(0, 0)
        self.onFloor = False
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../" + name.lower() + "/" + name + ".png")
        try:
            self.sprite = pygame.image.load(path)
        except:
            print("Could not load sprite for " + name)


    def update(self, deltaTime, state):
        if not self.onFloor:
            self.velocity.y = (self.velocity.y + state.gravity)

        self.y = self.y + self.velocity.y * deltaTime
        self.x = self.x + self.velocity.x * deltaTime
        self.velocity.x = 0

    def set_x(self, x):
        self.x = x
        if "set_x" in self.listeners:
            for listener in self.listeners["set_x"]:
                listener[1]()

    def set_y(self, y):
        self.y = y
        if "set_y" in self.listeners:
            for listener in self.listeners["set_y"]:
                listener[1]()

    def set_width(self, width):
        self.width = width
        if "set_width" in self.listeners:
            for listener in self.listeners["set_width"]:
                listener[1]()

    def set_height(self, height):
        self.height = height
        if "set_height" in self.listeners:
            for listener in self.listeners["set_height"]:
                listener[1]()


    def add_listener(self, func_name, callback):
        if func_name in self.listeners:
            self.listeners[func_name].append((func_name, callback))
        else:
            self.listeners[func_name] = [(func_name, callback)]

    def remove_listener(self, func_name, callback):
        if func_name in self.listeners and (func_name, callback) in self.listeners[func_name]:
            self.listeners[func_name].remove((func_name, callback))
        return

    def get_behaviour(self, behaviour_name):
        if not isinstance(behaviour_name, str):
            behaviour_name = behaviour_name.__name__
        if behaviour_name in self.behaviours:
            return self.behaviours[behaviour_name]
        else:
            return None

    def register_behaviour(self, behaviour):
        behaviour.set_owner(self, None, None, None)
        self.behaviours[type(behaviour).__name__] = behaviour

    def register_behaviours(self, behaviours):
        for name, behaviour in behaviours.items():
            self.register_behaviour(behaviour)

    def update(self, delta_time, keys, config):
        for name, behaviour in self.behaviours.items():
            behaviour.update(self, delta_time, keys, config)
        self.update_position(delta_time)

    def update_position(self, delta_time):
        dx = delta_time * self.velocity.x
        dy = delta_time * self.velocity.y

        c = self.get_behaviour(Collide.Collide)
        if c is None:
            self.set_y(self.y + dy)
            self.set_x(self.x + dx)
        else:
            if dy < 0:
                colliding_top = c.check_top(abs(dy))
                if len(colliding_top) <= 0:
                    self.set_y(self.y + dy)
                else:
                    self.move_top_to(Collide.get_bottom_most_of(colliding_top).get_bottom())
                    self.velocity.y = 0
            else:
                colliding_bottom = c.check_bottom(abs(dy))
                if len(colliding_bottom) <= 0:
                    self.set_y(self.y + dy)
                else:
                    self.move_bottom_to(Collide.get_top_most_of(colliding_bottom).get_top())
                    self.velocity.y = 0
            if dx < 0:
                colliding_left = c.check_left(abs(dx))
                if len(colliding_left) <= 0:
                    self.set_x(self.x + dx)
                else:
                    self.move_left_to(Collide.get_right_most_of(colliding_left).get_right())
                    self.velocity.x = 0
            else:
                colliding_right = c.check_right(abs(dx))
                if len(colliding_right) <= 0:
                    self.set_x(self.x + dx)
                else:
                    self.move_right_to(Collide.get_left_most_of(colliding_right).get_left())
                    self.velocity.x = 0

    def move_top_to(self, y):
        self.set_y(y)

    def get_top(self):
        return self.y

    def move_vertical_center_to(self, y):
        self.set_y(y - self.height / 2)

    def get_vertical_center(self):
        return self.y + self.height / 2

    def move_bottom_to(self, y):
        self.set_y(y - self.height)

    def get_bottom(self):
        return self.y + self.height

    def move_left_to(self, x):
        self.set_x(x)

    def get_left(self):
        return self.x

    def move_horizontal_center_to(self, x):
        self.set_x(x - self.width / 2)

    def get_horizontal_center(self):
        return self.x + self.width / 2

    def move_right_to(self, x):
        self.set_x(x - self.width)

    def get_right(self):
        return self.x + self.width
