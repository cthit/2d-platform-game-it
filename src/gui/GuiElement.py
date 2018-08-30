class GuiElement:
    def __init__(self, pos_x, pos_y, width, height, image = None):
        self.x = pos_x
        self.y = pos_y
        self.width = width
        self.height = height
        self.image = image

    def contains(self, x, y):
        if x <= self.x + self.width and x >= self.x and y <= self.y + self.height and y >= self.y:
            return True
        return False

    def on_mouse_down(self):
        pass

    def on_mouse_up(self):
        pass

    def on_hover(self):
        pass

    def draw(self, surface):
        surface.blit(self.image, (x, y))