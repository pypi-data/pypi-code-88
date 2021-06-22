from pass_admin.admin import Admin
from pass_admin.user import User
from pass_admin.admin_check import admin_check
from pass_admin.login_err import login_err
from pass_admin.r_w_data import read_data


def run_program(file_name):
    data_json = file_name
    data = dict()
    data['admin_data'] = []
    data['user_data'] = []

    try:
        # Reading data and adding it to the data dict.
        read_data(data_json, data)
    except FileNotFoundError:
        # Creating a file if it does not exist
        f = open(data_json, 'w')
        f.close()

    # Main mode loop
    while True:
        print('Main mode:\n'
              'Enter 1 to Login as Admin.\n'
              'Enter 2 to Login as User.\n'
              'Enter 3 to Sign in new User.\n'
              'Enter 4 to Exit.')

        i = input(': ')
        if i == '1':
            # Check for existing admin and display message for Login or Sign in
            admin_check(data)

            # Admin login/sign in loop
            while True:
                username = input('Username: ')
                password = input('Password: ')
                admin = Admin(username, password, data, data_json)

                if admin.admin_log():
                    # Admin mode loop
                    while True:
                        print('Admin mode:\n'
                              'Enter 1 to see all users.\n'
                              'Enter 2 to delete a user.\n'
                              'Enter 3 to delete all users.\n'
                              'Enter 4 to go back.')

                        admin_i = input(': ')
                        if admin_i == '1':
                            admin.all_users()
                        elif admin_i == '2':
                            user = input('Enter the user\'s username or nickname to delete it: ')
                            admin.del_user(user)
                        elif admin_i == '3':
                            admin.del_all_users()
                        elif admin_i == '4':
                            # Admin mode loop break
                            break

                        else:
                            # Back to Admin mode
                            print('Invalid input!\n'
                                  'Please try again.')
                    # Back to Main mode
                    break

                else:
                    # Incorrect username or password message
                    re = login_err()
                    if re:
                        # Back to username and password input
                        continue
                    else:
                        # Back to Main mode
                        break

        elif i == '2':
            # User login loop
            while True:
                username = input('Username: ')
                password = input('Password: ')
                user = User(username, password, data, data_json)

                if user.user_log():
                    # User mode loop
                    while True:
                        print('User mode:\n'
                              'Enter 1 to Edit username.\n'
                              'Enter 2 to Edit password.\n'
                              'Enter 3 to Edit nickname.\n'
                              'Enter 4 for User information.\n'
                              'Enter 5 to go back.')

                        user_i = input(': ')
                        if user_i == '1':
                            # Edit username loop
                            while True:
                                new_name = input('Enter new username: ')
                                name_taken = False
                                for u in data['user_data']:
                                    if new_name == u['username'] or new_name == u['nickname']:
                                        print('This name is already taken.\n'
                                              'Please choose another name.')
                                        name_taken = True
                                        # For loop break
                                        break

                                if name_taken:
                                    # Back to new username input
                                    continue
                                else:
                                    verification = input('Reenter username for verification: ')

                                if new_name == verification:
                                    user.edit_username(new_name)
                                    # Back to User mode
                                    break

                                else:
                                    # Back to new username input
                                    print('The usernames do not match, please try again!')

                        elif user_i == '2':
                            # Edit password loop
                            while True:
                                new_pass = input('Enter new password: ')
                                verification = input('Reenter password for verification: ')
                                if new_pass == verification:
                                    user.edit_password(new_pass)
                                    # Back to User mode
                                    break

                                else:
                                    # Back to new password input
                                    print('The passwords do not match, please try again!')

                        elif user_i == '3':
                            # Edit nickname loop
                            while True:
                                new_nick = input('Enter new nickname: ')
                                name_taken = False
                                for u in data['user_data']:
                                    if new_nick == u['nickname'] or new_nick == u['username']:
                                        print('This name is already taken.\n'
                                              'Please choose another name.')
                                        name_taken = True
                                        # For loop break
                                        break

                                if name_taken:
                                    # Back to new nickname input
                                    continue
                                else:
                                    user.edit_nickname(new_nick)
                                    # Back to User mode
                                    break

                        elif user_i == '4':
                            print(user)
                            print('-' * 10)
                            # Back to User mode

                        elif user_i == '5':
                            # User mode loop break
                            break

                        else:
                            # Back to User mode
                            print('Invalid input!\n'
                                  'Please try again.')
                    # Back to Main mode
                    break

                else:
                    # Incorrect username or password message
                    re = login_err()
                    if re:
                        # Back to username and password input
                        continue
                    else:
                        # Back to Main mode
                        break

        elif i == '3':
            # User sign in loop
            while True:
                username = input('Enter username: ')
                name_taken = False
                for u in data['user_data']:
                    if username == u['username'] or username == u['nickname']:
                        print('This name is already taken.\n'
                              'Please choose another name.')
                        name_taken = True
                        # For loop break
                        break

                if name_taken:
                    # Back to username input
                    continue
                else:
                    password = input('Enter password: ')
                    # Sign in loop break
                    break

            User(username, password, data, data_json).user_sign()
            # Successful sign in and back to Main mode

        elif i == '4':
            print('Exit!')
            # Exit main mode
            break

        else:
            # Back to Main mode
            print('Invalid input!\n'
                  'Please try again.')


if __name__ == '__main__':
    run_program('data_main.json')
