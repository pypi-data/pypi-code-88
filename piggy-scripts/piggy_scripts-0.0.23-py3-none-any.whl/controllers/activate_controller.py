
import app.scripts.terminal_scripts as term
from app.controllers.cloudhsm_mgmt_util_controller import CloudHSMMgmtUtil, LoginError
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

    def run(self):
        try:
            crypto_officer = self.activate_cloudhsm_mgmt_util()
            crypto_user = self.create_crypto_user()
            return {'crypto_officer': crypto_officer, 'crypto_user': crypto_user}

        except ActivateCloudHSMUtilError as e:
            return {'error': e.args[0]}

        except CreateCryptoUserError as e:
            return {'error': e.args[0]}

    def activate_cloudhsm_mgmt_util(self):
        move_customer_ca_cert()

        co_cmu = CloudHSMMgmtUtil(
            eni_ip=self.eni_ip,
            crypto_officer_type='CO',
            crypto_officer_username=self.crypto_officer_username,
            crypto_officer_password=self.crypto_officer_password,
        )

        if co_cmu.active is True:
            try:
                co_cmu.login()
                co_cmu.quit()
                return {'type': 'CO', 'username': self.crypto_officer_username, 'password': self.crypto_officer_password}
            except LoginError:
                raise ActivateCloudHSMUtilError(
                    'CloudHSM Utility is active but crypto office username and password are not valid.')
        else:
            preco_cmu = CloudHSMMgmtUtil(
                eni_ip=self.eni_ip,
                crypto_officer_type='PRECO',
                crypto_officer_username=self.crypto_officer_username,
                crypto_officer_password='password'
            )
            # change active to True to prevent CMU from throwing an error
            preco_cmu.active = True
            preco_cmu.change_password(
                user_type='PRECO',
                username=self.crypto_officer_username,
                new_password=self.crypto_officer_password
            )
            preco_cmu.quit()

        co_cmu.active = co_cmu.is_active()
        if co_cmu.active is True:
            return {
                'type': 'CO',
                'username': self.crypto_officer_username,
                'password': self.crypto_officer_password
            }
        else:
            raise ActivateCloudHSMUtilError('Crypto Officer not created')

    def create_crypto_user(self):
        cu_cmu = CloudHSMMgmtUtil(
            eni_ip=self.eni_ip,
            crypto_officer_type='CO',
            crypto_officer_username=self.crypto_officer_username,
            crypto_officer_password=self.crypto_officer_password
        )
        if cu_cmu.active is False:
            raise CreateCryptoUserError(
                'CloudHSM Mgmt Utility must be active to create a crypto user.')

        crypto_users = cu_cmu.crypto_users
        for cu in crypto_users:
            if cu['username'] == self.crypto_user_username:
                try:
                    cu_cmu.crypto_user_login(
                        username=self.crypto_user_username, password=self.crypto_user_password)
                    cu_cmu.quit()
                    return {'type': 'CU', 'username': self.crypto_user_username, 'password': self.crypto_user_password}
                except LoginError:
                    raise CreateCryptoUserError(
                        f'Crypto User {self.crypto_user_username} exists, but password is not valid.')

        cu_cmu.create_user(
            user_type="CU",
            username=self.crypto_user_username,
            password=self.crypto_user_password
        )
        cu_cmu.quit()

        crypto_users = cu_cmu.crypto_users
        for cu in crypto_users:
            if cu['username'] == self.crypto_user_username:
                return {
                    'type': cu['user_type'],
                    'username': cu['username'],
                    'password': self.crypto_user_password
                }

        raise CreateCryptoUserError(
            f'Crypto User {self.crypto_user_username} was not created')


def move_customer_ca_cert():
    moved = term.move_customer_ca_cert()
    if moved is True:
        return True
    else:
        raise ActivateCloudHSMUtilError('Unable to move customerCA.crt')


class ActivateCloudHSMUtilError(Exception):
    pass


class CreateCryptoUserError(Exception):
    pass
