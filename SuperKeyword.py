# The super keyword in Python is used to refer to the parent class (or base class) from within a child class (or subclass). It allows the child class to access methods and attributes of the parent class.

# Syntax:   super().__init__()
 #          super().methodName(with params) 


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade = grade

def getInput():
     name = input( "Enter your name: ")
     age = int(input( "Enter your age: "))
     grade = input( "Enter your grade: ")
     return name, age, grade

name, age, grade = getInput()
st1 = Student(name, age, grade)
print("Name:",st1.name)
print("Age:",st1.age)
print("Grade:",st1.grade)


class Shape:
    def area(self):
        return 0

class Rectagle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    
rect = Rectagle(5,6)
print(f"Area: {rect.area()}")
