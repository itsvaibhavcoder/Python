def binarySearch(myArray, target):
    start = 0
    end = len(myArray)-1

    while start<end:
        mid = start+end//2
        if myArray[mid]==target:
            return mid
        elif myArray[mid]>target:
            end-=1
        else:
            start+=1
    
    return -1 # If element is not found
 
myArray = [1,2,4,6,21,45,67]
target = 40

result = binarySearch(myArray, target)
print(result)
