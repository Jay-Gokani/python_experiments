pets = ['dog', 'cat', 'mouse']

# cat
print(pets[1])

# mouse
print(pets[-1])

# The dog chased the cat
print(f'The {pets[0]} is chased the {pets[1]}')

# cat, mouse
# from 1 until but not including 3 (i.e. 1 to 2)
print(pets[1:3])

# dog, cat, mouse
print(pets[:])

# 3
print(len(pets))

# dog, cat, mouse
for pet in pets:
    print(pet)

for index, item in enumerate(pets):
    print(f'index: {index} - pet: {item}')

# 0
print(pets.index('dog'))

# dog, cat, mouse, snake
pets.append('snake')
print(pets)

# dog, chicken, cat, mouse, snake
pets.insert(1, 'chicken')
print(pets)

# dog, cat, mouse, snake
pets.remove('chicken')
print(pets)

# dog, chicken, mouse, snake
del pets[2]
print(pets)

# cat, dog, snake
pets.sort()
print(pets)