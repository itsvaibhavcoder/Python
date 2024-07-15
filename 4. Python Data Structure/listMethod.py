fruits = ["berries", "apples","grapes","oranges"]
vegetables = ["kale", "broccoli", "lettuce"]

# Method 1 --> extend()
fruits.extend(vegetables)
print(fruits)

# Method 2 --> append()
vegetables.append("bean")
print(vegetables)

# Method 3 --> sort()
# vegetables.sort() # Default ascending A to Z
vegetables.sort(reverse = True) # Descending
print(vegetables)

# Method 4 --> count()
print(fruits.count("berries"))

# Method 5 --> index()
print(fruits.index("grapes"))

# Method 6 --> insert()
fruits.insert(0, "banana")
print(fruits)

# Method 7 --> pop()
fruits.pop()
print(fruits)

# Method 8 --> remove()
vegetables.remove("kale")
print(vegetables)

# Method 9 --> del()
del vegetables
print(vegetables) # Vegetable not exit
