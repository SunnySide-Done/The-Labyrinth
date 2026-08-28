import random

class entity:
    def __init__(self):
        self.health = 100
        
    def attack_damage(self) -> int:
        """Rolls for attack damage done out of 10 and returns the attack damage"""
        attack_damage = random.randrange(1, 11)
        return attack_damage

    def hit(self, damage: int):
        """Changes health of monster based on the damage done by player"""
        self.health -= damage
        return

    def get_health(self) -> int:
        """returns health of player"""
        return self.health
