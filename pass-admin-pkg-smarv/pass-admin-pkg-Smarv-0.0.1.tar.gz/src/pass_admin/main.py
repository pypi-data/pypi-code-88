from pass_admin.admin import Admin
from pass_admin.user import User
from pass_admin.login_err import login_err
from pass_admin.r_w_data import read_data


def run_program(data_json):
    data = dict()
    data['admin_data'] = []
    data['user_data'] = []

    try:
        # Reading data and adding it to the data dict.
        read_data(data_json, data)
    except OSError:
        # Creating a file if it does not exist
        f = open(data_json, 'w')
        f.close()

    # Main mode loop
    while True:
        print('Main mode:\n'
              'Enter 1 to Log In as Admin.\n'
              'Enter 2 to Log In as User.\n'
              'Enter 3 to Sign In as User.\n'
              'Enter 4 to Exit.')

        i = input(': ')
        if i == '1':
            admin = Admin(data, data_json)
            # Admin log/sign in loop
            while True:
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
                            # Display all users and go back to Admin mode
                        elif admin_i == '2':
                            admin.del_user()
                            # Delete a user and go back to Admin mode
                        elif admin_i == '3':
                            admin.del_all_users()
                            # Delete all users and go back to Admin mode
                        elif admin_i == '4':
                            break
                            # Admin mode loop break
                        else:
                            print('Invalid input!\n'
                                  'Please try again.')
                            # Back to Admin mode
                    break
                    # Admin log/sign loop break. Back to Main mode

                else:
                    # Incorrect username or password message
                    back = login_err()
                    if back:
                        break
                        # Admin log/sign loop break. Back to Main mode
                    # else: Go back to Admin log in (username and password input)

        elif i == '2':
            user = User(data, data_json)
            # User login loop
            while True:
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
                            user.edit_username()
                            # Edit username and go back to User mode
                        elif user_i == '2':
                            user.edit_password()
                            # Edit password and go back to User mode
                        elif user_i == '3':
                            user.edit_nickname()
                            # Edit nickname and go back to User mode
                        elif user_i == '4':
                            print(user)
                            print('-' * 10)
                            # Back to User mode
                        elif user_i == '5':
                            break
                            # User mode loop break
                        else:
                            print('Invalid input!\n'
                                  'Please try again.')
                            # Back to User mode

                    break
                    # User login loop break. Back to Main mode

                else:
                    # Incorrect username or password message
                    back = login_err()
                    if back:
                        break
                        # User login loop break. Back to Main mode
                    # else: Go back to User log in (username and password input)

        elif i == '3':
            User(data, data_json).user_sign()
            # Successful sign in and back to Main mode

        elif i == '4':
            print('Exit!')
            break
            # Program Exit

        else:
            print('Invalid input!\n'
                  'Please try again.')
            # Back to Main mode


if __name__ == '__main__':
    run_program('data.json')
