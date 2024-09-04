class Student:
    schoolName = "ABC School" # Class Variable
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    def showDetails(self):
        print(f"Name: {self.name}, age: {self.age}, grade: {self.grade},SchoolName: {self.schoolName}")
    
st = Student("Harry",22,"A+")
st.schoolName = "University of Lahore" # Instance variable
st.showDetails()

st2 = Student("Abdu",19,"B+")
# st2 schoolname will be from class Variable
st2.showDetails()