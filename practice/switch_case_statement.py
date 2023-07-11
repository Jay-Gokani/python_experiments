# Switch-case statement

starter = 'Squirtle'

# Matching the string
match starter:
    case 'Bulbasaur':
        print('Bulbasaur is a grass/poison type')
    case 'Charmander':
        print('Charmander is a fire type')
    case 'Squirtle':
        print('Squirtle is a water type')
    case _:
        print('Invalid choice')

# Setting valid responses in one line
match starter:
    case 'Bulbasaur' | 'Squirtle' | 'Charmander':
        print('Valid choice')
    case _:
        print('Invalid choice')