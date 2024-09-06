#Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class to inherit the properties and behaviors (attributes and methods) of an existing class. The class that is inherited from is called the parent class or base class (sometimes referred to as the superclass), and the class that inherits from it is called the child class or subclass.

class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def make_Sound(self):
        print( "This animal makes a Sound" )
    def showDetails(self):
        print(f"Name: {self.name}, Species: {self.species}, Model: {self.breed}")
        

class Dog(Animal):
    def __init__(self,breed,name,species):
        self.name = name
        self.species = species
        self.breed = breed
    def make_sound(self):
        print("Woof")
        
buddy = Dog("Buddy","Dog","Golden Retriever")
buddy.make_sound()
buddy.showDetails()

class Vechile:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year

    def start_engine(self):
        print( "Engine started" )

    def showDetails(self):
        print(f"Name: {self.brand}, Year: {self.year}, Model: {self.model}")
        


class Car(Vechile):
    def __init__(self,brand,year,model):
        self.brand = brand
        self.year = year
        self.model = model

    def start_engine(self):
        print("The car engine starts with a roar!")

car = Car("Toyota",2022,"Camry")
car.start_engine()
car.showDetails()