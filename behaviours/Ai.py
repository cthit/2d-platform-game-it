from behaviours.Behaviour import Behaviour
from behaviours.Collide import Collide
from behaviours.Shoot import Shoot
from behaviours.Jump import Jump
from behaviours.Move import Move
from behaviours.Shoot import Shoot
from entities.base.Entity import Entity
from src.GameMethods import GameMethods


class Ai(Behaviour):
    def update(self, delta_time, keys, config, game_methods: GameMethods):
        # Super simple enemy Ai as an example

        # Find player if it is within 10 tiles
        player = self.look_for_player(search_range=10)

        if player is None:
            self.idle()
        else:
            self.move_towards(player)
            self.attack(player)


    def look_for_player(self, search_range=5):
        """Look for the Player entity within a certain range of the owner"""
        c = self.owner.get_behaviour(Collide)
        if c is None:
            return None
        for entity in c.check_around(search_range):
            if entity.name == "Player":
                return entity


    def get_direction_towards(self, entity: Entity):
        if Entity is None:
            return None
        entity_is_left = entity.get_horizontal_center() < self.owner.get_horizontal_center()
        if entity_is_left:
            return "left"
        else:
            return "right"

    def idle(self):
        # Do nothing, maybe walk around (todo)
        pass

    def attack(self, target):
        if self.owner.has_behaviour(Shoot):
            shoot_behaviour = self.owner.get_behaviour(Shoot)
            shoot_behaviour.shoot()

    def move_towards(self, entity):
        # Try to move towards entity
        if self.owner.has_behaviour(Move):
            move_behaviour = self.owner.get_behaviour(Move)
            direction = self.get_direction_towards(entity)
            if direction == "right":
                move_behaviour.move_right()
            elif direction == "left":
                move_behaviour.move_left()

        # Jump if entity is higher up
        if self.owner.has_behaviour(Jump) and self.is_below(entity):
            self.owner.get_behaviour(Jump).jump_if_possible()

    def look_for_player(self, search_range=5):
        """Look for the Player entity within a certain range of the owner"""
        if self.owner.has_behaviour(Collide):
            c = self.owner.get_behaviour(Collide)
            for entity in c.check_around(search_range):
                if entity.name == "Player":
                    return entity

    def get_direction_towards(self, entity: Entity):
        if Entity is None:
            return None
        entity_is_left = entity.get_horizontal_center() < self.owner.get_horizontal_center()
        if entity_is_left:
            return "left"
        else:
            return "right"

    def is_below(self, entity):
        return entity.get_bottom() < self.owner.get_bottom()
