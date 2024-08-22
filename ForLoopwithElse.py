for i in range(5):
    print(i)

else:
    print("In Else Statment")

for k in []:
    print(k)

else:
    print("In Else Statment due to because loop does not work")


# For loop with else if there is a break keyword for the correct loop it wouldnt execute the else statement

for i in range(3):
    if i == 2:
        break
    print(i)
else:
    print("In Else Statment")  ,"""This wouldn't run because the loop condition is statisfying, But if the range is equal to the condition else block will execute"""

