<<<<<<< HEAD
<<<<<<< HEAD
class Player:
    def __init__(self):
        

=======
class data:
    def __init__(self):
            self.data = data
>>>>>>> origin/main
=======
import random

class entity:
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

class minotaur(entity):
    def __init__():
        self.health = 200

    def attack

class inventory_slot:
    def __init__(self, item):
        self.item = item

class player:
    def __init__(self):
        data.health = 100
        data.inventory = none

    def add_item(self, item):
        added_item = inventory_slot(item)
        return

    def get_item(self, slot_num):

class rooms:


def create_player():
    player = player()
>>>>>>> origin/jieyu
