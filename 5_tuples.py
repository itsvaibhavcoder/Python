#tuples are immutable 
#Creating tuples 
my_tuple = (1,2,3,4,5)
print(my_tuple)

#Accessing Elements
first_element = my_tuple[0]
last_element = my_tuple[-1]

#Length of a Tuple
length = len(my_tuple)

#Concatenating Tuples
new_tuple = my_tuple + (6, 7, 8)

#Repeating Tuples
repeated_tuple = my_tuple * 2

#Checking if an Element is in a Tuple
is_present = 3 in my_tuple

# Tuple Packing
my_tuple = 1, 2, 3, 4, 5
print("Packed Tuple:", my_tuple)

# Tuple Unpacking
a, b, c, d, e = my_tuple
print("Unpacked Variables:", a, b, c, d, e)

