# Method overriding is an ability of any object-oriented programming language that allows a subclass or child class to provide a specific implementation of a method that is already provided by one of its super-classes or parent classes. When a method in a subclass has the same name, the same parameters or signature, and same return type(or sub-type) as a method in its super-class, then the method in the subclass is said to override the method in the super-class.

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y
    



class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"{3.14 * self.radius * self.radius:.2f}"
    

class Radius(Shape):
    def __init__(self, height,base):
        self.height = height
        self.base = base

    def area(self):
        return f"{0.5 * self.height * self.base:.2f}"
    
rec = Shape(5,6)
print(rec.area())

cir = Circle(3)
print(cir.area())

rad = Radius(6,9)
print(rad.area())
