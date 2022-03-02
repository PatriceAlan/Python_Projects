# Text-based adventure

name = input("Type your name : ")
print("Welcome", name, "to this adventure !!! ")
print("Let's start : ")
answer = input(
    "You are walking on a road and it has come to an end, you can go left or right..."
    " Which one do you choose ?? ").lower()
if answer == "left":
    answer = input("You are now in a maze you can go left or right choose one way:(left, right)    ").lower()
    if answer == "left":
        print("There's a serial killer and he killed you")
    elif answer == "right":
        answer = input("You are raised by a community as their new king: Do you accept: Yes or No ??   ").lower()
        if answer == "yes":
            print("You fought against the strongest of the village and you're dead...")
        elif answer == "No":
            print("Congratulations", name, "you are far but it's the end...")
        else:
            print("Invalid option : It was a trap you lose ")
    else:
        print("Invalid option : It was a trap you lose ")
elif answer == "right":
    answer = input("You come across a river, choose:(swim or jump)  ").lower()
    if answer == "swim":
        print("Ops ! there are alligators there so they ate you")
    elif answer == "jump":
        print("You got small so you didn't jump well... You're dead")
    else:
        print("Invalid option : It was a trap you lose ")
else:
    print("Invalid option : It was a trap you lose ")
