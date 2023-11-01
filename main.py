def menu():
    print('Menu\n-------------\n1. Encode\n2.Decode\n3. Quit\n')


# Alejandro Fluitt
def Encode(password):
    new_password = ''
    num = 0
    for i in password:
        num = int(i) + 3
        new_password += str(num)[-1]
    return new_password


# Connor Patchen
def decode(password):
    old_password = ''
    num = 0
    for i in password:
        num = int(i) + 7
        old_password += str(num)[-1]
    return old_password


if __name__ == '__main__':
    while True:
        menu()
        user_input = input('Please enter an option: ')
        if user_input == '1':
            password = input('Please enter your password to encode: ')
            print('Your password has been encoded and stored!')
            passwprd = Encode(password)
        elif user_input == '2':
            print(f'The encoded passworf is {password}, and the original passworf is {decode(password)}')
        elif user_input == '3':
            break
