import os

if os.path.exists("Data"):
    os.rmdir("Data")
    print("Directory 'Data' deleted successfully.")
else:
    print("Directory 'Data' does not exist.")

# Shows the List of Directories in the Data Directory
folders = os.listdir("Data")
print(folders)
