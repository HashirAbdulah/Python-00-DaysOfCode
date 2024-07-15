# Geometric Mean
a = int(input("Enter First number for Geometric mean: "))
b = int(input("Enter First number for Geometric mean: "))

def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def  isGreater(a,b):
 if (a > b):
     print("First number",a, "is Greater")
 else:
     print("Second number",b, "is  Greater or Equal")
calculateGmean(a,b)
isGreater(a,b)

def average (*numbers):
   sum = 0
   for i in numbers:
      sum = sum+i
      return sum/len(numbers)

avg = average(7,9,8)
print(avg)