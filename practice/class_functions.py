class Animal:
    def __init__(self, colour, species):
        self.colour = colour
        self.species = species
    
    def hello (self, greeting):
        self.greeting = greeting 

milo = Animal('black', 'dog')

milo.hello('hiya')

print(f'Milo is a {milo.colour} {milo.species} who says {milo.greeting}')