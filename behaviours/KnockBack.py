from behaviours.Behaviour import Behaviour


class KnockBack(Behaviour):
    def __init__(self, mass=10):
        self.mass = mass

    def push(self, velocity, mass):
        self.owner.velocity += velocity * mass / self.mass
