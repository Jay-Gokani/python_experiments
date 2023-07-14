# Multiline string
print(
"""Hello there,

It's been sunny in Hawaii,
You would love the turles.

From Jay."""
)

x = "Hello there"

# Indexing and slicing

# H
print(x[0])

# e
print(x[-1])

# Hello
print(x[0:5])

# True
print('Hello' in x)

# False
print('hello' in x)

# True
print('Hi' not in x)

# Built in methods

# HELLO THERE
print(x.upper())

# hello there
print(x.lower())

# Hello There
print(x.title())

# False
print(x.islower())

# True
print(x.startswith('Hello'))

# False
print(x.endswith('th'))

# JOIN

x = ['Hi', 'there', 'my', 'friend']

# Hi there my friend
print(' '.join(x))

# Hi, there, my, friend
print(', '.join(x))

# SPLIT

y = 'Fire water ice'

# ['Fire', 'water', 'ice']
print(y.split())

x = 'Hello'

#                          Hello
print(x.rjust(20))

# Hello
# Contains blank spaces at the end
print(x.ljust(10))

#           Hello
print(x.center(20))

# =======Hello========
print(x.center(20, '='))


y = '     Hello     '

# Removes all whitespaces
y.strip()

# Removes whitespace on the left
y.lstrip()

# Removes whitespace on the right
y.rstrip()

z = 'zzzzzzzJayzzz'
# Jay
print(z.strip('z'))