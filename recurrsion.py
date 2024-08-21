n = int(input("Enter number for factorial :"))
def factorial (n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)

print("Factorial of",n, "is",factorial(n))



number  = int(input("Enter a Number for fibonacci sequence:"))
def fibonacciSequence (number):
        if number < 0 :
            print("Incorrect input,Input Number Greater than 0")
        elif (number == 0):
            return 0
        elif(number == 1):
                return 1
        else:
            return fibonacciSequence(number-1) + fibonacciSequence(number-2)
        
print("Fibonacci sequence upto",number, "is", fibonacciSequence(number))