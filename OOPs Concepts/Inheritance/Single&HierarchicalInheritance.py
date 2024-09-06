# A child class inherits from only one Parent Class is Single Inheritance.
# Different Child classes inherits from one Parent Class is Hierarchical Inheritance.

# This example shows the Hierarchical And Single Inheritance..
# In this example, Dog and Cat classes inherit from Animal class.
class Animal:
    def __init__(self, name):
        self.name = name

    def makeSound(self):
        print(f"{self.name} makes Sound")
    def eat(self):
        return (f"{self.name} eats")

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
    def makeSound(self):
        return (f"{self.name} barks")
    
    

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def makeSound(self):
        return (f"{self.name} MEOW")



dog = Dog("Buddy")
print(dog.makeSound())
print(dog.eat())
cat = Cat("Phuss")
print(cat.makeSound())
print(cat.eat())

