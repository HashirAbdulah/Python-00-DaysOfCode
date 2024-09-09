# Combination of two or more types of Inheritance


class Human:
    def __init__(self, name, age ):
        self.name = name
        self.age = age

    def eat(self):
        return "Human Eats"

    def walk(self):
        return "Human Walks"


class Employee(Human):
    def __init__(self, name, age,id,department):
        super().__init__(name, age)
        self.id = id
        self.department = department

    def work(self):
        return "Employee Works"


class Student(Human,Employee):
    def __init__(self, name, age, id,department,subjects,institute):
        Employee.__init__(name, age, id, department)
        self.subjects = subjects
        self.institute = institute


class Child(Student, Employee, Human):
    def __init__(self, name, age, id, department, subjects, institute, fatherName, cast):
        Human.__init__(self, name, age)
        Employee.__init__(self, name, age, id, department)
        Student.__init__(self, name, age, id, department, subjects, institute)
        self.fatherName = fatherName
        self.cast = cast
        print("I am an example of Hybrid Inheritance")

child = Child("Hashir", 21, "A218c", "CS", "Math", "UOL", "Abdul Majeed", "Paolii")
print(Child.mro())
