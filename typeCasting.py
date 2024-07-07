## Typecasting (or type conversion) refers to the process of converting a variable from one data type to another. 
## This is useful when you want to perform operations that require a different type of data than the one you currently have.
x = 5
y = float(x)
print(y)  # Output: 5.0


x = 3.7
y = int(x)
print(y)  # Output: 3

x = "123"
y = int(x)
print(y)  # Output: 123

x = 456
y = str(x)
print(y)  # Output: "456"

x = "3.14"
y = float(x)
print(y)  # Output: 3.14

x = [1, 2, 3]
y = tuple(x)
print(y)  # Output: (1, 2, 3)

x = (4, 5, 6)
y = list(x)
print(y)  # Output: [4, 5, 6]
