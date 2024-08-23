try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
    list1 = [1,4,6,8,9]
    print(list1[7])
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a number.")
except IndexError:
    print("Error: Index out of range.")
else:
    print("Operation successful.")
finally:
    print("Execution completed.")
