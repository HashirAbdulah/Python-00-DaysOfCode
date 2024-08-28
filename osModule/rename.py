import os 
# This will rename the Directory
for i in range(1,101):
    os.rename(f"Data/Tutorial{i}",f"Data/Tutorial {i}")