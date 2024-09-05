# Operator Overloading means giving extended meaning beyond their predefined operational meaning. For example operator + is used to add two integers as well as join two strings and merge two lists. It is achievable because ‘+’ operator is overloaded by int class and str class. You might have noticed that the same built-in operator or function shows different behavior for objects of different classes, this is called Operator Overloading. 

# Operator overloading is used for operations on the objects/instances of the class
class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
    
    def __str__(self):
        return f"({self.i}i + {self.j}j + {self.k}k)"
    
    def __add__(self, x):
        return Vector(self.i + x.i, self.j + x.j, self.k + x.k)
    

v1 = Vector(1,5,8)
v2 = Vector(2,3,4)

print(v1)
print(v2)

print(v1 + v2)

