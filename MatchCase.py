x = int(input("Enter the value of x: "))
match x:
    case 0 :
        print("X is zero")
    case 1:
        print("x is equal to 1")
    case 2 | 3:
        print("x is either 2 or 3")
    case x if 4 <= x <= 6:
        print("x is between 4 and 6")
    case 7:
        print("x is equal to 7")
    case _:
        print("x is not a valid choice")