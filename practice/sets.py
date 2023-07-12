# A set is an unordered collection with no duplicate elements
# Useful for membership testing and de-duping

# Creating a set can be done in two ways
s = {1, 2, 3}
s = set([1, 2, 3])

# Printing values
s = {1, 2, 5, 2, 1, 3, 4}
print(s)

# Unordered, so no indexing - results in an error
print(s[0])

# Adding an element
s.add(6)

# Update is used for multiple ones and can also be used for only one
s.update([7, 8, 9])
s.update([10])

# Remove an element and raise an error if it doesn't exist
# >>> error
s.remove(12)

# Remove an element and don't raise an error if it doesn't exist
s.discard(12)

# Create a new set from the two and print
s2 = {30, 40, 50}
s3 = s.union(s2) # can also use s3 = s | s2
print(s3)

# Intersection, only return elements that are common for all sets
s2 = {3, 4, 5}
s3 = s.intersection(s2) # Can also use s3 = s & s2
print(s3)

# Difference, only show unique elements in the first set specified
s3 = s.difference(s2) # Can also use s3 = s - s2
print(s3)

# Symetric difference, only show unique elements 
s3 = s.symmetric_difference(s2) # Can also use s3 = s ^ s2
print(s3)