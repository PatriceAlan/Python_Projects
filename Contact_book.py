# contact book
names = []
phone_numbers = []

while True:
    print("---------------------------------------------------------------------------------Welcome to your CONTACT "
          "BOOK "
          "!!!---------------------------------------------------------------------------------------------------")
    print("\n")
    print("What do you want to do ?:")
    print("1-Insert new contacts")
    print("2-Search for new contacts")
    print("3-Remove a contact")
    print("4-show your lists of contacts")
    print("5-Quit")
    print("\n")
    chc = int(input(" "))

    if chc == 1:
        no = int(input("How many numbers do want to insert ?:  "))
        for i in range(no):
            name = input("Name: ")
            phone_number = input("Phone Number: ")
            names.append(name)
            phone_numbers.append(phone_number)

    elif chc == 2:
        search_term = input("\nEnter Search Term: ")
        print("Search Result")
        if search_term in names:
            index = names.index(search_term)
            phone_number = phone_numbers[index]
            print("Name {}, Phone Number: {}".format(search_term, phone_number))
        else:
            print("Name not found")

    elif chc == 3:
        to_remove = input("Enter the name of the contact to delete: ")
        if to_remove in names:
            names.remove(to_remove)
            print("The contact has been deleted")
        else:
            print("This contact does not appear in the list")

    elif chc == 4:
        for i in range(len(phone_numbers)):
            if not phone_numbers:
                print("There are no contacts")
            else:
                print("Name\t\t\tPhone number")
                print("______\t\t\t_________")
                print("{}\t\t\t{}".format(names[i], phone_numbers[i]))

    elif chc == 5:
        print("Ok, thanks and goodbye...")
        quit()

    while chc != 1 or 2 or 3 or 4:
        chc = int(input("Wrong choice, choose again:  "))
    break
