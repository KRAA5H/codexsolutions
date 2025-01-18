class Pokemon:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught

    def speak(self):
        print(f"{self.name}! " * 2)

    def display_details(self):
        for item, value in vars(self).items():
            print(f"{item}: {value}")


pikachu = Pokemon(
    25,
    "Pikachu",
    ["Electric"],
    "A mouse-like Pokémon that has electric abilities.",
    True,
)
charmander = Pokemon(
    4,
    "Charmander",
    ["Fire"],
    "A small lizard Pokémon that has a flame on its tail.",
    False,
)
bulbasaur = Pokemon(
    1,
    "Bulbasaur",
    ["Grass", "Poison"],
    "A seed Pokémon that has a plant bulb on its back.",
    True,
)

pikachu.speak()
charmander.speak()
bulbasaur.speak()

pikachu.display_details()
charmander.display_details()
bulbasaur.display_details()
