''' In python all the part of python class in python there are integer, string and boolean type of datatype 
integer : it holds the  value positive, negative and zero , not contain any decimal values
float : it holds the values contain decimal points
string : It contain the stream of character denoted by "" or ''

boolean : True or False 

type casting in python : the process of converting one type of datatype into another datatype is calles type casting.
Two Types : implicit and explicit
'''

number = 10 # type is int 
print(type(number))
number_float = 10.0
print(type(number_float)) # type is float

number = True
print(type(number)) # type is boolean

# Type casting

number1 = 10
str1 = '20'
# res = str1 + number1 -- not possible
res = str1 + str(number1) # Explicit type casting
print(res)


