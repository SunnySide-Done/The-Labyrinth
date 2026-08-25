import random

class Enemy:
    def __init__(self, rank):
        # M rank is minotaur, N rank is normal monster
        self.rank = rank
        self.health = 100
        
    def attack(self) -> int:
        """Rolls for attack damage done out of 10 and returns the attack damage"""
        attack_damage = random.randrange(1, 11)
        return attack_damage

    def hit(self, damage: int):
        """Changes health of monster based on the damage done by player"""
        self.health -= damage
        return

class BigEnemy(Enemy):
    def __init__():
        self.health = 200

    def attack