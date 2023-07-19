# Instead of a call...
class Pokemon:
    def __init__(self, name, number):
        self.name = name
        self.number = number

# A dataclass can be used...

from dataclasses import dataclass

@dataclass
class Pokemon:
    name: str
    number: int

charmander = Pokemon('Charmander', 4)

# Charmander
print(charmander.name)