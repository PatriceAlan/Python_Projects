import array
vals = array.array('i', [])
number = int(input("Enter the number of values of the array: "))
for i in range(number):
    n = int(input("Enter the value "+str(i + 1)+": "))
    vals.append(n)
print("Your array is: "+str(vals))

print("What do you want to do next ?:")
print("1- Add new values")
print("2- Remove some values")
print("3- Reverse the values of the array")
print("4- Get the number of occurrences of a number")
print("5- Get the length in bytes")
print("6- Get the current memory address and length in elements")
print("7- Quit")
chc = int(input("Make your choice: "))

while True:
    if chc == 1:
        number = int(input("Enter the number of values to add to the array: "))
        for i in range(number):
            n = int(input("Enter the value " + str(i + 1) + ": "))
            vals.append(n)
            print("The new array is: "+str(vals))
    elif chc == 2:
        number = int(input("Enter the number of values to remove: "))
        for i in range(number):
            n = int(input("Enter the value to remove: "))
            vals.remove(n)
            print("The new array is: " + str(vals))
    elif chc == 3:
        vals.reverse()
        print("The reversed array is: "+str(vals))
    elif chc == 4:
        m = int(input("Enter the number you want to know the number of occurrences: "))
        print("The number of occurrences of "+str(m)+" is: "+str(vals.count(m)))
    elif chc == 5:
        print("The length in bytes is " + str(vals.itemsize))
    elif chc == 6:
        print("The current memory address and length in elements: "+str(vals.buffer_info()))
    elif chc == 7:
        print("OK, goodbye")
        quit()
    else:
        print("Please make a choice")
        break

