#Access Modifiers are used to limit the access of class variables and methods outside the class.
#Types of access specifiers:
    # 1.Public access modifier: Declared public are easily accessible from any part of the program
    # 2.Private access modifier: Declared private are accessible within the class only, private access modifier is the most secure access modifier
    # 3.Protected access modifier: Declared protected are only accessible to a class derived from it 

class Employee:
    # Public Access Modifier
    def __init__(self,name,age):
        self.name = name
        self.age = age

e = Employee("Harry",20)
print(e.name)
print(e.age)


class Student:
    # Private Access Modifier
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

s = Student("Nass",20)
# print(s.name) This cannot be directly output the values because the variables are private
# print(s.age)  This cannot be directly output the values because the variables are private
# For Acessing the variables we use Indirect Method:
#   Syntax :(objectInstace._ClassName__Variable)
print(s._Student__name)
print(s._Student__age)


class Vechile:
    # Protected Access Modifier
    def __init__(self,color,engine):
        self._color = color
        self._engine = engine

v = Vechile("Red","250g")
print(v._color)
print(v._engine)