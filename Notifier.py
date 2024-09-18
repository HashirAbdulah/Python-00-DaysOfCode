import time
from plyer import notification

def notify():
    notification.notify(
        title = "Saab Pani Pee Lo",
        message = "Panni Pee ley Bhadway",
        app_icon = "C:/Users/M.Hashir Abdullah/Downloads/glass.ico",
        timeout = 10
    )

interval = 60 *60  #3600 sec

while True:
    notify()
    time.sleep(interval)  # interval for next notification
