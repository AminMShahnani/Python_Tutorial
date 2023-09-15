"""
Sets e similar to lists but are unordered and cannot contain duplications
Use curly brackets
"""

my_set = {1, 2, 3, 4, 5, 3, 2, 0}
print(my_set)
print(len(my_set))

for x in my_set:
    print(x)

print(my_set[0]) # GET ERROR : TypeError: 'set' object is not subscriptable

print(my_set)
my_set.discard(3)
print(my_set)
my_set.clear()
print(my_set)
my_set.add(8)
print(my_set)
my_set.update([7,4])
print(my_set)

