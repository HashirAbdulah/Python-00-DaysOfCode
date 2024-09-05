# A class method belongs to the class rather than to an instance of the class. One common use case for class methods as alternative constructors is when you want to create an object from data that is stored in a different format, such as a string or a dictionary.

class Person:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def showDetails(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

    @classmethod
    def from_string(cls, string):
        name, age, grade = string.split(',')
        return cls(name, int(age), grade)
    

person = Person.from_string("John Doe, 30, A+")
person.showDetails()