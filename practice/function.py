# Basic
def hello():
    print('Hello')

hello()

# Variable
def name():
    print(f'Your name is {x}')

x = input('What is your name? ')

name()

# Function arguments
def full(first, second):
    print(f'Your name is {first} {second}') 

full('Jay', 'Gokani')

# Function argument with user inputs
def full(first, second):
    print(f'Your name is {first} {second}') 

x = input('What is your first name? ')
y = input('What is your second name? ')

full(x, y)

# Math function
def sum(first, second):
    return first + second

first = input('Choose a number ')
second = input('Choose a second number ')

result = sum(int(first), int(second))

print(result)

# Global and local variables
def animal():
    # This line makes it global. If not used, the final print will fail
    global colour
    colour = 'pink'
    print(colour)

animal()    

print(f'Pig is {colour}')