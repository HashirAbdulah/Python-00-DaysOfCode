a = int(input("Enter a Number for Even/Odd: "))
print(a,"is Even") if a % 2 == 0 else print(a,"is Odd") if a % 2 != 0 else ""

age = int(input("Enter Voter Age: "))
print(age,"Year age is Eligible for Vote") if age >= 18 else print(age,"Year age is Not Eligible")


num1 = int(input("Enter first Number: "))
num2 = int(input("Enter second Number: "))
print(num1,"is Maximum") if num1 > num2 else print(num1, "is equal to", num2) if num1 == num2 else print(num2,"is Maximum")

b = int(input("Enter a Number: "))
print(b,"is Postive" if b >= 0 else "is Negative")

char = input("Enter a Character: ")
print(char,"is Vowel" if char in "aeiouAEIOU" else "Consonant")