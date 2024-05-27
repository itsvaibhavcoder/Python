# Dictionary -- mutable (key-value pairs)
#Creating a Dictionary
my_dict = {"name": "John", "age": 25, "city": "New York"}

#Accessing Values
name_value = my_dict["name"]

#Modifying Values
my_dict["age"] = 26

#Adding and Removing Key-Value Pairs
my_dict["gender"] = "Male"
removed_value = my_dict.pop("city")

#Checking if a Key is in the Dictionary
is_present = "age" in my_dict
print(is_present)

#Getting Keys and Values
all_keys = my_dict.keys()
print(all_keys)
all_values = my_dict.values()
print(all_values)
all_items = my_dict.items()
print(all_items)

#Length of a Dictionary
length = len(my_dict)
print(length)