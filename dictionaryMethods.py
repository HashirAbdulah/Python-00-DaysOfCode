info = {
    "Name": "John Doe",
    "Age": 30,
    "Country": "USA",
    "City": "New York",
    "Occupation": "Engineer"
}

info2 = {
    "Education": "BSCS",
    "Skills": ["Python", "JavaScript", "C++"],
}

info.update(info2)
print(info) 
print(info.pop("Name"))
print(info.popitem())
# print(info.clear())        returns empty dictionary
# del info                   delete the whole dicionary
# del info["Occupation"]     delete the specific key value pairs

#  Adding Methods in Dictionary
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# Adding Method 1
car["color"] = "red"
print(car)
car.clear() # Clear the list
print(car) # Prints the Empty Dictionary



x = {'type' : 'fruit', 'name' : 'apple'}
# Adding Method 2
x.update({'color' : 'green'})
print(x)
# ========================================

