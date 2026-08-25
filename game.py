class Game:

    """
    The last few variables will be cleaned up after the room & player is settled
    """


    def __init__(self):
        # Set up game variables
        self.room_number = 0
        self.rooms = []
        pass


    def welcome(self):
        # Display welcome message
        with open("welcome.txt", "r") as f:
            content = f.read()
            print(content)
        pass


    def add_player(self, player):
        #add the player
        self.player = player
        pass

    def is_gameover(self):
        # Return True if game is over
        if self.player.life <= 0:
            return True
        else:
            return False
        pass

    def get_options(self):
        """
        Return available choices.
        This returns what a player CAN do: aka, can they pick up a weapon? 
        which way can they go?
        can they eat ambrosia? 
        Can they use a weapon?
        This is also used in combat.
        """
        pass
        


    def get_actions(self, choice):
        # Return actions based on choice
        """
        Refer to get options and basically this tells the user what they need
        aka: add life? weapon? something along those lines. 
        """
        pass

    def execute(self, actions):
        # Perform the actions
        """
        actually adds life/switches weapons/goes to the next room
        """
        pass

    def status(self):
        # Return current game status
        """
        Confirm what player/enemy/room classes actually contain before coding this.
        """
        pass


    def generate_rooms(self, room_count):
        #Keeps track of what room is created, determines whether a enemy room or healing room is generated.
        #Then, instantiates the room.
        #Ensures that certain rooms (ie, tutorial, boss) are FIXED the moment user reaches certain room number.
        pass
    
