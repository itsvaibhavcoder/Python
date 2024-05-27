# Reverse the given aaray in python and print the output

myArray = [1,4,21,24,7,8]  # Output = [8,7,24,21,4,1]

a = 0 
b = len(myArray)-1 

while a<b:
    temp = myArray[a]
    myArray[a] = myArray[b]
    myArray[b] = temp
    a+= 1
    b-=1

print(myArray)
