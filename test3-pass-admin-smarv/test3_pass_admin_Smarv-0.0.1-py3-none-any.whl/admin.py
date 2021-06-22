from pass_admin.r_w_data import write_data
from tabulate import tabulate


class Admin:
    def __init__(self, username, password, data, file):
        self.username = username
        self.password = password
        self.data = data
        self.file = file

    def admin_log(self):
        # Login if there is admin data
        if self.data['admin_data']:
            for admin in self.data['admin_data']:
                if self.username in admin['username'] and self.password in admin['password']:
                    print('Login Successful!')
                    print('-' * 10)
                    return True

        # Sign in if there is no admin data
        else:
            while True:
                i = input('Reenter password for verification: ')
                if i == self.password:
                    self.data['admin_data'].append({'username': self.username,
                                                    'password': self.password})
                    write_data(self.file, self.data)
                    print('Sign in Successful!')
                    print('-' * 10)
                    return True

                else:
                    print('The passwords do not match, please try again!')

    def all_users(self):
        if self.data['user_data']:
            users_table = [['Username', 'Password', 'Nickname']]
            for user in self.data['user_data']:
                users_table.append([user['username'], user['password'], user['nickname']])

            print(tabulate(users_table))
            print('-' * 10)
        else:
            print('<Empty>')
            print('-' * 10)

    def del_user(self, user_del):
        flag = False
        for user in self.data['user_data']:
            if user_del == user['username'] or user_del == user['nickname']:
                print(f'{user["username"]}({user["nickname"]}) was deleted!')
                print('-' * 10)
                self.data['user_data'].remove(user)
                write_data(self.file, self.data)
                flag = True
                break

        if not flag:
            print(f'There is no user with username or nickname "{user_del}"!')
            print('-' * 10)

    def del_all_users(self):
        while True:
            print('Are you sure you want to delete all users data:\n'
                  'Y(yes) / N(no)')
            dell_all = input(': ')

            if dell_all.upper() == 'Y':
                self.data['user_data'].clear()
                write_data(self.file, self.data)
                print('All users data was deleted!')
                print('-' * 10)
                break

            elif dell_all.upper() == 'N':
                print('Delete all users data was canceled!')
                print('-' * 10)
                break

            else:
                print('Invalid input!\n'
                      'Please try again.')
