# quiz game
print("Hello, welcome to this quiz game !")
score = 0
play = input("Do you want to play ?? Answer by yes or no: ")
if play.lower() != "yes":
    print("End before even starting")
    quit()
elif play.lower() == "yes":
    print("Let's go :) ")

answer = input("What does CPU stand for?: ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Correct answer: central processing unit")

answer = input("In which year has python been created?: ")
if answer == "1995":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Correct answer: 1991")

answer = input("What does GPU stand for?: ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Correct answer: graphic processing unit")

answer = input("What does RAM stand for?: ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Correct answer: random access memory")

answer = input("What does ROM stand for?: ")
if answer.lower() == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Correct answer: read only memory")

answer = input("What does PSU stand for?: ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Correct answer: power supply")

print(" ")
print("Number of points: " + str(score) + "/6")

if score <= 2:
    print("Not good at all")
elif score == 3:
    print("Good but you can do better")
elif score == 4 or score == 5:
    print("Very good, you got this :)")
else:
    print("Excellent, Nothing else to say")
