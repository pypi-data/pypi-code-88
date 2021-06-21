import app.scripts.terminal_scripts as term
import app.scripts.cloudhsm_mgmt_utility_scripts as cmu
import os
import time


class Activate:

    def __init__(self, eni_ip, crypto_officer_password, crypto_user_username, crypto_user_password):
        self.eni_ip = eni_ip
        self.crypto_officer_password = crypto_officer_password
        self.crypto_user_username = crypto_user_username
        self.crypto_user_password = crypto_user_password

    def run(self):
        try:
            moved = _move_customer_ca_cert()

            configured = _configure_cloudhsm_mgmt_utility(eni_ip=self.eni_ip)

            can_connect = _can_connect_to_cloudhsm_mgmt_utility()

            child = _connect()

            child = _login_as_preco(child=child)

            child, crypto_officer = _change_preco_to_crypto_officer(
                child=child, crypto_officer_password=self.crypto_officer_password)

            child, crypto_user = _create_crypto_user(
                child=child, crypto_user_username=self.crypto_user_username, crypto_user_password=self.crypto_user_password)

            cmu.quit(child=child)

            return {'crypto_officer': crypto_officer, 'crypto_user': crypto_user}

        except Exception as Error:

            return {'error': Error}


def _move_customer_ca_cert():
    moved = term.move_customer_ca_cert()
    assert moved, 'Unable move customerCA.crt'
    return moved


def _configure_cloudhsm_mgmt_utility(eni_ip):
    configured = term.configure_cloudhsm_mgmt_utility(eni_ip=eni_ip)
    assert configured, 'Unable to configure the CloudHSM Mgmt Utility'
    return configured


def _can_connect_to_cloudhsm_mgmt_utility(count=0):
    count += 1
    connected = cmu.test_connection()
    if connected is True:
        return True
    else:
        if count > 5:
            raise Exception('Unable to connect to CloudHSM Mgmt Utility')
        else:
            time.sleep(1)
            return _can_connect_to_cloudhsm_mgmt_utility(count=count)


def _connect():
    resp = cmu.connect()
    assert resp.get('error') is None, f"connect failed: {data['error']}"
    return resp['data']['child']


def _login_as_preco(child):
    resp = cmu.login(
        child=child,
        crypto_officer_type='PRECO',
        crypto_officer_username='admin',
        crypto_officer_password='password'
    )
    assert resp.get('error') is None, f"login failed: {resp['error']}"
    return resp['data']['child']


def _change_preco_to_crypto_officer(child, crypto_officer_password):
    resp = cmu.change_user_password(
        child=child,
        user_type='PRECO',
        user_username='admin',
        user_password=crypto_officer_password
    )
    assert resp.get(
        'error') is None, f"Change user password failed: {resp['error']}"
    return resp['data']['child'], resp['data']['user']


def _create_crypto_user(child, crypto_user_username, crypto_user_password):
    resp = cmu.create_user(child=child, user_type="CU",
                           user_username=crypto_user_username, user_password=crypto_user_password)
    assert resp.get('error') is None, f"Create user failed: {resp['error']}"
    return resp['data']['child'], resp['data']['user']
