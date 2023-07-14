# Regex is a sequence of characters which specifies a search pattern in text
# Lots can be done with regex, this is a handful:

# 1. import re
import re

# 2. Create a regex object with re.compile() and pass the raw string
phone = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

# 3. Pass a search into the search() method which returns a match object
mo = phone.search('My number is 432-524-5172.')

# 4. Call the match object's group() to return a string of the matched text
print(f'Phone number is: {mo.group()}')

# 5. Split by groups if you wish
# 432
print(mo.group(1))

# 524-5172
print(mo.group(2))

# 432-524-5172
print(mo.group(0))

# 432-524-5172
print(mo.group())

# ('432', '524-5172')
print(mo.groups())

area_code, main_number = mo.groups()

# 432
print(area_code)

import re

hero = re.compile (r'Batman|Superman')

mo1 = hero.search('Batman and Superman')
# Batman
print(mo1.group())

mo2 = hero.search('Superman and Batman')
# Superman
print(mo2.group())


# var 1 = re.compile(r'<string>')
# var 2 = var1.search('<string>')

# var2.group(<int>)

animal = re.compile(r'Cat(ch|apult)')
mo = animal.search('Catch the ball')

print(mo.group(0))