# CLASS is a bluePrint for Object. Containing variables, methods, attribute and other properties.
# OBJECT is a instance of the Class.
# Self keyword is a reference to the current instance of the class,used to access variables that belongs to the Class. (Object for which method is called). Always necessary for the function that is made in class.

class Person:
    name = "Hashir"
    age = 20
    Occupation = "Student"
    country = "Pakistan"
    
    def greet(self):
        print(f"Hello {self.name}, Good Morning")
    
    def showDetails(self):
        print(f"Name:{self.name}, Age:{self.age}, Occupation:{self.Occupation}, Country:{self.country}")
        

a = Person()
b = Person()
a.showDetails()
b.name = "Faisal Sarfraz"
b.Occupation = "CEO"
b.country = "United Arab Emirates"
b.showDetails()
a.greet()
b.greet()