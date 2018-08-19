from PIL import Image
from numpy import *


def load_map(uri):
    temp = Image.open(uri)
    A = array(temp)  # Creates an array, white pixels==True and black pixels==False
    print(A)


load_map("../../levels/level1/test-map.bmp")
