# roll the dice
import random


def rolldice(min1, max1):
    return random.randint(min1, max1)


chc = input("Do you want to roll your dices?? yes or no:  ").lower()
ply = 0
cpu = 0
play = 0
while True:   # beginning of the simulation of the do...while loop
    if chc == "yes":
        ply1 = rolldice(1, 6)
        ply2 = rolldice(1, 6)
        print("You got: " + str(ply1) + " and " + str(ply2), "the sum is: " + str(ply1 + ply2))
        cpu1 = rolldice(1, 6)
        cpu2 = rolldice(1, 6)
        print("The computer got: " + str(cpu1) + " and " + str(cpu2), "the sum is: " + str(cpu1 + cpu2))
        if ply1 + ply2 < cpu1 + cpu2:
            print("You lose, the computer won")
            cpu += 1
        elif ply1 + ply2 > cpu1 + cpu2:
            print("You won, the computer lose")
            ply += 1
        else:
            print("Draw")
    answer = input("Do you want to play again yes/no ?:  ").lower()
    if answer == "no":
        break  # end of the do...while loop
    while answer != "yes" and answer != "no":
        answer = input("Do you want to play again yes/no ?:  ").lower()


print("You won " + str(ply) + " times.")
print("The computer won " + str(cpu) + " times.")
