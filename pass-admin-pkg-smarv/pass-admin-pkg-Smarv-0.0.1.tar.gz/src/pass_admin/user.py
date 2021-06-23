from pass_admin.r_w_data import write_data


class User:
    def __init__(self, data, file):
        self.username = ''
        self.password = ''
        self.nickname = ''
        self.data = data
        self.file = file

    def __str__(self):
        return f'Username: {self.username}\n' \
               f'Password: {self.password}\n' \
               f'Nickname: {self.nickname}' \


    def user_sign(self):
        # Username input loop
        while True:
            self.username = input('Username: ')
            name_taken = False
            for user in self.data['user_data']:
                # Checking for existing username or nickname
                if self.username == user['username'] or self.username == user['nickname']:
                    name_taken = True
                    break
                    # For loop break

            if name_taken:
                print('This name is already taken.\n'
                      'Please choose another name.')
                # Back to username input
            else:
                break
                # Username loop break. Proceed to password input

        # Password input loop
        while True:
            self.password = input('Password: ')
            # Password length condition
            if len(self.password) < 6:
                print('The password must have at least 6 characters.')
                continue
                # Back to password input

            # Password verification
            verification = input('Reenter password for verification: ')
            if verification == self.password:
                self.data['user_data'].append({'username': self.username,
                                               'password': self.password,
                                               'nickname': self.nickname})

                write_data(self.file, self.data)
                print('Sign In Successful!')
                print('-' * 10)
                break
                # Password loop break and successful sign in.

            else:
                print('The passwords do not match, please try again!')
                # Back to password input

    def user_log(self):
        self.username = input('Username: ')
        self.password = input('Password: ')
        for user in self.data['user_data']:
            if self.username == user['username'] and self.password == user['password']:
                print('Login Successful!')
                print('-' * 10)
                return True
                # Logged in

    def edit_username(self):
        # New username loop
        while True:
            new_username = input('Enter new username: ')
            name_taken = False
            for user in self.data['user_data']:
                if new_username == user['username'] or new_username == user['nickname']:
                    name_taken = True
                    break
                    # For loop break

            if name_taken:
                print('This name is already taken.\n'
                      'Please choose another name.')
                # Back to new username input
            else:
                for user in self.data['user_data']:
                    if self.username == user['username']:
                        user['username'] = new_username
                        self.username = new_username
                        break
                        # For loop break

                write_data(self.file, self.data)
                print('Username successfully changed!')
                print('-' * 10)
                break
                # New username input loop break

    def edit_password(self):
        # New password loop
        while True:
            new_password = input('Enter new password: ')
            # Password length condition
            if len(new_password) < 6:
                print('The password must have at least 6 characters.')
                continue
                # Back to new password input

            # Password verification
            verification = input('Reenter password for verification: ')
            if verification == new_password:
                for user in self.data['user_data']:
                    if self.username == user['username']:
                        user['password'] = new_password
                        self.password = new_password
                        break
                        # For loop break

                write_data(self.file, self.data)
                print('Password successfully changed!')
                print('-' * 10)
                break
                # New password loop break

            else:
                print('The passwords do not match, please try again!')
                # Back to new password input

    def edit_nickname(self):
        # New nickname loop
        while True:
            new_nickname = input('Enter new nickname: ')
            name_taken = False
            for user in self.data['user_data']:
                if new_nickname == user['username'] or new_nickname == user['nickname']:
                    name_taken = True
                    break
                    # For loop break

            if name_taken:
                print('This name is already taken.\n'
                      'Please choose another name.')
                # Back to new nickname input
            else:
                for user in self.data['user_data']:
                    if self.username == user['username']:
                        user['nickname'] = new_nickname
                        self.nickname = new_nickname
                        break
                        # For loop break

                write_data(self.file, self.data)
                print(f'Your nickname is changed to {new_nickname}.')
                print('-' * 10)
                break
                # New nickname loop break
