import configparser
import importlib.util
from pdb import set_trace

import numpy as np

from PIL import Image
import os

from tiles.base.Tile import Tile

level_paths = {}
level_configs = {}
entity_map = {}


image_file_formats = [".png", ".jpg", ".jpeg", ".bmp"]

def constructor_factory(constructor, name):
    return lambda x, y: constructor(x, y, name)

def load_entity_map():
    for path in [f.path for f in os.scandir("../entities") if f.is_dir()]:
        path = [x for x in os.scandir(path) if os.path.splitext(x)[1] == ".py"][0]
        class_name = os.path.splitext(os.path.basename(path))[0]
        if ' ' in class_name:
            raise ValueError("Entities cannot have spaces in their names, '" + class_name + "'")
        spec = importlib.util.spec_from_file_location("dynamic_load.entities." + class_name, path)
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)
        class_constructor = getattr(foo, class_name)
        entity_map[class_name] = constructor_factory(class_constructor, class_name)

    for path in [f.path for f in os.scandir("../tiles") if f.is_dir()]:
        paths = [x for x in os.scandir(path) if os.path.splitext(x)[1] in image_file_formats]
        if len(paths) <= 0:
            continue
        path = paths[0]
        class_name = os.path.splitext(os.path.basename(path))[0]
        if ' ' in class_name:
            raise ValueError("Tiles cannot have spaces in their names, '" + class_name + "'")
        entity_map[class_name] = constructor_factory(Tile, class_name)

load_entity_map()


def load_levels():
    for path in [f.path for f in os.scandir("../levels") if f.is_dir()]:
        config = configparser.ConfigParser()
        config.read(path + "/config.ini")
        level_name = config["General"]["Name"]
        level_paths[level_name] = path
        level_configs[level_name] = config


load_levels()


def hex_to_rgb(h):
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def load_config(path):
    config = configparser.ConfigParser()
    config.read(path)
    return config


default_color_map = load_config("../levels/default/color-map.ini")


# returns a dictionary that maps rgb tuples to entity constructors
# @param entity_map: a dictionary that maps entity names to entity constructors.
def get_color_map(level):
    color_map = {}
    config = combine_configs(load_config(level.path + "/color-map.ini"), default_color_map)
    for key in config["Colors"]:
        color_map[hex_to_rgb(key)] = entity_map[config["Colors"][key]]
    return color_map


def combine_configs(c1, c2):
    combined = {}
    for category in list(set().union(c1.keys(), c2.keys())):
        combined[category] = {**(c2[category] if category in c2 else {}), **(c1[category] if category in c1 else {})}
    return combined


def load_entities(level):
    entities = []
    tiles = []
    color_map = get_color_map(level)
    arr3d = np.array(Image.open(level.path + "/map.bmp"))

    for ix, iy in np.ndindex(arr3d.shape[:2]):
        rgb = tuple(arr3d[ix, iy])
        if rgb in color_map:
            entity = color_map[rgb](iy, ix)
            if isinstance(entity, Tile):
                tiles.append(entity)
            else:
                entities.append(entity)

    return entities, tiles


class Level:
    def __init__(self, name):
        if name == "Default":
            raise ValueError("Do not instantiate the default level")
        print(level_paths.keys())
        self.path = level_paths[name]
        self.config = combine_configs(level_configs[name], level_configs["Default"])
        self.name = name
        print(self.config)

    def load(self):
        self.entities, self.tiles = load_entities(self)
        return
