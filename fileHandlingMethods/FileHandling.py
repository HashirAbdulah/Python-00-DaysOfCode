# Mode will be same as the task  if ur mode is "r" reading the file u will read the file only This will throw error if there will not a existing file.
#  if ur mode is "w" writing the file u will write the file only (This will remove the previous data 'overwrite the file') it creates the file if it doesnot exists. 
# if ur mode is "a" apppending the file u will append the file only (This will add the data with previous data) it creates the file if it doesnot exist. 
# if ur mode is "x" creating the file (This will add the data with previous data) it creates the file if it doesnot exist and return error if the file already exists.


# Reading a file:
f = open("file.txt","r") #Read mode is by Default
txt = f.read()
print(txt)
f.close()


# Writing a file
f = open("file.txt","w") # Write mode will remove the previous data 'overwrite the file' ("you cant read the file at the writing stage")
text = f.write("Hello World! Chnages to Naya Pakistan")
f.close()

f = open("file.txt","w") # Write mode will remove the previous data 'overwrite the file' ("you cant read the file at the writing stage")
text = f.write("Hello World! Chnages to Naya Pakistan")
f.close()


# Appending a file
f = open("file.txt","at")
try:
    text1 = f.write("\nThis is the new line added by the append operation.")
    print("Text appended successfully.")
    f.close()
except:
    print("Unable to append the text.")
    f.close()