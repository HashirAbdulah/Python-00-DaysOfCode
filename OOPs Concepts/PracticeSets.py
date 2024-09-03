# Basic Getter and Setter
class Circle:
    def __init__(self,radius):
        self._radius = radius

    def show(self):
        print(f"Radius: {self._radius}")
        print(f"Area of Cirlce: {3.14 * self._radius ** 2}")   

    @property
    def radius(self):
       return self._radius
    
    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = radius

a = Circle(5)
a.show()

# Area of Rectangle
class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def show(self):
        print(f"width: {self._width} height: {self._length}")
        print(f"Area of Rectangle: {self._width * self._length}")

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("Width cannot be negative")
        self._width = value

    @length.setter
    def length(self, value):
        if value < 0:
            raise ValueError("length cannot be negative")
        self._lengthe = value

    @property
    def area(self):
        return self._width * self._height
    

rect = Rectangle(10,5)
rect.show()


# Read-Only Property
class Employee:
    def __init__(self,firstname,lastname,idnumber):
        self._firstname = firstname
        self._lastname = lastname
        self._idnumber = idnumber

    def show(self):
        print(f"Firstname: {self.firstname} Lastname: {self.lastname} ID Number: {self._idnumber}")
        print(f"Fullname: {self.fullname}")

    @property
    def firstname(self):
        return self._firstname

    @property
    def lastname(self):
        return self._lastname
    
    @firstname.setter
    def firstname(self,updatedName):
        self._firstname = updatedName

    @lastname.setter
    def lastname(self,updatedName):
        self._lastname = updatedName
    
    @property
    def fullname(self):
        return f"{self._firstname} {self._lastname}"
    
e = Employee("Hashir","Abdullah","A1055")
e.show()

# Bank Account
class BankAccount:
    def __init__(self,balance):
        self._balance = balance

    def show(self):
        print(f"Balance: {self._balance}")

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self._balance += amount

bank = BankAccount(5000)
bank.show()
bank.balance = 5550
bank.show()
bank.balance = -29
bank.show()