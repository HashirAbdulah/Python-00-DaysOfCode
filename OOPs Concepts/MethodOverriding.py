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
