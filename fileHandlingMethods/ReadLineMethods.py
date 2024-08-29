import os

x = os.getcwd()
print(x)

try:
    f = open("fileHandlingMethods\myfile.txt","r")
    while True:
        line = f.readline()
        if not line:
            break
        print(line)
except:
   print("File not found.")



try:
   #uses "with" keyword with Write file for excluding fileclose method
   with open("fileHandlingMethods\myfile2.txt","w") as g:
    lines = ["This is the 1st Line\nThis is the 2nd Line\nThis is the 3rd Line\nThis is the 4th Line\nThese Lines are added through file Handling"]
    g.writelines(lines)
    # g.close()
    
except:
   print("File not found.")

    