
import app.scripts.terminal_scripts as term
from app.controllers.cloudhsm_mgmt_util_controller import CloudHSMMgmtUtil
import app.scripts.cloudhsm_mgmt_utility_scripts as cmu
import os
import time


class Activate:

    def __init__(self, eni_ip, crypto_officer_username, crypto_officer_password, crypto_user_username, crypto_user_password):
        self.eni_ip = eni_ip
        self.crypto_officer_username = crypto_officer_username
        self.crypto_officer_password = crypto_officer_password
        self.crypto_user_username = crypto_user_username
        self.crypto_user_password = crypto_user_password

    def crypto_officer(self):
        try:
            moved = term.move_customer_ca_cert()
            assert moved, 'Unable move customerCA.crt'

            crypto_officer = self.activate_cloudhsm_mgmt_util()

            return {'crypto_officer': crypto_officer}

        except Exception as e:
            return {'error': e}

    def activate_cloudhsm_mgmt_util(self):
        cloudhsm_mgmt_util = CloudHSMMgmtUtil(
            eni_ip=self.eni_ip,
            crypto_officer_username=self.crypto_officer_username,
            crypto_officer_password='password'
        )
        cloudhsm_mgmt_util.active = True
        cloudhsm_mgmt_util.crypto_officer_type = 'PRECO'
        cloudhsm_mgmt_util.change_password(
            user_type='PRECO',
            username=self.crypto_officer_username,
            new_password=self.crypto_officer_password
        )
        cloudhsm_mgmt_util.quit()
        cloudhsm_mgmt_util.crypto_officer_password = self.crypto_officer_password
        crypto_officers = cloudhsm_mgmt_util.crypto_officers
        for co in crypto_officers:
            if co['username'] == self.crypto_officer_username and co['user_type'] == 'CO':
                return {
                    'type': co['user_type'],
                    'username': co['username'],
                    'password': self.crypto_officer_password
                }

        raise ActivateCloudHSMUtilError('Crypto Officer not created')


class ActivateCloudHSMUtilError(Exception):
    pass


# def activate_crypto_officer(crypto_officer_password):
#     crypto_officers = _get_crypto_officers()
#     if crypto_officers:
#         assert len(crypto_officers) == 1, 'Multiple Crypto Officers exist.'
#         crypto_officer = {
#             'type': crypto_officers[0]['user_type'],
#             'username': crypto_officers[0]['username'],
#             'password': crypto_officer_password
#         }
#     else:
#         child = _login_as_preco(child=child)
#         child, crypto_officer = _change_preco_to_crypto_officer(
#             child=child, crypto_officer_password=crypto_officer_password)
#         cmu.quit(child=child)

#     return crypto_officer


# def create_crypto_user(crypto_officer_password, crypto_user_username, crypto_user_password):
#     child = _connect()
#     child = _login_as_crypto_officer(
#         child=child, crypto_officer_password=crypto_officer_password)
#     child, crypto_user = _create_crypto_user(
#         child=child, crypto_user_username=crypto_user_username, crypto_user_password=crypto_user_password)
#     cmu.quit(child=child)

#     return crypto_user


# def _get_crypto_officers():
#     child = _connect()
#     users = cmu.list_users(child=child)
#     crypto_officers = [user for user in users if user['user_type'] == 'CO']
#     if len(crypto_officers) == 0:
#         return False
#     else:
#         return crypto_officers


# def _configure_cloudhsm_mgmt_utility(eni_ip):
#     configured = term.configure_cloudhsm_mgmt_utility(eni_ip=eni_ip)
#     assert configured, 'Unable to configure the CloudHSM Mgmt Utility'
#     return configured


# def _connect(count=0):
#     count += 1
#     try:
#         resp = cmu.connect()
#         assert resp.get('error') is None, f"#connect: {resp['error']}"
#         return resp['data']['child']
#     except AssertionError as e:
#         if count > 5:
#             raise ConnectionError(e.args[0])
#         else:
#             return _connect(count=count)


# def _login_as_preco(child, count=0):
#     count += 1
#     try:
#         resp = cmu.login(
#             child=child,
#             crypto_officer_type='PRECO',
#             crypto_officer_username='admin',
#             crypto_officer_password='password'
#         )
#         assert resp.get('error') is None, f"#login_as_preco: {resp['error']}"
#         return resp['data']['child']
#     except AssertionError as e:
#         error_type = e.args[0].split(': ')[1]
#         if count > 5:
#             raise LoginError(e.args[0])
#         elif error_type == 'HSM Error':
#             raise UserNotValidError('PRECO is not a valid user.')
#         else:
#             return _login_as_preco(child=child, count=count)


# def _login_as_crypto_officer(child, crypto_officer_password, count=0):
#     count += 1
#     if count > 5:
#         raise UserNotValidError("Crypto Office is not a valid user.")

#     try:
#         resp = cmu.login(
#             child=child,
#             crypto_officer_type='CO',
#             crypto_officer_username='admin',
#             crypto_officer_password=crypto_officer_password
#         )
#         assert resp.get(
#             'error') is None, f"#login_as_crypto_officer: {resp['error']}"
#         return resp['data']['child']

#     except AssertionError as e:
#         error_type = e.args[0].split(': ')[1]
#         if count > 5:
#             raise LoginError(e.args[0])
#         if error_type == 'HSM Error':
#             raise UserNotValidError("Crypto Office is not a valid user.")
#         else:
#             return _login_as_crypto_officer(
#                 child=child,
#                 crypto_officer_password=crypto_officer_password,
#                 count=count
#             )


# def _change_preco_to_crypto_officer(child, crypto_officer_password):
#     resp = cmu.change_user_password(
#         child=child,
#         user_type='PRECO',
#         user_username='admin',
#         user_password=crypto_officer_password
#     )
#     assert resp.get(
#         'error') is None, f"#change_preco_to_crypto_officer: {resp['error']}"
#     return resp['data']['child'], resp['data']['user']


# def _create_crypto_user(child, crypto_user_username, crypto_user_password):
#     resp = cmu.create_user(child=child, user_type="CU",
#                            user_username=crypto_user_username, user_password=crypto_user_password)
#     assert resp.get('error') is None, f"#create_crypto_user: {resp['error']}"
#     return resp['data']['child'], resp['data']['user']


# class UserNotValidError(Exception):
#     pass


# class LoginError(Exception):
#     pass


# class ConnectionError(Exception):
#     pass
