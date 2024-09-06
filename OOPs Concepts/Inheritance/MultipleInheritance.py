# Class Inherting from different Parent classes is Multiple Inheritance
# If the Parameters of the class is Passed for inheritance the override methods always run for the given first parameter of the inherited class.(For checking the methods calls option use .mro() method = Method Resolution Order).
# Syntax = class Name(Parent-Class1, Parent-Class2):

class Employee:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"Name of Employee: {self.name}")
        

class Member:
    def __init__(self, Designation):
        self.Designation = Designation

    def show(self):
        print(f"The Designation of Employee in Commettie is : {self.Designation}")

class MemberCommitee(Member,Employee):
    def __init__(self, name, Designation):
        self.name = name
        self.Designation = Designation



emp = MemberCommitee("Hashir", "Employee")
print(emp.name)
print(emp.Designation)
emp.show()
# print(MemberCommitee.mro())
