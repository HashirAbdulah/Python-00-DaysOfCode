# The walrus operator (:=) was introduced in Python 3.8 and is used for assignment expressions. It allows you to assign a value to a variable as part of an expression, which can be useful in scenarios where you want to use the value immediately and avoid redundant calculations.

# Example with while loop without using warlus operator
line = input("Enter a line (or 'quit' to stop): ")
while line != 'quit':
    print(f"You entered: {line}")
    line = input("Enter a line (or 'quit' to stop): ")

# Example with while loop using warlus operator
while (line := input("Enter a line (or 'quit' to stop): ")) != 'quit':
    print(f"You entered: {line}")
