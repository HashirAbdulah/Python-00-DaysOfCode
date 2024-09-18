import shutil

# Copy file from one to another with same thing
shutil.copy("ShutilModule.py","ShutilModule2.py")
print("File copied successfully!")

# Copy files with meta data too
shutil.copy2("ShutilModule.py","ShutilModule3.py")


# Move file from one path to other
shutil.move("C:/Users/M.Hashir Abdullah/Desktop/Python-100-DaysOfCode/ShutilModule.py","C:/Users/M.Hashir Abdullah/Desktop/Python-100-DaysOfCode/osModule/Shutil.py")

# Remove the whole folder containg the files.
shutil.rmtree("folderpath| foldername")
