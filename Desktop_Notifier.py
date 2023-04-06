from plyer import notification

print("Enter the title of the message : ")
title = input("-> ")

print("Enter the message : ")
message = input("-> ")

# title = "THE TITLE"
# message = "A PROGRAM TO SEND NOTIFICATIONS"

if __name__ == "__main__":
    notification.notify(title=title, message=message, app_icon='', timeout=60, toast=False)
