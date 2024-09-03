# Getter and Setters are used for access modification of class attributes.
# Moreover performing the Encapsulation of the data Items.

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name
    
    def get_age(self):
        return self._age
    
    def set_age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self._age = age

person  = Person("Gasgur",20)

print(person.get_name())
person.set_name("John")
print(person.get_name())
print(person.get_age())
person.set_age(30)
print(person.get_age())
# person.set_age(-10)  # This will raise an error.
# print(person.get_age())
print(person.__dict__) 
    