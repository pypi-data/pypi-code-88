def login_err():
    print('The username or password is incorrect!\n'
          'Enter 0 to go back to Main mode or else to try again.')

    i = input(': ')
    if i == '0':
        return True
