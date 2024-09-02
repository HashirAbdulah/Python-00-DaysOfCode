import random
computer = random.randint(1, 3)
print("Use 1 for Snake, 2 for Water & 3 for Gun")
choice = int(input("Enter a Choice between \n 1.Snake \n 2.Water \n 3.Gun \n"))
if choice == computer:
    print("It's a tie!")
elif choice == 1 and computer == 2:
    print("You Win (Choosed: Snake)! Snake drinks water.")
elif choice == 2 and computer == 3:
    print("You Win (Choosed: Water)! Water rusts gun.")
elif choice == 3 and computer == 1:
    print("You Win (Choosed: Gun)! Gun shoots snake.")
elif choice == 1 and computer == 3:
    print("You Lose! Gun shoots snake.")
elif choice == 2 and computer == 1:
    print("You Lose! Snake drinks water.")
elif choice == 3 and computer == 2:
    print("You Lose! Water rusts gun.")
else:
    print("Invalid input! Please enter 1, 2, or 3.")

