class Bulbasaur():
    def __init__(self):
        self.num = 1
        self.type = "grass"

fruitroot = Bulbasaur()
print(fruitroot.num)

class Charmander():
    def __init__(self):
        self.num = 4
        self.type = "fire"

lizard = Charmander()
print(lizard.num)

# Using variables from two methods each in their own class
print(lizard.num + fruitroot.num)


##############################

class Bulbasaur():
    def __init__(self):
        self.num = 1
        self.type = "grass"
    def stats(self):
        self.attack = 7
        self.defence = 10

class Charmander():
    def __init__(self):
        self.num = 4
        self.type = "fire"
    def stats(self):
        self.attack = 15
        self.defence = 5

fruitroot = Bulbasaur()
lizard = Charmander()

# This works fine
print(fruitroot.type)

# This doesn't work as the method hasn't been initialised
print(fruitroot.attack)

# This works
fruitroot.stats()
print(fruitroot.attack)

# Call the other instance's method
lizard.stats()

# Now the values in the methods are accessible
print(lizard.attack - fruitroot.defence)