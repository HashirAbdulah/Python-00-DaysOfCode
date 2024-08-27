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
#  Adding Method
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car["color"] = "red"

print(car)

info.update(info2)
print(info) 
print(info.pop("Name"))
print(info.popitem())
# print(info.clear())        returns empty dictionary
# del info                   delete the whole dicionary
# del info["Occupation"]     delete the specific key value pairs