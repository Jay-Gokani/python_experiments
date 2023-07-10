# Print string
print('Hello')

# Variables
dan_age = 50
eddie_surname = 'Coom'

# Print variable
name = 'Dan'
print(name)

# Function
def question():
    # This line makes the var global, i.e. usable outside of the function
    global answer
    answer = input('How old are you?')

# Question
name = input('What is your first name? ')
if name == 'Eddie':
    eddie_surname = input('What is your surname? ') 

# Detemination
if name == 'Dan':
    if dan_age > 25:
        question()
        print(f'I am Dan, {answer} years old')
    else:
        print('I am Dan, a young man')
elif name == 'Eddie':
    if eddie_surname != 'Coom':
        print('I am not Eddie Coom')
    else:
        print('My name is Eddie Coom')
else:
    print(f'My name is {name}')