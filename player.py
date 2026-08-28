import entity

class player(entity):
    def __init__(self):
        super().__init__()
        self.inventory = []
    
    def heal(self):
        """
        adds health to the player after drinking ambrosia
        """
        if self.health == 100:
            return
        elif self.health > 80:
            self.health == 100
            return
        else:
            self.health += 20
        return

    def get_inventory(self) -> list:
        """
        gets players inventory and displays in string
        """
        print(self.inventory)
        return


    def set_inventory(self, item: str):  
        """
        adds item to player inventory
        """
        item = item
        print("Choose an item slot. [1-5]")
        wanted_item_position = input("Enter: ")
        while int(wanted_item_position) and int(wanted_item_position) < 6 and int(wanted_item_position) > 0:
            wanted_item_position = input("Enter: ")
        if self.inventory[wanted_item_position] is not None:
            print("Item slot occupied. Switch item? (y/n)")
            switch_item_choice = input("Enter: ")
            while switch_item_choice is not "y" or "n":
                switch_item_choice = input("Enter: ")
            if switch_item_choice is 'y':
                self.inventory[wanted_item_position] = item
                return
            else:
                print("Choose an item slot.")
                player.set_inventory(item)
