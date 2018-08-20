import importlib
from importlib import import_module
import os

import configparser as configparser
from PIL import Image
from numpy import *


def load_class(path):
    class_name = os.path.splitext(os.path.basename(path))[0]
    spec = importlib.util.spec_from_file_location("dynamic_load.entities." + class_name, path)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    foo.MyClass()


def load_map(uri):
    temp = Image.open(uri)
    a = array(temp)
    print(a)


def to_hex(h):
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def get_color_map():
    config = configparser.ConfigParser()
    config.read("../../levels/default/color-map.ini")
    for key in config["Colors"]:
        print(to_hex(key), config["Colors"][key])


load_map("../../levels/level1/map.bmp")

get_color_map()

print([f for f in os.scandir("..\..\levels") if f.is_dir()])
