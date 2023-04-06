# from pathlib import Path
#
# filepath = Path.home() / 'Documents' / 'Pycharm_Projects'
passwordFile = open('SecretPasswordFile.txt', 'w')
passwordFile.write("qwerty")
secretPassword = open('SecretPasswordFile.txt', 'r')
print('Enter your password.')
typedPassword = input()
if typedPassword == secretPassword:
    print('Access granted')
    if typedPassword == '12345':
        print('That password is one that an idiot puts on their luggage.')
    else:
        print('Access denied')
