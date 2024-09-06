# When we have a child and grandchild relationship in Inheritance.
class GrandFather:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def show_details(self):
        print(f"Name: {self.name}, Species: {self.species}")
        
class Father(GrandFather):
    def __init__(self, name, cast):
        GrandFather.__init__(self, name, species="Human")
        self.cast = cast
        
    def show_details(self):
        GrandFather.show_details(self)
        print(f"Cast: {self.cast}")
        
class Child(Father):
    def __init__(self, name, color):
        Father.__init__(self, name, cast="Paolee")
        self.color = color
        
    def show_details(self):
        Father.show_details(self)
        print(f"Color: {self.color}")

dog = Child("GigaNigga", "ExtraNigga")
dog.show_details()