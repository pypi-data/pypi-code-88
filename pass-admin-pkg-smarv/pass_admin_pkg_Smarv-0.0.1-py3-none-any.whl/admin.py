from pass_admin.r_w_data import write_data
from tabulate import tabulate


class Admin:
    def __init__(self, data, file):
        self.username = ''
        self.password = ''
        self.data = data
        self.file = file

    def admin_log(self):
        # Check for existing admin and display message for Log in or Sign in
        if self.data['admin_data']:
            print('Log In as admin:')
        else:
            print('There is no admin!\nSign In as admin:')

        self.username = input('Username: ')
        self.password = input('Password: ')
        # Log in if there is admin data
        if self.data['admin_data']:
            for admin in self.data['admin_data']:
                if self.username in admin['username'] and self.password in admin['password']:
                    print('Login Successful!')
                    print('-' * 10)
                    return True
                    # Logged in

        # Sign in if there is no admin data
        else:
            # Password verification loop
            while True:
                # Password length condition
                if len(self.password) < 6:
                    print('The password must have at least 6 characters.')
                    self.password = input('Password: ')
                    continue
                    # Back to password length check

                # Password verification
                verification = input('Reenter password for verification: ')
                if verification == self.password:
                    self.data['admin_data'].append({'username': self.username,
                                                    'password': self.password})

                    write_data(self.file, self.data)
                    print('Sign In Successful!')
                    print('-' * 10)
                    return True
                    # Logged in

                else:
                    print('The passwords do not match, please try again!')
                    # Back to password verification input

    def all_users(self):
        if self.data['user_data']:
            users_table = [['Username', 'Password', 'Nickname']]
            for user in self.data['user_data']:
                users_table.append([user['username'], user['password'], user['nickname']])

            print(tabulate(users_table))
            print('-' * 10)
        else:
            print('No Data Found.')
            print('-' * 10)

    def del_user(self):
        if self.data['user_data']:
            user_del = input('Enter the user\'s username or nickname to delete it: ')
            if not user_del:
                print('Invalid input!')
            else:
                in_data = False
                for user in self.data['user_data']:
                    if user_del == user['username'] or user_del == user['nickname']:
                        print(f'{user["username"]}({user["nickname"]}) was deleted!')
                        print('-' * 10)
                        self.data['user_data'].remove(user)
                        write_data(self.file, self.data)
                        in_data = True
                        break

                if not in_data:
                    print(f'There is no user with username or nickname "{user_del}"!')
                    print('-' * 10)
        else:
            print('No Data Found.')
            print('-' * 10)

    def del_all_users(self):
        if self.data['user_data']:
            print('Are you sure you want to delete all users data?')
            dell_all = input('Y(yes) / N(no): ')

            if dell_all.upper() == 'Y':
                self.data['user_data'].clear()
                write_data(self.file, self.data)
                print('All users data was deleted!')
                print('-' * 10)
            elif dell_all.upper() == 'N':
                print('Delete all users data was canceled!')
                print('-' * 10)
            else:
                print('Invalid input!\n'
                      'Operation canceled.')
                print('-' * 10)
        else:
            print('No Data Found.')
            print('-' * 10)
