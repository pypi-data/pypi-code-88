import pexpect


def list_users():
    child = pexpect.spawn(
        '/opt/cloudhsm/bin/cloudhsm_mgmt_util /opt/cloudhsm/etc/cloudhsm_mgmt_util.cfg')
    child.expect('aws-cloudhsm>')
    child.sendline('listUsers')
    child.expect('aws-cloudhsm>')
    resp = child.before
    child.sendline('quit')

    return _user_dict(resp.decode().split())


def connect():
    child = pexpect.spawn(
        '/opt/cloudhsm/bin/cloudhsm_mgmt_util /opt/cloudhsm/etc/cloudhsm_mgmt_util.cfg', timeout=1)
    expected_resps = ['aws-cloudhsm>', pexpect.EOF, pexpect.TIMEOUT]

    i = child.expect(expected_resps)
    if i == 0:
        return {'data': {'child': child}}
    else:
        return {'error': expected_resps[i]}


def login(child, crypto_officer_type, crypto_officer_username, crypto_officer_password):
    child.sendline(
        f'loginHSM {crypto_officer_type} {crypto_officer_username} {crypto_officer_password}')
    expected_resps = ['aws-cloudhsm>',
                      'HSM Error', pexpect.EOF, pexpect.TIMEOUT]

    i = child.expect(expected_resps)
    if i == 0:
        return {'data': {'child': child}}
    elif i == 1:
        child.sendline('quit')
        child.expect([pexpect.EOF, pexpect.TIMEOUT])
        child.close()
        return {'error': expected_resps[i]}
    else:
        child.close()
        return {'error': expected_resps[i]}


def change_user_password(child, user_type, user_username, user_password):
    child.sendline(f'changePswd {user_type} {user_username} {user_password}')
    expected_resps = [
        'Do you want to continue(y/n)?', pexpect.EOF, pexpect.TIMEOUT]

    i = child.expect(expected_resps)
    if i != 0:
        child.close()
        return {'error': expected_resps[i]}
    else:
        child.sendline('y')
        expected_resps = ['aws-cloudhsm>', "user doesn't exist",
                          "min pswd len 7 and max pswd len 32", pexpect.EOF, pexpect.TIMEOUT]

        i = child.expect(expected_resps)
        if i == 0:
            return {'data': {'child': child, 'user': {'type': user_type, 'username': user_username, 'password': user_password}}}
        elif i > 2:
            child.close()
            return {'error': expected_resps[i]}
        else:
            child.sendline('A')
            resp = child.expect(
                ['aws-cloudhsm>', pexpect.EOF, pexpect.TIMEOUT])
            if resp == 0:
                child.sendline('quit')
                child.expect([pexpect.EOF, pexpect.TIMEOUT])
                child.close()
                return {'error': expected_resps[i]}
            else:
                child.close()
                return {'error': expected_resps[i]}


def create_user(child, user_type, user_username, user_password):
    child.sendline(f'createUser {user_type} {user_username} {user_password}')
    expected_resps = [
        'Do you want to continue(y/n)?', pexpect.EOF, pexpect.TIMEOUT]

    i = child.expect(expected_resps)
    if i != 0:
        child.close()
        return {'error': expected_resps[i]}
    else:
        child.sendline('y')
        expected_resps = ['aws-cloudhsm>', "invalid user type", "Invalid input data/params",
                          "min pswd len 7 and max pswd len 32", pexpect.EOF, pexpect.TIMEOUT]

        i = child.expect(expected_resps)
        if i == 0:
            return {'data': {'child': child, 'user': {'type': user_type, 'username': user_username, 'password': user_password}}}
        elif i > 2:
            child.close()
            return {'error': expected_resps[i]}
        else:
            child.sendline('A')
            resp = child.expect(
                ['aws-cloudhsm>', pexpect.EOF, pexpect.TIMEOUT])
            if resp == 0:
                child.sendline('quit')
                child.expect([pexpect.EOF, pexpect.TIMEOUT])
                child.close()
                return {'error': expected_resps[i]}
            else:
                child.close()
                return {'error': expected_resps[i]}


def quit(child):
    child.sendline('quit')
    child.expect([pexpect.EOF, pexpect.TIMEOUT])
    child.close()


def _user_dict(user_list):
    user_list = user_list[user_list.index('2FA') + 1:]
    n, users = 0, []
    for elem in user_list:
        n += 1
        mod = n % 6
        if mod == 1:
            dict = {}
            dict['id'] = elem
        elif mod == 2:
            dict['user_type'] = elem
        elif mod == 3:
            dict['username'] = elem
        elif mod == 4:
            dict['MofnPubKey'] = elem
        elif mod == 5:
            dict['LoginFailureCnt'] = elem
        elif mod == 0:
            dict['2FA'] = elem
            users.append(dict)
    return users


def test_connection():
    child = pexpect.spawn(
        '/opt/cloudhsm/bin/cloudhsm_mgmt_util /opt/cloudhsm/etc/cloudhsm_mgmt_util.cfg')
    i = child.expect([
        'aws-cloudhsm>',
        'Connection to one of servers failed, exiting...',
        pexpect.EOF,
        pexpect.TIMEOUT
    ])
    if i == 0:
        child.sendline('quit')
        child.expect(pexpect.EOF)
        return True
    else:
        return False


class LoginHSMError(Exception):
    pass


class ChangePasswordError(Exception):
    pass
