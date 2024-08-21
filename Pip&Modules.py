# This Is the pip and modules concept
# Example:

# import pandas
# Module for getting current directory
import os
directory_path = '.'  # Current directory

try:
    # List all files and directories in the specified path
    contents = os.listdir(directory_path)
    
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"You do not have permission to access '{directory_path}'.")
except Exception as e:
    print(f"An error occurred: {e}")


    # os module in Python provides functions for interacting with the operating system.

# This link shows the modules provided by Pyhton
# https://docs.python.org/3/py-modindex.html