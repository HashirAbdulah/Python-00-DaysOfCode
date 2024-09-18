# MultiThreading is the concept of parallel execution of the tasks
# E.g: Square function for the different args get the time according to the execution but by using threading these functions can be executed at the same time..

import threading as t
import time
from concurrent.futures import ThreadPoolExecutor
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
