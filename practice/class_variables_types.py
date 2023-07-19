class Animal:
    def __init__(self, name, size, ears, teeth):
        self.name    = name
        self.size    = size
        self._ears   = ears
        self.__teeth = teeth

        # Private variable can be used within the class, like below (but not outside)
        print(self.__teeth)

tiger = Animal('Tiger', 'med', 2, 10)

# This can be accessed inside the class and in subclasses
# Intended to be used in the class or subclass
print(tiger._ears)

# Throws an error as it can't be accessed outside the class or in subclasses
print(tiger.__teeth)