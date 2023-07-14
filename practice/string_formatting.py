n = 'Sohana'
# My name is Sohana
print(f'My name is {n}')

# My name is n='Sohana'
print(f'My name is {n=}')


x = 1209329.4156
# The number is 1209329.4156
print(f'The number is {x}')

# The number is 1,209,329.4156
print(f'The number is {x:,}')

# The number is 1209329.42
print(f'The number is {x:.2f}')

# The number is 1,209,329.42
print(f'The number is {x:,.2f}')


y = 0.6213
# The number is 62.13
print(f'The number is {y:.2%}')


# There's lots of f string formatting options
# See this link for a table: https://www.pythoncheatsheet.org/cheatsheet/string-formatting