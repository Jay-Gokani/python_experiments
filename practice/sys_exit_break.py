import sys

numbers = [1, 2, 3, 4, 5]

# Exits the programme when a condition is met
# sys.exit terminates the programme while break exits a loop which will cause this loop to just loop through 1:3
while True:
    for number in numbers:
        print(number)
        if number == 3:
            sys.exit()
            # break