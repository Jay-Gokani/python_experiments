# List
# Ordered, indexable, mutable 
names = ['Jay', 'Lauren', 'Milo']

# Tuple
# Ordered, indexable, immutable
names = ('Jay', 'Lauren', 'Milo')

# Set
# Unordered, unindexable, mutable
names = {'Jay', 'Lauren', 'Milo'}

# Dictionary
# Ordered, indexable, mutable, key-values
names = {
    'Jay': 'Boy',
    'Lauren': 'Girl',
    'Milo': 'Boy'
}

# Function
# Reusable code which is invoked when called
def hello():
    print('Hello')

hello()

# Class
# Blueprint objects
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# And object    
milo = Dog('Milo', '2')

print(milo.age)

# Variable
colour = 'blue'
size = 'small'

# Conditional
if colour == 'blue':
    print('Blueberry')
elif colour == 'purple':
    if size == 'small':
        print('Grape')
    else:
        print('plumb')
else:
    print('Fruit unavailable')

# Case
# Quicker conditionals for simple uses
match colour:
    case 'blue':
        print('Sweet')
    case _:    
        print('Invalid choice')


# For loop
# Loop through elements and perform an operation
tickets = [1, 2, 3]
for ticket in tickets:
    print(ticket)

# While loop
# While something is a condition 
import sys

tickets = [1, 2, 3]

while True:
    for ticket in tickets:
        print(ticket)
        if ticket == 2:
            sys.exit()