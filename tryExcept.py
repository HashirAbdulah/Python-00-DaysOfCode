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

def addition ():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 + num2
        print("Addition:", result)
        return result
     
    except ValueError:
        print("Error: Invalid input. Please enter numbers.")
        return None
    finally:
        print("Addition operation completed.")

addition()
