# Example 1
def loopy(*args):
    for a in args:
        print(a)

loopy('hello', 'there', 'jim')

# Example 2
print('The animal you say second is your fav')

def zap(*args):
    print("Your fav is " + (args[1]))

zap('lion', 'tiger')

# Kwarg example
def picnic(key, **kwargs):
    print(kwargs.get(key))

picnic('key3', key1='egg', key2='grape', key3='milk')
# milk