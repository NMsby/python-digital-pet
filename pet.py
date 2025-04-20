class Pet:
    def __init__(self, name):
        """Initialize a new Pet with the given name"""
        self.name = name
        self.hunger = 5  # Starting at middle value (0 = full, 10 = very hungry)
        self.energy = 5  # Starting at middle value (0 = tired, 10 = fully rested)
        self.happiness = 5  # Starting at middle value