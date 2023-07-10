class Animal:
    def __init__(self, colour, sub_colour):
        self.colour = colour
        self.sub_colour = sub_colour

dog = Animal('black', 'brown')

print(f'Milo is both {dog.colour} and {dog.sub_colour}')