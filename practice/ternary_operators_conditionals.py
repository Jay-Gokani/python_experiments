# Ternary operators - conditional on one line

age = 19

# standard
if age < 18:
    if age < 13:
        print('kid')
    else:
        print('teen')
else:
    print('adult')

# equivalent to
print('kid' if age < 13 else 'teen' if age < 18 else 'adult')