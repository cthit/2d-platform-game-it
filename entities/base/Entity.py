class Entity:

    def __init__(self, x, y, name):
        self.spawnX = x
        self.spawnY = y
        self.name = name

    def update(self, deltaTime, state):
        self.y -= state.gravity * deltaTime;

