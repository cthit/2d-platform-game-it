from entities.base.Entity import Entity

class Character(Entity):

    def __init__(self, x, y, name, movementSpeed):
        Entity.__init__(self, x, y, name)
        self.movementSpeed = movementSpeed

    def update(self, deltaTime, state):
        self.y = self.y + (deltaTime * state.gravity)