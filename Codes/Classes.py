# Creating class in python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def Bark(self):
        print(f"The {self.name} is barking !")


#Creating object of classes

dog = Dog("Sheru", 12)

print(f"The {dog.name} is {dog.age} old !")

#Calling method of class on object

dog.Bark()
