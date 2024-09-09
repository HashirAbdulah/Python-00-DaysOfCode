# The time module in Python provides a set of functions to work with time-related operations, such as timekeeping, formatting, and time conversions. 
import time


t = time.localtime()
# localtime returns the current local time in a tuple format
# strftime is used for formating the local and updated time 
current_time = time.strftime("%d,%m,%Y %H:%M:%S", t)
print(current_time)


# The time.sleep() function suspends the execution of the current thread for a specified number of seconds. This function can be used to pause the program for a certain period of time, allowing other parts of the program to run, or to synchronize the execution of multiple threads.

# time.time() shows the epoch time in floats from when the time module is initiated.

print("Start:", time.time())
time.sleep(2)
print("End:", time.time())