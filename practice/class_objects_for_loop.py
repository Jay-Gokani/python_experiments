class Pokemon:
    def __init__(self, number, name, type):
        self.number = number
        self.name = name
        self.type = type
    
    def extra(self, size, colour):
        self.size = size
        self.colour = colour

bulbasaur = Pokemon(1, 'Bulbasaur', 'Grass')
squirtle = Pokemon(4, 'Squirtle', 'Water')
charmander = Pokemon (7, 'Charmander', 'Fire')

bulbasaur.extra('small', 'green'),
squirtle.extra('round', 'blue'),
charmander.extra('tall', 'red')

starters = [bulbasaur, squirtle, charmander]

for i in starters:
    print(f'{i.name} is number {i.number} in the Pokedex. It\'s a {i.type} type and is {i.size} and {i.colour}.')
