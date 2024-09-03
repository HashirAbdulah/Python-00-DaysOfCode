# Special method in class used to create and Initialize a object of a class. Invoked Automatically when object is called.

# def __init__(self,other arguments) -----> initialize

# No return other than None.
# Always necessary |self| keyword when a function is made inside the class.
class Person:
    def __init__(self,name,occupation,age): #Constructor initialization
        self.name = name
        self.occupation = occupation
        self.age = age

    def info(self):
        print(f"Name:{self.name}, Occupation:{self.occupation}, Age:{self.age}")
        
# Now create as much as needed objects of the class py passing same amount of parameters
a = Person("Harry","Developer",23)
b = Person("Ali","HR",20)

a.info()
b.info()