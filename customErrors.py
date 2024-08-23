a = (input("Enter a number between 5 and 10: "))

if a == 'quit':
    raise SystemExit("Program terminated by user")

if not a.isnumeric():
    raise TypeError("Value should be a number")


a = int(a)
if a < 5 or a > 10:
    raise ValueError("Value should be between 5 and 10")


print("You entered:", a)


