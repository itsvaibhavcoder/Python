#List are muttable in python 
#Creating List
my_list = [1,2,3,4,5]
print(my_list)

#Accessing Element
print(my_list[0]) # First element 
print(my_list[-1]) # last element

#List Slicing
sub_list = my_list[1:4]
print(sub_list)
print(my_list)

#Modifying Lists
my_list[2] = 10
print(my_list)

#Adding element
my_list.append(6) # Append element to last
my_list.insert(2,7) # insert elemet to specific index
print(my_list)

#Removing element
my_list = [1,2,3,4,5]
my_list.remove(3) # Removes first occurence of 3
my_list.pop(1) # remove element from specified index default is last element
print(my_list)

#list opearations
new_list = my_list+[8,9,10]
print(new_list)

#length of list
print(len(new_list))

#Checking element in a list
is_present = 7 in my_list
print(is_present)