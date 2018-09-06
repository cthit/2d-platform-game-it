import os
import string
from pdb import set_trace
from typing import TypeVar, Union, Type

import pygame

from behaviours import Collide
from src.GameMethods import GameMethods
from src.utils.ClassGetter import get_class_that_defined_method
from src.utils.Renderable import Renderable

image_file_formats = [".png", ".jpg", ".jpeg", ".bmp"]


class Entity:

    def __init__(self, x, y, name):
        self.friction_coefficient = 10
        self.deletion_pending = False
        self.spawn_x = x
        self.spawn_y = y
        self.x = x  # do not modify directly, use self.set_x
        self.y = y  # do not modify directly, use self.set_y
        self.width = 1  # do not modify directly, use self.set_width
        self.height = 1  # do not modify directly, use self.set_height
        self.behaviours = {}
        self.listeners = {}
        self.name = name
        self.remain_on_reset = False
        self.velocity = pygame.math.Vector2(0, 0)
        self.register_behaviour(Collide.Collide())
        self.is_dead = False
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../" + name.lower())
        image_paths = [x for x in os.scandir(path) if os.path.splitext(x)[1] in image_file_formats]
        image_paths.sort(key=lambda x: x.name.lower().startswith(self.name.lower()))
        try:
            self.sprite = pygame.image.load(image_paths[0].path)
        except:
            print("Could not load sprite for " + name)

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def add_listener(self, func_name, callback):
        func = getattr(self, func_name)
        if func.__name__ != "patched_func":
            cls = get_class_that_defined_method(func)
            name = func.__name__
            cls_func = getattr(cls, name)

            def patched_func(self, *args, **kwargs):
                cls_func(self, *args, **kwargs)
                if func_name in self.listeners:
                    for listener in self.listeners[func_name]:
                        listener()

            setattr(cls, name, patched_func)
            func = getattr(cls, name)
        if func in self.listeners:
            self.listeners[func_name].append(callback)
        else:
            self.listeners[func_name] = [callback]

    def remove_listener(self, func_name, callback):
        if func_name in self.listeners and callback in self.listeners[func_name]:
            self.listeners[func_name].remove(callback)
        return

    T = TypeVar('T', bound='Behaviour')

    def has_behaviour(self, behaviour_type: Type[T]) -> bool:
        if not isinstance(behaviour_type, str):
            behaviour_name = behaviour_type.__name__
        else:
            behaviour_name = behaviour_type
        return behaviour_name in self.behaviours

    def get_behaviour(self, behaviour_type: Type[T]) -> T:
        if not isinstance(behaviour_type, str):
            behaviour_name = behaviour_type.__name__
        else:
            behaviour_name = behaviour_type
        if behaviour_name in self.behaviours:
            return self.behaviours[behaviour_name]
        else:
            return None

    def register_behaviour(self, behaviour: T) -> T:
        behaviour.set_owner(self, None, None, None)
        self.behaviours[type(behaviour).__name__] = behaviour
        return behaviour

    def register_behaviours(self, behaviours):
        for name, behaviour in behaviours.items():
            self.register_behaviour(behaviour)

    def update(self, delta_time, keys, config, game_methods: GameMethods):
        self._game_methods = game_methods
        for name, behaviour in self.behaviours.items():
            behaviour.update(delta_time, keys, config, game_methods)
            if self.is_dead:
                return

        self.update_position(delta_time)
        if self.deletion_pending:
            self.clear()

    def die(self):
        self._game_methods.kill_entity(self)

    def update_position(self, delta_time):
        dx = delta_time * self.velocity.x
        dy = delta_time * self.velocity.y

        c = self.get_behaviour(Collide.Collide)
        if c is None or not c.affects_motion:
            self.set_y(self.y + dy)
            self.set_x(self.x + dx)
        else:
            friction = (1 / (1 + self.friction_coefficient)) ** delta_time
            if dy < 0:
                colliding_top = c.check_top(abs(dy))
                if len(colliding_top) <= 0:
                    self.set_y(self.y + dy)
                else:
                    self.move_top_to(Collide.get_bottom_most_of(colliding_top).get_bottom())
                    self.velocity.y = 0
                    self.velocity.x *= friction
            else:
                colliding_bottom = c.check_bottom(abs(dy))
                if len(colliding_bottom) <= 0:
                    self.set_y(self.y + dy)
                else:
                    self.move_bottom_to(Collide.get_top_most_of(colliding_bottom).get_top())
                    self.velocity.y = 0
                    self.velocity.x *= friction
            if dx < 0:
                colliding_left = c.check_left(abs(dx))
                if len(colliding_left) <= 0:
                    self.set_x(self.x + dx)
                else:
                    self.move_left_to(Collide.get_right_most_of(colliding_left).get_right())
                    self.velocity.x = 0
                    self.velocity.y *= friction
            else:
                colliding_right = c.check_right(abs(dx))
                if len(colliding_right) <= 0:
                    self.set_x(self.x + dx)
                else:
                    self.move_right_to(Collide.get_left_most_of(colliding_right).get_left())
                    self.velocity.x = 0
                    self.velocity.y *= friction

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

    def get_renderables(self):
        res = [Renderable(self.x, self.y, self.width, self.height, self.sprite)]
        for behavior in self.behaviours.values():
            res.extend(behavior.get_renderables())
        return res

    def reset(self):
        if not self.remain_on_reset:
            self.die()
            return
        self.set_x(self.spawn_x)
        self.set_y(self.spawn_y)
        self.velocity = pygame.math.Vector2(0, 0)

    def clear(self):
        self.deletion_pending = True
        c = self.get_behaviour(Collide.Collide)
        if c is not None:
            c.clear()

    def __del__(self):
        self.clear()
