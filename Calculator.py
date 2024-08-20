num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

# Commented Part is with basic knowledge while update is of making Calculations using FUNCTIONS


# {
# addition = num1 + num2
# print("Addition: ",addition)

# substraction = num1-num2
# print("Substraction: ",substraction)

# multiplication = num1*num2
# print("Multiplication:",multiplication)

# division = num1/num2
# print("Division:",division)

# floor_division = num1//num2
# print("Floor_division: ",floor_division)

# exponential = num1**num2
# print("Exponentail:" ,exponential)

# modulus = num1%num2
# print("Modulus: ",modulus)
# }


def addition(num1,num2):
    addition = num1 + num2
    return addition

def substraction(num1,num2):
    substraction = num1 - num2
    return substraction

def multiplication(num1,num2):
    multiplication = num1 * num2
    return multiplication

def division(num1,num2):
    if num2 == 0:
        print("Error: Division by zero is not possible.")
        return None
    division = num1 / num2
    return division

def modulus(num1,num2):
    modulus = num1 % num2
    return modulus

def exponential(num1 , num2):
    exponential = num1**num2
    return exponential


addition_result = addition(num1, num2)
print("Addition: ", addition_result)

subtraction_result = substraction(num1, num2)
print("Substraction: ", subtraction_result)

multiplication_result = multiplication(num1, num2)
print("Multiplication:", multiplication_result)

division_result = division(num1, num2)
print("Division:", division_result)

modulus_result = modulus(num1, num2)
print("Modulus: ", modulus_result)

exponential_result = exponential(num1, num2)
print("Exponential:", exponential_result)






