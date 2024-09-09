import argparse
import sys
import requests
import os

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


# Example usage: For downloading an image/video from web

def file(url, local_filename):
    try:
        print(f"Downloading file from URL: {url}")
        if local_filename is None:
            local_filename = url.split('/')[-1]
        print(f"Saving file as: {local_filename}")
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            if os.path.exists(local_filename):
                print(f"File {local_filename} already exists. Skipping download.")
                return local_filename
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        return local_filename
    except Exception as e:
        print(f"Error: {e}")
        sys.exit()

parser2 = argparse.ArgumentParser()
parser2.add_argument("url", help="Url of the file to download")
parser2.add_argument("-o", "--output", type=str, help="Name of the file", default=None)
args2 = parser2.parse_args()
print(args2.url)
print(args2.output, type(args2.output))
file(args2.url, args2.output)