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


def change_user_password(crypto_officer_type, crypto_officer_username, crypto_officer_password,
                         user_type, user_username, user_password):
    child = pexpect.spawn(
        '/opt/cloudhsm/bin/cloudhsm_mgmt_util /opt/cloudhsm/etc/cloudhsm_mgmt_util.cfg')
    child.expect('aws-cloudhsm>')
    child.sendline(
        f'loginHSM {crypto_officer_type} {crypto_officer_username} {crypto_officer_password}')
    i = child.expect(['HSM Error', 'aws-cloudhsm>'])
    if i == 0:
        child.sendline('quit')
        child.expect(pexpect.EOF)
        raise LoginHSMError(
            f'Username: {crypto_officer_username} login failed')
    elif i == 1:
        child.sendline(
            f'changePswd {user_type} {user_username} {user_password}')
        child.expect('Do you want to continue(y/n)?')
        child.sendline('y')
        i1 = child.expect(['Retry/Ignore/Abort?(R/I/A)', 'aws-cloudhsm>'])
        if i1 == 0:
            child.sendline('A')
            child.expect('aws-cloudhsm>')
            child.sendline('quit')
            child.expect(pexpect.EOF)
            raise ChangePasswordError(
                f'Change password for username: {user_username} failed')
        elif i1 == 1:
            resp = child.before
            child.sendline('quit')
            child.expect(pexpect.EOF)

    if 'success' in resp.decode().split():
        return ' '.join(resp.decode().split()[1:])
    else:
        raise Exception('Unspecified change password failure.')


def create_user(crypto_officer_type, crypto_officer_username, crypto_officer_password,
                user_type, user_username, user_password):
    child = pexpect.spawn(
        '/opt/cloudhsm/bin/cloudhsm_mgmt_util /opt/cloudhsm/etc/cloudhsm_mgmt_util.cfg')
    child.expect('aws-cloudhsm>')
    child.sendline(
        f'loginHSM {crypto_officer_type} {crypto_officer_username} {crypto_officer_password}')
    i = child.expect(['HSM Error', 'aws-cloudhsm>'])
    if i == 0:
        child.sendline('quit')
        child.expect(pexpect.EOF)
        raise LoginHSMError(
            f'Username: {crypto_officer_username} login failed')
    elif i == 1:
        child.sendline(
            f'createUser {user_type} {user_username} {user_password}')
        child.expect('Do you want to continue(y/n)?')
        child.sendline('y')
        i1 = child.expect(['Retry/Ignore/Abort?(R/I/A)', 'aws-cloudhsm>'])
        if i1 == 0:
            child.sendline('A')
            child.expect('aws-cloudhsm>')
            child.sendline('quit')
            child.expect(pexpect.EOF)
            raise ChangePasswordError(f'Create user: {user_username} failed')
        elif i1 == 1:
            resp = child.before
            child.sendline('quit')
            child.expect(pexpect.EOF)

    if 'success' in resp.decode().split():
        return ' '.join(resp.decode().split()[1:])
    else:
        raise Exception('Unspecified create user failure.')


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
        pexpect.EOF
    ])
    if i == 0:
        child.sendline('quit')
        child.expect(pexpect.EOF)
        return True
    elif i == 1:
        return 'Connection to one of servers failed'
    else:
        return 'Unexpected EOF'


class LoginHSMError(Exception):
    pass


class ChangePasswordError(Exception):
    pass
