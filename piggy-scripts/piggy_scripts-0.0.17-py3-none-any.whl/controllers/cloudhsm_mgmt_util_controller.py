import app.scripts.terminal_scripts as term
import app.scripts.cloudhsm_mgmt_utility_scripts as cmu

import time
import json


class CloudHSMMgmtUtilController():

    def __init__(self, eni_ip, crypto_officer_username, crypto_officer_password):
        self.eni_ip = eni_ip
        self.crypto_officer_type = "CO"
        self.crypto_officer_username = crypto_officer_username
        self.crypto_officer_password = crypto_officer_password
        self.child = False
        self.logged_in = False
        self.configured = self.configure()
        self.active = self.is_active()

    @classmethod
    def activate(cls, eni_ip, crypto_officer_password):
        util = cls(
            eni_ip=eni_ip,
            crypto_officer_username='admin',
            crypto_officer_password='password'
        )
        breakpoint()

    @property
    def hostname(self):
        with open('/opt/cloudhsm/etc/cloudhsm_client.cfg', 'r') as file:
            client_data_json = file.read()
        client_data = json.loads(client_data_json)
        hostname = client_data['server']['hostname']
        return hostname

    @property
    def users(self):
        if self.child is False:
            resp = self.connect()
        users = cmu.list_users(child=self.child)
        resp = self.quit()
        return users

    @property
    def crypto_officers(self):
        crypto_officers = [
            user for user in self.users if user['user_type'] == 'CO']
        return crypto_officers

    @property
    def crypto_users(self):
        crypto_users = [
            user for user in self.users if user['user_type'] == 'CU']
        return crypto_users

    @property
    def pre_crypto_officers(self):
        pre_crypto_officers = [
            user for user in self.users if user['user_type'] == 'PRECO']
        return pre_crypto_officers

    def is_active(self):
        if len(self.pre_crypto_officers) != 0:
            False
        else:
            return True

    def configure(self, count=0):
        count += 1
        if self.hostname == self.eni_ip:
            return True
        try:
            output = term.configure_cloudhsm_mgmt_util(eni_ip=self.eni_ip)
            time.sleep(1)
            assert self.hostname == self.eni_ip
            return True
        except AssertionError as e:
            if count > 5:
                raise ConfigurationError(
                    'Unable to configure the CloudHSM Mgmt Util')
            else:
                return self.configure(count=count)

    def connect(self, count=0):
        count += 1
        try:
            resp = cmu.connect()
            assert resp.get('error') is None, f"#connect: {resp['error']}"

            child = resp['data']['child']
            self.child = child
            return True

        except AssertionError as e:
            if count > 5:
                raise ConnectionError(e.args[0])
            else:
                return self.connect(count=count)

    def login(self):
        if self.active is False:
            raise CloudMgmtUtilNotActiveError(
                'Must activate the CloudHSM Mgmt Util first')
        if self.child is False:
            self.connect()
        try:
            resp = cmu.login(
                child=self.child,
                crypto_officer_type=self.crypto_officer_type,
                crypto_officer_username=self.crypto_officer_username,
                crypto_officer_password=self.crypto_officer_password
            )
            assert resp.get('error') is None, f"Login Failed: {resp['error']}"

            return True

        except AssertionError as e:
            self.child = False
            raise LoginError(e.args[0])

    def change_password(self, user_type, username, new_password):
        if self.child is False:
            self.connect()
        if self.logged_in is False:
            self.login()

        try:
            resp = cmu.change_user_password(
                child=self.child,
                user_type=user_type,
                user_username=username,
                user_password=new_password
            )
            assert resp.get(
                'error') is None, f"Change password failed: {resp['error']}"
            return True
        except AssertionError as e:
            self.child = False
            raise ChangePasswordError(e.args[0])

    def create_user(self, user_type, username, password):
        if self.child is False:
            self.connect()
        if self.logged_in is False:
            self.login()

        try:
            resp = cmu.create_user(
                child=self.child,
                user_type=user_type,
                user_username=username,
                user_password=password
            )
            assert resp.get(
                'error') is None, f"Create user failed: {resp['error']}"
            return True
        except AssertionError as e:
            self.child = False
            raise CreateUserError(e.args[0])

    def quit(self):
        if self.child is False:
            return True
        else:
            cmu.quit(child=self.child)
            self.child = False
            return True


class CloudMgmtUtilNotActiveError(Exception):
    pass


class ConfigurationError(Exception):
    pass


class ConnectionError(Exception):
    pass


class LoginError(Exception):
    pass


class ChangePasswordError(Exception):
    pass


class CreateUserError(Exception):
    pass
