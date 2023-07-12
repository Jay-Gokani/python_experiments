# dictionary
milo = {
    'colour': 'black',
    'energy': 'high'
}

# print a value
print(milo['colour'])

# print all values
for value in milo.values():
    print(value)

# print all keys
for key in milo.keys():
    print(key)

# print all items
for item in milo.items():
    print(item)

# iterate over keys, values, items
for key, value in milo.items():
    print(f'Milo is {key} {value}')

# get a value of a given key
print(f'Milo is {milo.get("colour")} in colour')

# add an item to the dictionary
milo.setdefault('mood', 'happy')

# remove an item from a dictionary based on a key
del milo['mood']

# remove an item from a dictionary based on a key and return the value
milo.pop('mood')

import pprint

# dictionary
milo = {
    'colour': 'black',
    'energy': 'high'
}

# check if a key is in the dictionary
print('colour' in milo.keys())

# check if a value is in the dictionary
print('black' in milo.values())

# pretty print a one line dictionary
whiskers = {'colour': 'brown', 'food': 'fish', 'toy': 'yarn'}
pprint.pprint(whiskers)

# merge two dictionaries
# this brings all the unique items into dict_d and overwrites any items with any later specified items
# in this example, photons is earlier in the dictionary than nickname but has value 1
dict_a = {'number': '12', 'name': 'Jason'}
dict_b = {'photons': '3', 'nickname': 'Lenny'}
dict_c = {'photons': '1', 'food': 'pizza'}
dict_d = {**dict_a, **dict_b, **dict_c}
print(dict_d)