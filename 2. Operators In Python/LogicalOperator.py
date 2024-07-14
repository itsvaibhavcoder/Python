''' Logical operators are used to combine the different conditional statement
Example : and, or and not 
and : Execute only when all conditions are True
or : Execute on;y when one of the condition is True
not : convert true to false, false to true
'''
number = 7
print(number>5 and number <8) #True
print(number>=5 and number<=8) #True

print(number<5 or number<8) # True
print(number<=5 or number<=8) # True

print(not(number<5 or number<8)) # number <5 or number < 8 --> True !(True) ==> False
