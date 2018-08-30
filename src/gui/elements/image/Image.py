from src.gui.GuiElement import GuiElement


class Image(GuiElement):
    def __init__(self, pos_x, pos_y, width=0, height=0, image=None):
        super().__init__(pos_x, pos_y, width, height, image)

    def on_mouse_down(self):
        print("Image was clicked!")