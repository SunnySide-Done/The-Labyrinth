import entity

class minotaur(entity):
    def __init__(self):
        super().__init__()
        self.health = 200

    def when_killed(self) -> str:
        """drop bag of feathers when killed"""
        return "Bag of Feathers"

    def attack(self) -> int:
        """return damage dealt"""
        attack_damage = random.randrange(1, 11)
        return attack_damage