# MultiThreading is the concept of parallel execution of the tasks..Multithreading is suitable for I/O-bound tasks, like downloading files, reading from disk, or network requests.
# E.g: Square function for the different args get the time according to the execution but by using threading these functions can be executed at the same time..

import threading as t
import time
from concurrent.futures import ThreadPoolExecutor
import multiprocessing
import requests
import os
import shutil

def Square(n):
    time.sleep(n)
    print(f"Square of {n} is {n*n}")

t4 = t.Thread(target=Square,args=[12])
t1 = t.Thread(target=Square,args=[5])
t2 = t.Thread(target=Square,args=[3])
t3 = t.Thread(target=Square,args=[8])

t4.start()
t1.start()
t2.start()
t3.start()

# Joining the threads ensures that the main thread waits for the other threads to finish before it continues
t1.join()
t2.join()
t3.join()
t4.join()

print("All threads are completed")


# Using ThreadPoolExecutor for concurrent execution

def square(n):
    time.sleep(n)
    print(f"Square of {n} is {n*n}")

with ThreadPoolExecutor() as executor:
    l = [4, 2, 7, 9]
    executor.map(square, l)

print("All threads are completed")


# Example for downloading file:

def download_file(url,name):
    print(f"Download Started {name}")
    response = requests.get(url)
    open(f"files/file{name}.jpg", "wb").write(response.content)
    print(f"Finished Downloading {name}")

url = "https://picsum.photos/2000/3000"


if __name__ == '__main__':
    if os.path.exists("files"):
        shutil.rmtree("files")
    else:
        os.makedirs("files")
        pros = []
        for i in range(20):
            p = t.Thread(target=download_file,args=(url,i))
            p.start()
            pros.append(p)
        for p in pros:
            p.join()
print("All Files Downloaded")
