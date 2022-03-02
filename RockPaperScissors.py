# the rock,scissors,paper game

import random

user_win = 0
computer_win = 0

options = ["rock", "paper", "scissors"]  # defining a list of words to be chosen later

while True:
    user_input = input("Type rock/paper/scissors or Q to quit: ").lower()
    if user_input == "q":
        print("You won " + str(user_win) + " times.")
        print("The computer won " + str(computer_win) + " times.")
        quit()
        break
    elif user_input not in options:
        continue
    number = random.randint(0, 2)  # choose of a random number between 0 and 2
    computer_pick = options[number]  # the number chosen before will represent one choice in the list of words
    print("The computer picked "+str(computer_pick))

    if user_input == "rock" and computer_pick == "scissors":
        print("you won")
        user_win += 1
    if user_input == "scissors" and computer_pick == "paper":
        print("you won")
        user_win += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("you won")
        user_win += 1
    elif user_input == computer_pick:
        print("Draw")
    else:
        print("you lost")
        computer_win += 1
