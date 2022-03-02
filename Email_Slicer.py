# email slicer
email_address = input("Enter the email address:  ").strip()  # the function strip is used to remove
# any space between letters

username = email_address[:email_address.index('@')]  # Here we use the slicing operator : and
# the index() function. the slice will operate until the index of the symbol in brackets,
# so it will only take the letters before...
domain = email_address[email_address.index('@') + 1:]  # the same process is used here

print(f"The username is {username} and the domain is {domain}")  # printing with the f-string structure
