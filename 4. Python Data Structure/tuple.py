'''
Tuple : A tuple is a list that can not be changed. (immutable)
can be created using paranthesis () and with a constructor
Elements in a tuple can be accessed by thier index.
'''
fruits = ("grapes", "apples", "berries")

# Traversing of tuple
for x in fruits:
    print(x)

print(fruits[2]) # berries

# Using constuctor
animals = tuple(("lion", "tiger", "bear"))
print(type(animals))
print(animals)
print(animals[1])
print(len(animals))

# animals.add("dog")
print(animals)

del animals
