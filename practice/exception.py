# This will result in an error due to speech marks missing
# Results in an error stating 'NameError'
print(hello)

# We can try to fulfill the operation and return a certain error if it errors
try:
    print(hello)
except:
    print('Error here')

############

try:
    # Code being tested, which might raise an exception
    result = 10 / 2
    # An exception which is being tested for. If The try results in a 'ZeroDivisionError' exception, the try block doesn't conclude and the except block does. We can have multiple of these for trying to catch different exceptions.
except ZeroDivisionError:
    print("Error: Division by zero")
    # If none of the exeptions were triggered, the else block is raised
else:
    print(f"Result: {result}")
    # Whether an exception was raised or not, the finally block is executed, which can be good for cleanup
finally:
    print("Execution completed, performing cleanup if necessary")
