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
        moved = term.move_customer_ca_crt()
        if moved is False:
            raise FileNotFoundError('Unable move customerCA.crt')

        configured = term.configure_cloudhsm_mgmt_utility(eni_ip=self.eni_ip)
        if configured is False:
            raise CloudHSMMgmtUtilityConfigureError(
                'Unable to configure the CloudHSM Mgmt Utility')

        connected = _can_connect_to_cloudhsm_mgmt_utility()
        if connected is False:
            raise ConnectionError('Unable to Connect to CloudHSM Mgt Utility')

        changed = cmu.change_user_password(
            crypto_officer_type='PRECO',
            crypto_officer_username='admin',
            crypto_officer_password='password',
            user_type='PRECO',
            user_username='admin',
            user_password=self.crypto_officer_password
        )

        created = cmu.create_user(
            crypto_officer_type="CO",
            crypto_officer_username="admin",
            crypto_officer_password=self.crypto_officer_password,
            user_type="CU",
            user_username=self.crypto_user_username,
            user_password=self.crypto_user_password
        )

        return True

    def _change_preco_password(self):
        cmu.change_user_password(
            crypto_officer_type='PRECO',
            crypto_officer_username='admin',
            crypto_officer_password='password',
            user_type='PRECO',
            user_username='admin',
            user_password=self.crypto_officer_password
        )
        return

    def _create_crypto_user(self):
        cmu.create_user(
            crypto_officer_type="CO",
            crypto_officer_username="admin",
            crypto_officer_password=self.crypto_officer_password,
            user_type="CU",
            user_username=self.crypto_user_username,
            user_password=self.crypto_user_password
        )

        return


def _can_connect_to_cloudhsm_mgmt_utility(count=0):
    count += 1
    print(count)

    resp = cmu.test_connection()
    if resp is True:
        return True

    if count < 5:
        time.sleep(1)
        _can_connect_to_cloudhsm_mgmt_utility(count=count)

    return resp


class ConnectionError(Exception):
    pass


class FileNotFoundError(Exception):
    pass


class CloudHSMMgmtUtilityConfigureError(Exception):
    pass
