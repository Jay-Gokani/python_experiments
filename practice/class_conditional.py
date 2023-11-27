class Animal:
    def __init__(self, colour, sub_colour):
        self.colour = colour
        self.sub_colour = sub_colour

dog = Animal('brown', True)

if dog.colour == 'brown':
    print('Dog is brown')
    if dog.sub_colour == True:
        print('Dog also has another colour')
else:
    print('Dog colour unknown')
