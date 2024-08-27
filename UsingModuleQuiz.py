import time

t = time.strftime("%H:%M:%S")
print("Time is:",t)
hour = int(time.strftime("%H"))

if (hour>=0 and hour<=12):
    print("Good Morning Sir!",hour)
elif(hour>=13 and hour<=19):
    print("Good AfterNoon Sir!",hour)
elif(hour>=19 and t<=24):
    print("Good Night Sir!",hour)