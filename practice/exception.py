# This will result in an error due to speech marks missing
# Results in an error stating 'NameError'
print(hello)

# We can try to fulfill the operation and return a certain error if it errors
try:
    print(hello)
except:
    print('Error here')
