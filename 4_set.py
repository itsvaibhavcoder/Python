#Set -- Unique elemenent only, Mutable

#Creating set 
#Empty set
my_set = set()
print(my_set)
my_set = {1,2,3,4,5}
print(my_set)

#Accessing elements
#Do not support indexing or slicing
is_present = 3 in my_set
print(is_present)

#Adding or removing element
my_set.add(6)
print(my_set)

my_set.update({7, 8, 9})
print(my_set)
# remove raises error if element is not present while discards does not
my_set.remove(3) 
print(my_set)
my_set.discard(4)
print(my_set)
# remove arbitary element from set
popped_element = my_set.pop()
print(my_set)

#Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1.union(set2) # {1, 2, 3, 4, 5, 6}
intersection_set = set1.intersection(set2) # {3, 4}
difference_set = set1.difference(set2) # {1, 2}
symmetric_difference_set = set1.symmetric_difference(set2)  # {1, 2, 5, 6}

#Clearing set 
my_set.clear()
print(my_set)