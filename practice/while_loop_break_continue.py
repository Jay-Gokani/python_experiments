# Simple
spam = 0

while spam < 5:
    print(f'Count is {spam + 1}')
    spam += 1


# Taking multiple names
while True:
    name = input('What is your name? ')
    if name == 'your name':
        print('How clever of you...')
        break
    else:
        print(f'Hello {name}')

# Continue keeps looping
# This will occur until the name is Joe
while True:
    name = input('What is your name? ')
    if name != 'Joe':
        continue
    else:
        print('Welcome, Joe...')
        break

# Exit programme before 2 is reached
import sys

tickets = [1, 2, 3]

for ticket in tickets:
    while ticket !=2:
        print(ticket)
        sys.exit()