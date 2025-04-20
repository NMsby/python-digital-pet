class Pet:
    def __init__(self, name):
        """Initialize a new Pet with the given name"""
        self.name = name
        self.hunger = 5  # Starting at middle value (0 = full, 10 = very hungry)
        self.energy = 5  # Starting at middle value (0 = tired, 10 = fully rested)
        self.happiness = 5  # Starting at middle value
        self.tricks = []  # List to store learned tricks

    def eat(self):
        """Reduces hunger by 3 (not below 0) and increases happiness by 1"""
        self.hunger = max(0, self.hunger - 3)  # Ensure hunger doesn't go below 0
        self.happiness = min(10, self.happiness + 1)  # Ensure happiness doesn't exceed 10
        print(f"{self.name} has eaten and is feeling less hungry!")

    def sleep(self):
        """Increases energy by 5 (not above 10)"""
        self.energy = min(10, self.energy + 5)  # Ensure energy doesn't exceed 10
        print(f"{self.name} had a good sleep and is now more energetic!")

    def play(self):
        """Decreases energy by 2, increases happiness by 2, and increases hunger by 1"""
        self.energy = max(0, self.energy - 2)  # Ensure energy doesn't go below 0
        self.happiness = min(10, self.happiness + 2)  # Ensure happiness doesn't exceed 10
        self.hunger = min(10, self.hunger + 1)  # Ensure hunger doesn't exceed 10
        print(f"{self.name} had a great time playing!")

    def train(self, trick):
        """Teaches pet a new trick and adds it to the tricks' list"""
        if trick in self.tricks:
            print(f"{self.name} already knows how to {trick}!")
        else:
            self.tricks.append(trick)
            self.energy = max(0, self.energy - 1)  # Training takes a bit of energy
            self.happiness = min(10, self.happiness + 1)  # Learning makes pet happy
            print(f"{self.name} has learned to {trick}! 🎓")

    def show_tricks(self):
        """Displays all tricks the pet has learned"""
        if not self.tricks:
            print(f"{self.name} doesn't know any tricks yet.")
        else:
            print(f"\n--- {self.name}'s Tricks ---")
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. {trick}")

    def get_status(self):
        """Prints the current state of the pet"""
        print(f"\n--- {self.name}'s Status ---")
        print(f"Hunger: {self.hunger}/10 {'🍖' * self.hunger}")
        print(f"Energy: {self.energy}/10 {'⚡' * self.energy}")
        print(f"Happiness: {self.happiness}/10 {'😊' * self.happiness}")

        # Add mood description based on stats
        if self.hunger > 7:
            print(f"{self.name} is very hungry!")
        if self.energy < 3:
            print(f"{self.name} is feeling tired...")
        if self.happiness < 3:
            print(f"{self.name} is feeling sad...")
        elif self.happiness > 7:
            print(f"{self.name} is super happy!")