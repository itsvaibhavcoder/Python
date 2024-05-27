# String in python
#String are immutable in python
# Single line string 
str = "hello, Vaibhav!"
print(str)

# Multiline string 
multiLine_string =  '''This is a
multiline
string.'''
print(multiLine_string)

# String Concatenation
str1 = "Hello"
str2 = "Python"
print(str1+ ", "+str2)


#String Repetition
str3 = "python"*3
print(str3)

#Accessing character
# Index start from 0 in string
print(str3[0])


#String slicing
my_string = "Python"
substr = my_string[1:4]  #1 -- inclusive , 4 -- Exclusive
print(substr)

#String length
print(len(my_string))

#String Methods
# upper(), lower(), replace(), find(), split(), capatilize()


index = my_string.find('t')
print(index)
my_string = "Hello,World,Python"

# Split the string using a comma as the delimiter
result = my_string.split(',')
print(result)

#Output: ['Hello', 'World', 'Python']

replaced_str = my_string.replace("World", "Python")
print(replaced_str)

#String Formatting 
name = "Alice"
age = 25
formatted_str = f"My name is {name} and I'm {age} years old."

print(formatted_str)