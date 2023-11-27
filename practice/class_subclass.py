# Parent class
class Pokemon:
    def __init__(self, name):
        self.name = name
    def speak(self):
        self.speak = ""

# Child class 1
class Fire(Pokemon):
    def speak(self):
        print('Bark')

# Child class 2
class Grass(Pokemon):
    def speak(self):
        print('Growl')

# Calling child class 1
charmander = Fire("Charmander")
charmander.speak()

# Calling child class 2
bulbasaur = Grass("Bulbasaur")
bulbasaur.speak()
