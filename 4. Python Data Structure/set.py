'''
Set : A set is a collection of
values.
Values in a set are not ordered
because  they have not index you can add values to a set nut not change values
set contain unique values only
'''

fruits = {"grapes", "apples", "berries"}

for fruit in fruits:
    print(fruit)

# Using constructor
animals = {("lion","tiger","bear")}
print(type(animals))

#len function
print(len(fruits))

# Set methods
fruits.add("oranges")
print(fruits)

fruits.update(["mango", "kiwi"])
print(fruits)

fruits.remove("kiwi")
print(fruits)

fruits.clear()
print(fruits)

del animals
print(animals)
