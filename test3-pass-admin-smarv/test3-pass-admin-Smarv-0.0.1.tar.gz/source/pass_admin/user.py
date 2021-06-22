from pass_admin.r_w_data import write_data


class User:
    def __init__(self, username, password, data, file):
        self.username = username
        self.password = password
        self.nickname = None
        self.data = data
        self.file = file

    def __str__(self):
        return f'Username: {self.username}\n' \
               f'Password: {self.password}\n' \
               f'Nickname: {self.nickname}' \


    def user_sign(self):
        while True:
            i = input('Reenter password for verification: ')
            if i == self.password:
                self.data['user_data'].append({'username': self.username,
                                               'password': self.password,
                                               'nickname': self.nickname})

                write_data(self.file, self.data)
                print('Sign in Successful!')
                print('-' * 10)

                break

            else:
                print('The passwords do not match, please try again!')

    def user_log(self):
        for user in self.data['user_data']:
            if self.username == user['username'] and self.password == user['password']:
                print('Login Successful!')
                print('-' * 10)
                return True

    def edit_username(self, new_username):
        for user in self.data['user_data']:
            if self.username == user['username']:
                user['username'] = new_username
                self.username = new_username
                break

        write_data(self.file, self.data)
        print('Username successfully changed!')
        print('-' * 10)

    def edit_password(self, new_password):
        for user in self.data['user_data']:
            if self.username == user['username']:
                user['password'] = new_password
                self.password = new_password
                break

        write_data(self.file, self.data)
        print('Password successfully changed!')
        print('-' * 10)

    def edit_nickname(self, new_nickname):
        for user in self.data['user_data']:
            if self.username == user['username']:
                user['nickname'] = new_nickname
                self.nickname = new_nickname
                break

        write_data(self.file, self.data)
        print(f'Your nickname is changed to {new_nickname}.')
        print('-' * 10)
