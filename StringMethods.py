# Upper and lowerCase
s = "Hello, Python!"
print(s.upper())  # Output: HELLO, PYTHON!
print(s.lower())  # Output: hello, python!


# Capitalize first letter of each word
s = "hello, world!"
print(s.capitalize())  # Output: Hello, world!

#
s = "   hello, world!   "
print(s.strip())    # Output: "hello, world!"
print(s.lstrip())   # Output: "hello, world!   "
print(s.rstrip())   # Output: "   hello, world!"


# Replace a substring
s = "Hello, world!"
print(s.replace("world", "Python"))  # Output: Hello, Python!


# Formats the string using placeholders {} for variable substitution.
name = "Alice"
age = 30
print("Name: {}, Age: {}".format(name, age))   # Output: Name: Alice, Age: 30


# Checks if all characters in the string are digits.
s = "12345"
print(s.isdigit())  # Output: True


# Join
words = ["Hello", "World", "!"]
print(" ".join(words))   # Output: Hello World !

# Start and Ends With
s = "Hello, World!"
print(s.startswith("Hello"))   # Output: True
print(s.endswith("!"))         # Output: True

