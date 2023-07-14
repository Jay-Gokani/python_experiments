# Create a new list from an old one
names = ['Nancy', 'Bart', 'Cleo']

new = [n for n in names]
print(new)

# For numbers
num = [(a, b) for a in range(1, 3) for b in range(1, 3)]
print(num)

# This can also be done for sets and dicts