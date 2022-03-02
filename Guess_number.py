# Number guessing quiz
import random

print("A number has been chosen randomly by the cpu, you are there to find it:")
number = random.randint(1, 1000)
guess = 0
user = int(input("Type a number between 0 and 1000: "))
while user != number:
    if user < number:
        print("It's bigger")
        user = int(input("Type a number between 0 and 1000: "))
        guess += 1
    elif user > number:
        print("It's lower")
        user = int(input("Type a number between 0 and 1000: "))
        guess += 1
    else:
        print("Correct you did it well...")
        break
print("You tried: " + str(guess) + "times")
# pr
