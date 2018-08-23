from entities.character.Character import Character


class Player(Character):
    def __init__(self, x, y, name):
        super().__init__(x, y, name, 10)

    def update(self, deltaTime, state):
        super().update(self, deltaTime, state)

