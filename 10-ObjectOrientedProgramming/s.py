class MyClass:
    x = 1 


use = MyClass()

print(use.x)

#class 
#object
#method - function wich belong to the object

#The self parameter is a reference to the current instance of the class, 
# and is used to access variables that belong to the class.

#It does not have to be named self , you can call it whatever you like, 
# but it has to be the first parameter of any function in the class:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name},{self.age}"

    
    def Myfunction(self) :  
        print("Hi my name is " + self.name)





p1 = Person("John", 23)


print(p1.name)
print(p1.age)

print(p1)
p1.Myfunction()



        

