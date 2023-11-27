# General structure is \x where x is the character to escape like:
# ' " \

# New line
# Hello. 
# Jay's hat is yellow.
print('Hello. \nJay\'s hat is yellow.')

# Tab
# Hello.  Jay's hat is yellow.
print('Hello. \tJay\'s hat is yellow.')

# I'm doing fine
print('I\'m doing fine')

# Raw strings ignore any escapes
# I\'m doing fine
print(r'I\'m doing fine')