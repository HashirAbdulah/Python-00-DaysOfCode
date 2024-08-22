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
