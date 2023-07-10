class Continent:
    def __init__(self, name, climate):
        self.name = name
        self.climate = climate

    def begin(self, begin):
        self.begin = begin
    
class Country(Continent):
    def begin(self, begin):
        self.begin = begin

india = Country('India', 'warm')

india.begin('I')

print(f'{india.name} is {india.climate} and begins with "{india.begin}"')