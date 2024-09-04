# Method that belongs to class rather than an instance/object of the class is Static Method.
# @staticmethod 

class Math:
    def __init__(self,num):
        self.num = num
    
    def add(self,n):
        self.num = self.num + n
        
    @staticmethod
    def add2(a,b):
        return a+b
    
m = Math(5)
m.add(6)
print(m.num)
print(Math.add2(3, 4)) # Static Method Call