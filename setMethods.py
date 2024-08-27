set1 = {1,2,3,4,6}
set2 = {1,7,8,5,6}

# set Add Method:
set1 = {1,2,3,4,6}
set1.add(7)
print(set1)

print(set1.union(set2))
print(set1.intersection(set2))
set1.update(set2)
print(set1)


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
#  isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.
print(cities.isdisjoint(cities2))

# issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))


# issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.
print(cities2.issubset(cities))

# Check more of the sets methods in the repel:
# https://replit.com/@codewithharry/32-Day32-Set-Methods