# The seek() function allows you to move the current position within a file to a specific point. The position is specified in bytes, and you can move either forward or backward from the current position. For example:

with open("fileHandlingMethods\sfile.txt", 'r') as f:
  # Move to the 10th byte in the file
  f.seek(12)

  print(f"Point where file is seeked:{f.tell()}")
  
  data = f.read(7)
  print("Data is Read at: ",data)
  

# Truncate Method is used for specifing Size of the file

#   with open('sample.txt', 'w') as f:
#     f.write('Hello World!')
#     f.truncate(5)

# with open('sample.txt', 'r') as f:
#   print(f.read())