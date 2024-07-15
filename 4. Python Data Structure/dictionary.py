'''
Dictionary : A disctionary of key value pairs
The values can be changed (mutable)
Mixed datatypes
'''

mycar = {
    "brand" : "Range Rover Sports",
    "model" : "HSE",
    "year" : 2017
}

# print(mycar)

# Using constructor

mygreens = dict(fruit ="green apples", vegetable = "kale")
# print(mygreens)

# print(type(mygreens))
# print(len(mygreens))
mycar["year"] = 2019

# dictionary methods
# print(mycar.get("year"))

mycar.update({"color":"silver"})
# print(mycar)

# b = mycar.keys()
# print(b)
# print(type(b))

# mycar.pop("color")
# print(mycar)
# print(mycar)

# mycar.clear()
# print(mycar)

del mycar
print(mycar) #Deleted from memory





