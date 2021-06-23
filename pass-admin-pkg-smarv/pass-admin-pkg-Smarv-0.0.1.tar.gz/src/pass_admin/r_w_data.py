import json


def read_data(json_file, data):
    with open(json_file) as file:
        try:
            read = json.load(file)
            for admin in read['admin_data']:
                data['admin_data'].append({'username': admin['username'],
                                           'password': admin['password']})

            for user in read['user_data']:
                data['user_data'].append({'username': user['username'],
                                          'password': user['password'],
                                          'nickname': user['nickname']})

        except json.decoder.JSONDecodeError:
            pass


def write_data(json_file, data):
    with open(json_file, 'w') as file:
        json.dump(data, file)
