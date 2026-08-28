import entity
import random

class minotaur(entity):
    def __init__(self):
        super().__init__()
        self.health = 200

    def when_killed(self) -> str:
        """drop bag of feathers when killed"""
        return "Bag of Feathers"

    def attack_damage(self) -> int:
        """return damage dealt"""
        attack_damage = random.randrange(1, 21)
        return attack_damage