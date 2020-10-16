# Class definitions

class MyClass:
    def __init__(self, name, age): # Constructor
        self.name = name
        self.age = age

instance1 = MyClass('Chris', 39)
instance2 = MyClass('Steve', 20)

class MyClassWithMethod:

    species = 'Human' # Class attribute
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def printNameAndAge(self):
        print("Name is: " + self.name, "\nAge is: " + self.age + ", " + self.species)
    
    def __str__(self):
        return "Name is: " + self.name, "\nAge is: " + self.age + ", " + self.species


instance3 = MyClassWithMethod('Chris', '39')
instance4 = MyClassWithMethod('Steve', '20')

print(instance3.printNameAndAge())

# Inheritance

class NewClass(MyClass):
    pass

n1 = NewClass('Billy', 50)

print(n1.name, n1.age)