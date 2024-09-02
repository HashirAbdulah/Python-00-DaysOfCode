# Difference between "is" and "==" operator
# They work in differenct cases for mutable and immutable objects 
# Like for same String, a int or float value and tuple remain same but when its about list,dict or any iterative object its use case become different.

#  Both are comparison operators

# `==` checks for equality of values.
# `is` checks for identity of objects. / test if two variables refer to the same object.

c = 4
d = 4
print(c == d)  # Outputs: True
print(c is d)  # Outputs: True

# For mutable objects like list, dict, set, etc., `is` checks if two variables refer to the same object, not if their values are equal.

x = ["apple", "banana", "cherry"]

y = x
print(x)
print(y)
print(x is y) # True Exact location of object in memory
print(x == y) # True

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True bcz values are same
print(a is b) # False different memory location


