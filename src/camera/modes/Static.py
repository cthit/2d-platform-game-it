from src.camera.BoundingBox import BoundingBox


def get_bounding_box(camera_settings, screen, level, target):
    block_size = float(camera_settings["blocksize"])
    x = level.get_x(float(camera_settings["x"]), camera_settings["x-unit"])
    y = level.get_y(float(camera_settings["y"]), camera_settings["y-unit"])

    width = screen.get_size()[0] / block_size
    height = screen.get_size()[1] / block_size

    x -= width / 2
    y -= height / 2
    return BoundingBox((x, x + width), (y, y + height), block_size, block_size)
