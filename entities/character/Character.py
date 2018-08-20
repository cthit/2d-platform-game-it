from entities.base.Entity import Entity

class Character(Entity):

    def __init__(self, x, y, name, movement_speed = 10):
        Entity.__init__(self, x, y, name)
        self.movementSpeed = movement_speed
        self.acceleration = (0, 0)
        self.onFloor = False

    def update(self, deltaTime, state):
        self.y = self.y + (deltaTime * state.gravity)