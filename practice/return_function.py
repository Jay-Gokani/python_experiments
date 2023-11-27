from random import randint

def randomiser():
    global randomise
    randomise = randint(1,3)
    return randomise

randomiser()

print(f'The number is {randomise}')


# If having issues with returning the value of a function, make sure:
# The import statement(s) are correct
# The var is global
# `return` is used
# The function is called
# The f string is properly formatted