import os

# Current Directory Check
current_directory = os.getcwd()
print("Current Directory:", current_directory)

# Check if 'Data' directory exists
if not os.path.exists("Data"):
    os.mkdir("Data")
    print("Directory 'Data' created successfully.")

else:
    os.rmdir("Data")
    print("Directory 'Data' deleted successfully.")
    
# Check again if 'Data' exists 
if os.path.exists("Data"):
    # Shows the List of Directories in the Data Directory
    folders = os.listdir("Data")
    print("Contents of 'Data' directory:", folders)
else:
    print("Directory 'Data' does not exist.")
