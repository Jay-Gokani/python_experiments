class Animal:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
    
    def speak(self, greeting, mood):
        self.greeting = greeting
        self.mood = mood

milo = Animal('Milo', 'black')

milo.speak('cheerio', 'cheeky')

print(f'The name is {milo.name}, my hide is {milo.colour} - {milo.greeting}! (He said in a {milo.mood} tone)...')