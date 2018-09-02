from src.camera.BoundingBox import BoundingBox


def get_bounding_box(camera_settings, screen, level, target):
    x = target.get_horizontal_center()
    y = target.get_vertical_center()
    x_offset = float(camera_settings["x"])
    y_offset = float(camera_settings["y"])
    x_span = float(camera_settings["x-span"])
    y_span = float(camera_settings["y-span"])
    x += x_offset
    y += y_offset
    x -= (x % x_span) + x_offset
    y -= (y % y_span) + y_offset

    block_size_x = screen.get_size()[0] / x_span
    block_size_y = screen.get_size()[1] / y_span
    return BoundingBox((x, x + x_span), (y, y + y_span), block_size_x, block_size_y)
