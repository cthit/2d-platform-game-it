from src.camera.BoundingBox import BoundingBox


def get_bounding_box(camera_settings, screen, level, target):
    block_size = float(camera_settings["blocksize"])
    x = target.get_horizontal_center()
    y = target.get_vertical_center()

    width = screen.get_size()[0] / block_size
    height = screen.get_size()[1] / block_size

    x -= width / 2
    y -= height / 2
    return BoundingBox((x, x + width), (y, y + height), block_size, block_size)