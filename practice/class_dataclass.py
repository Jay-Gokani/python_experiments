# Instead of a class...
class Pokemon:
    def __init__(self, name, number):
        self.name = name
        self.number = number

# A dataclass can be used for conciseness...
from dataclasses import dataclass

@dataclass
class Pokemon:
    name: str
    number: int

charmander = Pokemon('Charmander', 4)

# this prints 'Charmander'
print(charmander.name)