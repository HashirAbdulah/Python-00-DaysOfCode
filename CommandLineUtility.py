import argparse
import sys

def cal(args):
    if args.o == 'add':
        return args.a + args.b
    elif args.o == 'subtract':
        return args.a - args.b
    elif args.o == 'multiply':
        return args.a * args.b
    elif args.o == 'divide':
        if args.b == 0:
            print("Error: Division by zero")
            sys.exit()
        return args.a / args.b
    else:
        print("Error: Invalid operation. Use 'add', 'subtract', 'multiply', or 'divide'")
        sys.exit()


parser = argparse.ArgumentParser() #This is the step for initializing your parser 
parser.add_argument('--a',type=float, default=1.0, help="Enter first number: ")  # Arguments adding
parser.add_argument('--b',type=float, default=1.0, help="Enter Second number: ") # Arguments adding
parser.add_argument('--o',type=str, default=1.0, help="Enter Operator: ") # Arguments adding   (Any Amounts of Arguments)

args = parser.parse_args()  # Arguments that are given to the functions are parsed using .parse_args() method
sys.stdout.write(str(cal(args)))  # This Funtions is used for console printing..