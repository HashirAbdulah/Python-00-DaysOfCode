#These all(Map,filter and Reduce) are Higher order functions

from functools import reduce
def cube(num):
    return num ** 3

print(cube(2))

# Using map() function :
# The map() function in Python is used to apply a specified function to each item of an iterable (like a list, tuple, etc.) and return a map object (an iterator) with the results. It's a useful function for transforming data, allowing you to process and modify each element of a collection.
list1 = [1,2,5,7,8]
        #AnyDesiredObject(DataType),(map(function, dataType/iterable))
list2 = list(map(lambda x: x**2,list1))
print(list2)

# Filter Function:
#The filter() function iterates through the elements of the iterable, applies the function to each element, and includes only those elements for which the function returns True. The result is an iterator, which can be converted to a list, tuple, or other data structures if needed.

        #AnyDesiredObject(DataType),(filter(function, dataType/iterable))
list3 = list(filter(lambda y: y % 2 == 0, list1))
print(list3)

# Reduce Function:
#It is imported from library using import function
list4 = reduce(lambda x,y: x + y, list1)
print(list4)
