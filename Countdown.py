import time
from plyer import notification


title = "Hey there it's still Alan"
message = "End of the countdown, stay tuned for more..."


def countdown(ts):
    while ts:
        minis, secs = divmod(ts, 60)
        timer = '{:02d}:{:02d}'.format(minis, secs)
        print(timer, end="\r")
        time.sleep(1)
        ts -= 1
        print(f"Time left:{ts}")
    notification.notify(title=title, message=message,
                        app_icon=None, timeout=60, toast=False)


t = input("Enter the time in seconds: ")
countdown(int(t))
