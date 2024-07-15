'''
List Data Structure :
-- A list is collection of data can be of mixed type.
-- Items in a list are ordered by thier index and changeable
-- List are created with square backets. []
-- Items in a list can accessed by thier index
-- Each item in a list is separated by comma
'''

animals = ["bear", "tiger", "lion", "panda", "elephant"]

# for x in animals:
#     print(x)

# print(animals)

# Accesing elements of Lists

print(animals[0]) # bear
print(animals[-1]) # elephant

print(animals[1:3]) # 1 inclusive and 3 is exclusive

# How to modify list
animals[0] = "dog"
print(animals) 
