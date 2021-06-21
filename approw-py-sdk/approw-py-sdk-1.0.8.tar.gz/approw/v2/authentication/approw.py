# coding: utf-8
import re

from ..common.rest import RestClient
from .types import AuthenticationClientOptions
from ..common.graphql import GraphqlClient
from ..common.utils import encrypt, convert_udv_data_type, convert_udv_list_to_dict, get_hostname_from_url, \
    format_authorized_resources, get_random_string, url_join_args
from ..common.codegen import QUERY
from ..exceptions import ApprowWrongArgumentException, ApprowException
import json
import datetime
import base64
import hashlib


class AuthenticationClient(object):
    """Approw Management Client"""

    def __init__(self, options):
        # type:(AuthenticationClientOptions) -> AuthenticationClient

        self.options = options
        self.graphqlClient = GraphqlClient(
            options=self.options, endpoint=self.options.graphql_endpoint
        )
        self.restClient = RestClient(options=self.options)

        # Current user
        self._user = None
        # Current user's token
        self._token = self.options.token or None

    def _set_current_user(self, user):
        self._user = user
        self._token = user.get("token")

    def _clear_current_user(self):
        self._user = None
        self._token = None

    def _check_logged_in(self):
        user = self.get_current_user()
        if not user:
            raise Exception("Please Login First")
        return user

    def _get_token(self):
        return self._token

    def _set_token(self, token):
        self._token = token

    def get_current_user(self, token=None):
        """Get the current user's information

        Args:
            token (str): User authentciaton credentials
        """
        url = "%s/api/v2/users/me" % self.options.host
        data = self.restClient.request(
            method="GET", url=url, token=token or self._get_token()
        )
        code, message, user = data.get("code"), data.get(
            "message"), data.get("data")
        if code == 200:
            self._set_current_user(user)
            return user
        else:
            self.options.on_error(code, message)

    def register_by_email(
            self,
            email,
            password,
            profile=None,
            force_login=False,
            generate_token=False,
            client_ip=None,
            custom_data=None,
            context=None
    ):
        """Register by email

        Args:
            email (str): email
            password (str): password
            profile (dict): profile
            force_login (bool): force_login
            generate_token (bool): generate_token
            client_ip (str): client_ip
            custom_data (dict): user-defined data
            context (dict): context
        """
        password = encrypt(password, self.options.enc_public_key)

        params = []
        if custom_data:
            if not isinstance(custom_data, dict):
                raise Exception('custom_data must be a dict')
            for k, v in custom_data.items():
                params.append({
                    'key': k,
                    'value': v
                })
        context = context and json.dumps(context)
        data = self.graphqlClient.request(
            query=QUERY["registerByEmail"],
            params={
                "input": {
                    "email": email,
                    "password": password,
                    "profile": profile,
                    "forceLogin": force_login,
                    "generateToken": generate_token,
                    "clientIp": client_ip,
                    "params": json.dumps(params) if len(params) > 0 else None,
                    "context": context
                }
            },
        )
        user = data["registerByEmail"]
        self._set_current_user(user)
        return user

    def register_by_username(
            self,
            username,
            password,
            profile=None,
            force_login=False,
            generate_token=False,
            client_ip=None,
            custom_data=None,
            context=None
    ):
        """Register by username

        Args:
            username (str): username
            password (str): password
            profile (dict): profile
            force_login (bool): force_login
            generate_token (bool): generate_token
            client_ip (str): client_ip
            custom_data (dict): user-defined data
            context (dict): context
        """
        password = encrypt(password, self.options.enc_public_key)
        params = []
        if custom_data:
            if not isinstance(custom_data, dict):
                raise Exception('custom_data must be a dict')
            for k, v in custom_data.items():
                params.append({
                    'key': k,
                    'value': v
                })
        context = context and json.dumps(context)
        data = self.graphqlClient.request(
            query=QUERY["registerByUsername"],
            params={
                "input": {
                    "username": username,
                    "password": password,
                    "profile": profile,
                    "forceLogin": force_login,
                    "generateToken": generate_token,
                    "clientIp": client_ip,
                    "params": json.dumps(params) if len(params) > 0 else None,
                    "context": context
                }
            },
        )
        user = data["registerByUsername"]
        self._set_current_user(user)
        return user

    def register_by_phone_code(
            self,
            phone,
            code,
            password=None,
            profile=None,
            force_login=False,
            generate_token=False,
            client_ip=None,
            custom_data=None,
            context=None
    ):
        """Register with mobile phone number

        Args:
            phone (str): phone
            code (str): code
		    password (str): password
            profile (dict): profile
            force_login (bool): force_login
            generate_token (bool): generate_token
            client_ip (str): client_ip
            custom_data (dict): user-defined data
            context (dict): context
        """
        if password:
            password = encrypt(password, self.options.enc_public_key)
        params = []
        if custom_data:
            if not isinstance(custom_data, dict):
                raise Exception('custom_data must be a dict')
            for k, v in custom_data.items():
                params.append({
                    'key': k,
                    'value': v
                })
        context = context and json.dumps(context)
        data = self.graphqlClient.request(
            query=QUERY["registerByPhoneCode"],
            params={
                "input": {
                    "phone": phone,
                    "code": code,
                    "password": password,
                    "profile": profile,
                    "forceLogin": force_login,
                    "generateToken": generate_token,
                    "clientIp": client_ip,
                    "params": json.dumps(params) if len(params) > 0 else None,
                    "context": context
                }
            },
        )
        user = data["registerByPhoneCode"]
        self._set_current_user(user)
        return user

    def send_sms_code(self, phone):
        """Send SMS code

        Args:
            phone (str): phone
        """
        url = "%s/api/v2/sms/send" % self.options.host
        data = self.restClient.request(
            method="POST", url=url, token=None, json={"phone": phone}
        )
        return data

    def login_by_email(
            self,
            email,
            password,
            auto_register=False,
            captcha_code=None,
            client_ip=None,
            custom_data=None,
            context=None
    ):
        """login by email

        Args:
            email (str): email
            password (str): password
            auto_register (bool): auto_register
            captcha_code (str): captcha_code
            client_ip (str): client_ip
            custom_data (dict): custom_data
            context (dict): context
        """
        password = encrypt(password, self.options.enc_public_key)
        params = []
        if custom_data:
            if not isinstance(custom_data, dict):
                raise Exception('custom_data must be a dict')
            for k, v in custom_data.items():
                params.append({
                    'key': k,
                    'value': v
                })
        context = context and json.dumps(context)
        data = self.graphqlClient.request(
            query=QUERY["loginByEmail"],
            params={
                "input": {
                    "email": email,
                    "password": password,
                    "autoRegister": auto_register,
                    "captchaCode": captcha_code,
                    "clientIp": client_ip,
                    "params": json.dumps(params) if len(params) > 0 else None,
                    "context": context
                }
            },
        )
        user = data["loginByEmail"]
        self._set_current_user(user)
        return user

    def login_by_username(
            self,
            username,
            password,
            auto_register=False,
            captcha_code=None,
            client_ip=None,
            custom_data=None,
            context=None
    ):
        """login by username

        Args:
            username (str): username
            password (str): password
            auto_register (bool): auto_register
            captcha_code (str): captcha_code
            client_ip (str): client_ip
            custom_data (dict): custom_data
            context (dict): context
        """
        password = encrypt(password, self.options.enc_public_key)
        params = []
        if custom_data:
            if not isinstance(custom_data, dict):
                raise Exception('custom_data must be a dict')
            for k, v in custom_data.items():
                params.append({
                    'key': k,
                    'value': v
                })
        context = context and json.dumps(context)
        data = self.graphqlClient.request(
            query=QUERY["loginByUsername"],
            params={
                "input": {
                    "username": username,
                    "password": password,
                    "autoRegister": auto_register,
                    "captchaCode": captcha_code,
                    "clientIp": client_ip,
                    "params": json.dumps(params) if len(params) > 0 else None,
                    "context": context
                }
            },
        )
        user = data["loginByUsername"]
        self._set_current_user(user)
        return user

    def login_by_phone_code(
            self,
            phone,
            code,
            client_ip=None,
            custom_data=None,
            context=None
        ):
        """login by phone code

        Args:
            phone (str): phone
            code (str): code
            client_ip (str): client_ip
            custom_data (dict): custom_data
            context (dict): context
        """
        params = []
        if custom_data:
            if not isinstance(custom_data, dict):
                raise Exception('custom_data must be a dict')
            for k, v in custom_data.items():
                params.append({
                    'key': k,
                    'value': v
                })
        context = context and json.dumps(context)
        data = self.graphqlClient.request(
            query=QUERY["loginByPhoneCode"],
            params={
                "input": {
                    "phone": phone,
                    "code": code,
                    "clientIp": client_ip,
                    "params": json.dumps(params) if len(params) > 0 else None,
                    "context": context
                }
            },
        )
        user = data["loginByPhoneCode"]
        self._set_current_user(user)
        return user

    def login_by_phone_password(
            self,
            phone,
            password,
            auto_register=False,
            captcha_code=None,
            client_ip=None,
            custom_data=None,
            context=None
    ):
        """login by phone password

        Args:
            phone (str): phone
            password (str): password
            auto_register (bool): auto_register
            captcha_code (str): captcha_code
            client_ip (str): client_ip
            custom_data (dict): custom_data
            context (dict): context
        """
        password = encrypt(password, self.options.enc_public_key)
        params = []
        if custom_data:
            if not isinstance(custom_data, dict):
                raise Exception('custom_data must be a dict')
            for k, v in custom_data.items():
                params.append({
                    'key': k,
                    'value': v
                })
        context = context and json.dumps(context)
        data = self.graphqlClient.request(
            query=QUERY["loginByPhonePassword"],
            params={
                "input": {
                    "phone": phone,
                    "password": password,
                    "autoRegister": auto_register,
                    "captchaCode": captcha_code,
                    "clientIp": client_ip,
                    "params": json.dumps(params) if len(params) > 0 else None,
                    "context": context
                }
            },
        )
        user = data["loginByPhonePassword"]
        self._set_current_user(user)
        return user

    def login_by_ldap(self, username, password):
        """login by ldap

        Args:
            username: (str): LDAP username
            password: (str): LDAP password
        """

        url = "%s/api/v2/ldap/verify-user" % self.options.host
        data = self.restClient.request(
            method="POST", url=url, json={
                'username': username,
                'password': password
            }
        )
        code, message, user = data.get("code"), data.get(
            "message"), data.get("data")
        if code == 200:
            self._set_current_user(user)
            return user
        else:
            self.options.on_error(code, message)

    def login_by_ad(self, username, password):
        """
        login by ad 

        Args:
            username: (str): AD username
            password: (str): AD password
        """
        hostname = get_hostname_from_url(self.options.host)
        first_level_domain = '.'.join(hostname.split('.')[1:]) if len(hostname.split('.')) > 2 else hostname
        websocket_host = self.options.websocket_host or "https://ws.%s" % first_level_domain
        url = "%s/api/v2/ad/verify-user" % websocket_host
        data = self.restClient.request(
            method="POST", url=url, json={
                'username': username,
                'password': password
            }
        )
        code, message, user = data.get("code"), data.get(
            "message"), data.get("data")
        if code == 200:
            self._set_current_user(user)
            return user
        else:
            self.options.on_error(code, message)

    def check_password_strength(self, password):
        """password strength checking，learn more https://docs.authing.co/v2/guides/security/config-password.html"""
        data = self.graphqlClient.request(
            query=QUERY['checkPasswordStrength'],
            params={
                'password': password
            }
        )
        return data['checkPasswordStrength']

    def check_login_status(self, token=None):
        """check login/token status

        Args:
            token (str): token
        """
        data = self.graphqlClient.request(
            query=QUERY["checkLoginStatus"], params={
                "token": token or self._token}
        )
        return data["checkLoginStatus"]

    def send_email(self, email, scene):
        """send email"""
        data = self.graphqlClient.request(
            query=QUERY["sendEmail"], params={"email": email, "scene": scene}
        )
        return data["sendEmail"]

    def reset_password_by_phone_code(self, phone, code, new_password):
        """reset password by sms code

        Args:
            phone (str): phone
            code (str): code
            new_password (str): new password
        """
        new_password = encrypt(new_password, self.options.enc_public_key)
        data = self.graphqlClient.request(
            query=QUERY["resetPassword"],
            params={"phone": phone, "code": code, "newPassword": new_password},
        )
        return data["resetPassword"]

    def reset_password_by_email_code(self, email, code, new_password):
        """reset password by email

        Args:
            email (str): email
            code (str): code
            new_password (str): new password
        """
        new_password = encrypt(new_password, self.options.enc_public_key)
        data = self.graphqlClient.request(
            query=QUERY["resetPassword"],
            params={"email": email, "code": code, "newPassword": new_password},
        )
        return data["resetPassword"]

    def update_profile(self, updates):
        """update profile"""
        user = self._check_logged_in()
        data = self.graphqlClient.request(
            query=QUERY["updateUser"],
            params={"id": user["id"], "input": updates},
            token=self._get_token(),
        )
        user = data["updateUser"]
        self._set_current_user(user)
        return user

    def update_password(self, new_password, old_password):
        """change password

        Args:
            new_password (str): new password
            old_password (str): old password
        """
        new_password = encrypt(new_password, self.options.enc_public_key)
        old_password = encrypt(old_password, self.options.enc_public_key)
        data = self.graphqlClient.request(
            query=QUERY["updatePassword"],
            params={"newPassword": new_password, "oldPassword": old_password},
            token=self._get_token(),
        )
        user = data["updatePassword"]
        return user

    def update_phone(self, phone, phone_code, old_phone=None, old_phone_code=None):
        """
        Update a user's mobile phone number. Just like modifying the mailbox, by default, if the user has already bound a mobile phone number, the original mobile phone number (the mobile phone number bound to the current account) and the current phone number (the mobile phone number to be bound) need to be verified at the same time. '
        In other words, the mobile phone number currently bound to user A is 6000000000, and if you want to change it to 611111111, you need to verify both mobile phone numbers at the same time.
        Developers can also choose not to turn on "Verify original phone number", which can be turned off in the security information module under the settings directory of the Authing console.
        Please use the bind_phone interface to bind a mobile phone number for a new user.
        Args:
            phone (str): new cell phone number
            phone_code (str): new sms code from new cell phone
            old_phone (str): old cell phone number
            old_phone_code (str): sms code from old cell phone
        """
        data = self.graphqlClient.request(
            query=QUERY["updatePhone"],
            params={
                "phone": phone,
                "phoneCode": phone_code,
                "oldPhone": old_phone,
                "oldPhoneCode": old_phone_code,
            },
            token=self._get_token(),
        )
        user = data["updatePhone"]
        self._set_current_user(user)
        return user

    def update_email(self, email, email_code, old_email=None, old_email_code=None):
        """
        If the user has already bound a email address, the original email address (the email address bound to the current account) and the current phone number (the email address to be bound) need to be verified at the same time. '
        In other words, the email address currently bound to user A is 6000000000, and if you want to change it to 611111111, you need to verify both email addresses at the same time.
        Developers can also choose not to turn on "Verify original phone number", which can be turned off in the security information module under the settings directory of the Authing console.
        Please use the bind_phone interface to bind a email address for a new user.

        Args:
            email (str): new email address
            email_code (str): verification code from new email address
            old_email (str): old email address
            old_email_code (str): verification code from old email address
        """
        data = self.graphqlClient.request(
            query=QUERY["updateEmail"],
            params={
                "email": email,
                "emailCode": email_code,
                "oldEmail": old_email,
                "oldEmailCode": old_email_code,
            },
            token=self._get_token(),
        )
        user = data["updatePhone"]
        self._set_current_user(user)
        return user

    def link_account(self, primary_user_token, secondary_user_token):
        """Link account with social account。Bind a social account (such as twitter account, GitHub account) to a main account (mobile phone number, email account)

        Args:
            primary_user_token (str): primary_user Token
            secondary_user_token (str): secondary_user Token
        """
        url = "%s/api/v2/users/link" % self.options.host
        self.restClient.request(
            method="POST", url=url, token=self._get_token(), json={
                'primaryUserToken': primary_user_token,
                'secondaryUserToken': secondary_user_token
            }
        )
        return True

    def unlink_account(self, primary_user_token, provider):
        """"unlink the social login account

        Args:
            primary_user_token (str): primary_user Token
            provider (str): social login account provider
        """
        url = "%s/api/v2/users/unlink" % self.options.host
        self.restClient.request(
            method="POST", url=url, token=self._get_token(), json={
                'primaryUserToken': primary_user_token,
                'provider': provider
            }
        )
        return True

    def refresh_token(self, token=None):
        """refresh token

        Returns:
            [type]: [description]
        """
        data = self.graphqlClient.request(
            query=QUERY["refreshToken"], params={}, token=token or self._get_token()
        )
        token = data["refreshToken"].get("token")
        self._set_token(token)
        return data["refreshToken"]

    def bind_phone(self, phone, phone_code):
        """
        The user binds the mobile phone number for the first time. If you need to modify the mobile phone number, please use updatePhone.
        If this cell phone number has been binded with other account, it will fail.
        The verification code by sms.

        Args:
            phone (str): phone number
            phone_code (str): sms verification code
        """
        data = self.graphqlClient.request(
            query=QUERY["bindPhone"],
            params={"phone": phone, "phoneCode": phone_code},
            token=self._get_token(),
        )
        user = data["bindPhone"]
        self._set_current_user(user)
        return user

    def unbind_phone(self):
        """If the user unbind the mobile phone number, if the user is not bound to other login methods (email, social login account), the mobile phone number will not be unbound, and an error will be displayed."""
        data = self.graphqlClient.request(
            query=QUERY["unbindPhone"], params={}, token=self._get_token()
        )
        user = data["unbindPhone"]
        self._set_current_user(user)
        return user

    def bind_email(self, email, email_code):
        """
        It is used for the user to bind the mailbox for the first time.
        If you need to modify the email, please use the update_email method.
        If the mailbox has been bound, the binding will fail. Please use the send_email method to send the email verification code.

        Args:
            email (str): email
            email_code (str): verification code
        """
        data = self.graphqlClient.request(
            query=QUERY["bindEmail"], params={
                "email": email,
                "emailCode": email_code
            }, token=self._get_token()
        )
        user = data["bindEmail"]
        self._set_current_user(user)
        return user

    def unbind_email(self):
        """If the user unbinds the mailbox, if the user is not bound to other login methods (mobile phone number, social login account), the mailbox will not be unbound and an error will be displayed."""
        data = self.graphqlClient.request(
            query=QUERY["unbindEmail"], params={
            }, token=self._get_token()
        )
        user = data["unbindEmail"]
        self._set_current_user(user)
        return user

    def get_udf_value(self):
        """Get the custom user data of the current user"""
        user = self._check_logged_in()
        data = self.graphqlClient.request(
            query=QUERY["udv"],
            params={"targetType": "USER", "targetId": user["id"]},
            token=self._get_token(),
        )
        data = data['udv']
        return convert_udv_list_to_dict(data)

    def set_udf_value(self, data):
        """
        Set user-defined fields.
         You need to define user-defined data metadata in the user pool first, and the type of the incoming value must match the defined type.
         If the setting fails, an exception will be thrown, and you need to catch the exception.

        Args:
            data (dict): Custom data
        """
        user = self._check_logged_in()
        if len(data.keys()) == 0:
            raise ApprowWrongArgumentException('data must not be a empty dict')
        list = []
        for k, v in data.items():
            if isinstance(v, datetime.datetime):
                def default(o):
                    if isinstance(o, (datetime.date, datetime.datetime)):
                        return o.isoformat()

                v = json.dumps(v, sort_keys=True,
                               indent=1, default=default)
            else:
                v = json.dumps(v)
            list.append({
                'key': k,
                'value': v
            })
        self.graphqlClient.request(
            query=QUERY['setUdvBatch'],
            params={
                'targetType': 'USER',
                'targetId': user['id'],
                'udvList': list
            },
            token=self._get_token()
        )
        return True

    def remove_udf_value(self, key):
        """
        Delete custom data.

        Args:
            key (str): key
        """
        user = self._check_logged_in()
        self.graphqlClient.request(
            query=QUERY['removeUdv'],
            params={
                'targetType': 'USER',
                'targetId': user['id'],
                'key': key
            },
            token=self._get_token()
        )
        return True

    def list_udv(self):
        """[Abandoned, please use get_udf_vale] Get the current user's custom user data"""
        user = self._check_logged_in()
        data = self.graphqlClient.request(
            query=QUERY["udv"],
            params={"targetType": "USER", "targetId": user["id"]},
            token=self._get_token(),
        )
        data = data["udv"]
        return convert_udv_data_type(data)

    def set_udv(self, key, value):
        """Set up custom user data

        Args:
            key (type): key
            value (type): value
        """
        user = self._check_logged_in()
        if isinstance(value, datetime.datetime):

            def default(o):
                if isinstance(o, (datetime.date, datetime.datetime)):
                    return o.isoformat()

            value = json.dumps(value, sort_keys=True,
                               indent=1, default=default)
        else:
            value = json.dumps(value)
        data = self.graphqlClient.request(
            query=QUERY["setUdv"],
            params={
                "targetType": "USER",
                "targetId": user["id"],
                "key": key,
                "value": value,
            },
            token=self._get_token(),
        )
        data = data["setUdv"]
        return convert_udv_data_type(data)

    def remove_udv(self, key):
        """Delete user-defined field data

        Args:
            key (str): key
        """
        user = self._check_logged_in()
        data = self.graphqlClient.request(
            query=QUERY["removeUdv"],
            params={
                "targetType": "USER",
                "targetId": user["id"],
                "key": key,
            },
            token=self._get_token(),
        )
        data = data["removeUdv"]
        return convert_udv_data_type(data)

    def logout(self):
        """ The user logs out.
         1. Clear the user's session information under the current application;
         2. Mark the user's current id_token as invalid, and use this id_token to call the Approw interface to obtain the relevant data.
        """
        self._check_logged_in()
        url = "%s/api/v2/logout?app_id=%s" % (self.options.host, self.options.app_id)
        self.restClient.request(
            method="GET", url=url, token=self._get_token()
        )
        self._clear_current_user()
        return True

    def list_orgs(self):
        """
        Get the user's organization list
        """
        url = "%s/api/v2/users/me/orgs" % self.options.host
        data = self.restClient.request(
            method="GET",
            url=url,
            token=self._get_token()
        )
        code, message, data = data.get("code"), data.get(
            "message"), data.get("data")
        if code == 200:
            return data
        else:
            self.options.on_error(code, message)

    def get_security_level(self):
        """
        Get account's security level
        """
        url = "%s/api/v2/users/me/security-level" % self.options.host
        data = self.restClient.request(
            method='GET',
            url=url,
            token=self._get_token()
        )
        code, message, data = data.get("code"), data.get(
            "message"), data.get("data")
        if code == 200:
            return data
        else:
            self.options.on_error(code, message)

    def list_roles(self, namespace=None):
        """
        Get the list of roles

        Args:
            namespace (str):  namespace
        """
        user = self._check_logged_in()
        data = self.graphqlClient.request(
            query=QUERY["getUserRoles"],
            params={
                "id": user['id'],
                "namespace": namespace
            },
            token=self._get_token()
        )
        res = data["user"]["roles"]
        return res

    def has_role(self, code, namespace=None):
        """Determine whether the user has a certain role

        Args:
            code (str): Character's unique identifier code
            namespace (str):  namespace
        """
        data = self.list_roles(namespace)
        _list, total_count = data['list'], data['totalCount']

        if total_count == 0:
            return False

        has_role = False
        for item in _list:
            if item.get('code') == code:
                has_role = True
        return has_role

    def list_applications(self, page=1, limit=10):
        """
        Get the list of apps that the user can access

        Args:
            page (int) page number, start from 1，The default is 1.
            limit (int) page number limit. The defaul is 10.
        """
        url = "%s/api/v2/users/me/applications/allowed?page=%s&limit=%s" % (self.options.host, page, limit)
        data = self.restClient.request(
            method="GET",
            url=url,
            token=self._get_token()
        )
        code, message, data = data.get("code"), data.get(
            "message"), data.get("data")
        if code == 200:
            return data
        else:
            self.options.on_error(code, message)

    def list_authorized_resources(self, namespace, resource_type=None):
        """
        Get all the resources authorized by a user. All the resources authorized by the user include resources inherited from roles, groups, and organizations.

        Args:
            namespace (str) namespace
            resource_type (str) resource type，the value include DATA、API、MENU、UI、BUTTON
        """

        user = self._check_logged_in()
        valid_resource_types = [
            'DATA',
            'API',
            'MENU',
            'UI',
            'BUTTON'
        ]
        if not valid_resource_types.index(resource_type):
            raise ApprowWrongArgumentException('invalid argument: resource_type')
        data = self.graphqlClient.request(
            query=QUERY['listUserAuthorizedResources'],
            params={
                'id': user.get('id'),
                'namespace': namespace,
                'resourceType': resource_type
            }
        )
        data = data.get('user')
        if not data:
            raise ApprowException(500, 'user not exists')

        authorized_resources = data.get('authorizedResources')
        _list, total_count = authorized_resources.get('list'), authorized_resources.get('totalCount')
        _list = format_authorized_resources(_list)
        return {
            'totalCount': total_count,
            'list': _list
        }

    def compute_password_security_level(self, password):
        """
        compute the password security level.

        Args:
            password (str)
        """
        high_level_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^]{12,}$"
        middle_level_regex = r"^(?=.*[a-zA-Z])(?=.*\d)[^]{8,}$"
        if re.match(high_level_regex, password):
            return 1

    def ___get_access_token_by_code_with_client_secret_post(self, code, code_verifier=None):
        url = "%s/%s/token" % (self.options.host, 'oidc' if self.options.protocol == 'oidc' else 'oauth')
        data = self.restClient.request(
            method='POST',
            url=url,
            data={
                'client_id': self.options.app_id,
                'client_secret': self.options.secret,
                'grant_type': 'authorization_code',
                'code': code,
                'redirect_uri': self.options.redirect_uri,
                'code_verifier': code_verifier
            }
        )
        return data

    def ___get_access_token_by_code_with_client_secret_basic(self, code, code_verifier=None):
        url = "%s/%s/token" % (self.options.host, 'oidc' if self.options.protocol == 'oidc' else 'oauth')
        data = self.restClient.request(
            method='POST',
            url=url,
            data={
                'grant_type': 'authorization_code',
                'code': code,
                'redirect_uri': self.options.redirect_uri,
                'code_verifier': code_verifier
            },
            basic_token=base64.b64encode(('%s:%s' % (self.options.app_id, self.options.secret)).encode()).decode()
        )
        return data

    def __get_access_token_by_code_with_none(self, code, code_verifier=None):
        url = "%s/%s/token" % (self.options.host, 'oidc' if self.options.protocol == 'oidc' else 'oauth')
        data = self.restClient.request(
            method='POST',
            url=url,
            data={
                'client_id': self.options.app_id,
                'grant_type': 'authorization_code',
                'code': code,
                'redirect_uri': self.options.redirect_uri,
                'code_verifier': code_verifier
            }
        )
        return data

    def get_access_token_by_code(self, code, code_verifier=None):
        """
        Use the authorization code Code to get the user's Token information.

        Args:
            code (str): Authorization code. After the user is successfully authenticated, Approw will send the authorization code to the callback address.
            code_verifier (str): This parameter needs to be filled in when PKCE authorized login is initiated.
        """

        if self.options.protocol not in ['oidc', 'oauth']:
            raise ApprowWrongArgumentException('argument protocol must be oidc or oauth')

        if not self.options.redirect_uri:
            raise ApprowWrongArgumentException('argument redirect_uri must be oidc or oauth')

        if not self.options.secret and self.options.token_endpoint_auth_method != 'none':
            raise ApprowWrongArgumentException('argument secret must be provided')

        if self.options.token_endpoint_auth_method == 'client_secret_post':
            return self.___get_access_token_by_code_with_client_secret_post(code, code_verifier)

        elif self.options.token_endpoint_auth_method == 'client_secret_basic':
            return self.___get_access_token_by_code_with_client_secret_basic(code, code_verifier)

        elif self.options.token_endpoint_auth_method == 'none':
            return self.__get_access_token_by_code_with_none(code, code_verifier)

        raise ApprowWrongArgumentException(
            'unsupported argument token_endpoint_auth_method, must be client_secret_post, client_secret_basic or none')

    def get_access_token_by_client_credentials(self, scope, access_key, access_secret):
        """
        Use programmatic access account to obtain access token with permission.

        Args:
            scope (str): Permission items, a space-separated string, each item represents a permission.
            access_key (str): AccessKey
            access_secret (str): SecretKey
        """

        if not scope:
            raise ApprowWrongArgumentException(
                'must provide scope argument, see doc here: '
                'https://docs.authing.cn/v2/guides/authorization/m2m-authz.html')

        url = "%s/%s/token" % (self.options.host, 'oidc' if self.options.protocol == 'oidc' else 'oauth')
        data = self.restClient.request(
            method='POST',
            url=url,
            data={
                'client_id': access_key,
                'client_secret': access_secret,
                'grant_type': 'client_credentials',
                'scope': scope
            }
        )
        return data

    def get_user_info_by_access_token(self, access_token):
        """
        Use Access token to get user information.

        Args:
            access_token (str) Access token.
        """
        url = "%s/%s/me" % (self.options.host, 'oidc' if self.options.protocol == 'oidc' else 'oauth')

        data = self.restClient.request(
            method='POST',
            url=url,
            token=access_token
        )
        return data

    def __build_saml_authorize_url(self):
        return "%s/api/v2/saml-idp/%s" % (self.options.app_host, self.options.app_id)

    def __build_cas_authorize_url(self, service=None):
        if service:
            return "%s/cas-idp/%s?service=%s" % (self.options.app_host, self.options.app_id, service)
        else:
            return "%s/cas-idp/%s?service" % (self.options.app_host, self.options.app_id)

    def __build_oauth_authorize_url(self, scope=None, redirect_uri=None, state=None, response_type=None):
        res = {
            'state': get_random_string(10),
            'scope': 'user',
            'client_id': self.options.app_id,
            'redirect_uri': self.options.redirect_uri,
            'response_type': 'code'
        }
        if scope:
            res['scope'] = scope

        if redirect_uri:
            res['redirect_uri'] = redirect_uri

        if state:
            res['state'] = state

        if response_type:
            if response_type not in ['code', 'token']:
                raise ApprowWrongArgumentException('response_type must be code or token')
            res['response_type'] = response_type

        return url_join_args('%s/oauth/auth' % self.options.app_host, res)

    def __build_oidc_authorize_url(self, redirect_uri=None, response_type=None, response_mode=None,
                                   state=None, nonce=None, scope=None,
                                   code_challenge_method=None, code_challenge=None):
        """
        Generate the user login address of the OIDC protocol.

        Args:
            redirect_uri (str): Callback address(optional). The default is a parameter of redirectUri  when SDK is initialized.
            response_type (str): Resonse type(optional)，The value can be code、code id_token token、code id_token、code id_token、code token、id_token token、id_token、none；default is code.
            response_mode (str):  response mode(optional)，The value can be query、fragment、form_post；the default is query
            state (str): Random string(optional), automatically generated by default.
            nonce (str): Random string(optional), automatically generated by default.
            scope (str): Requested permission item(optional), the default of OIDC is openid profile email phone address，the default of OAuth 2.0 is user.
            code_challenge_method (str): it can be plain orS256，
            code_challenge (str): A string with a length greater than or equal to 43，as a code_challenge sending to Approw.
        """
        res = {
            'nonce': get_random_string(10),
            'state': get_random_string(10),
            'scope': 'openid profile email phone address',
            'client_id': self.options.app_id,
            'redirect_uri': self.options.redirect_uri,
            'response_type': 'code'
        }

        if redirect_uri:
            res['redirect_uri'] = redirect_uri

        if response_type:
            res['response_type'] = response_type

        if response_mode:
            res['response_mode'] = response_mode

        if state:
            res['state'] = state

        if scope:
            if 'offline_access' in scope:
                res['prompt'] = 'consent'

        if nonce:
            res['nonce'] = nonce

        if code_challenge:
            res['code_challenge'] = code_challenge

        if code_challenge_method:
            res['code_challenge_method'] = code_challenge_method

        return url_join_args('%s/oidc/auth' % self.options.app_host, res)

    def build_authorize_url(
            self,
            redirect_uri=None,
            response_type=None,
            response_mode=None,
            state=None,
            nonce=None,
            scope=None,
            code_challenge_method=None,
            code_challenge=None,
            service=None
    ):
        """
        Generate an address link for user login.
        """
        if not self.options.app_host:
            raise ApprowWrongArgumentException('must provider app_host when you init AuthenticationClient')

        if self.options.protocol == 'oidc':
            return self.__build_oidc_authorize_url(
                response_mode=response_mode,
                response_type=response_type,
                redirect_uri=redirect_uri,
                state=state,
                nonce=nonce,
                scope=scope,
                code_challenge=code_challenge,
                code_challenge_method=code_challenge_method
            )
        elif self.options.protocol == 'oauth':
            return self.__build_oauth_authorize_url(
                scope=scope,
                redirect_uri=redirect_uri,
                state=state,
                response_type=response_type
            )
        elif self.options.protocol == 'saml':
            return self.__build_saml_authorize_url()

        elif self.options.protocol == 'cas':
            return self.__build_cas_authorize_url(service=service)

        else:
            raise ApprowWrongArgumentException('protocol must be oidc oauth saml or cas')

    def generate_code_challenge(self, length=43):
        """
        Generate a PKCE code challenge, the length must be greater than or equal to 43.

        Args:
            length (int): The default length of code challenge is 43.
        """
        if not isinstance(length, int):
            raise ApprowWrongArgumentException('length must be a int')

        if length < 43:
            raise ApprowWrongArgumentException('length must be grater than 43')

        return get_random_string(length)

    def generate_code_challenge_digest(self, code_challenge, method=None):
        """
        Generate a PKCE code challenge.

        Args:
            code_challenge (str): Generate a PKCE code challenge, the length must be greater than or equal to 43.
            method (str): It can be plain、S256.
        """
        if len(code_challenge) < 43:
            raise ApprowWrongArgumentException('code_challenge must be a string length grater than 43')

        if not method:
            method = 'S256'

        if method not in ['S256', 'plain']:
            raise ApprowWrongArgumentException('method must be S256 or plain')

        if method == 'S256':
            code_challenge = hashlib.sha256(code_challenge.encode('utf-8')).digest()
            code_challenge = base64.urlsafe_b64encode(code_challenge).decode('utf-8')
            code_challenge = code_challenge.replace('=', '')
            return code_challenge

        elif method == 'plain':
            return code_challenge

        else:
            raise ApprowWrongArgumentException('unsupported method, must be S256 or plain')

    def __build_oidc_logout_url(self, redirect_uri=None, id_token=None):
        if redirect_uri:
            return "%s/oidc/session/end?id_token_hint=%s&post_logout_redirect_uri=%s" % (
                self.options.app_host,
                id_token,
                redirect_uri
            )
        else:
            return "%s/oidc/session/end" % self.options.app_host

    def __build_easy_logout_url(self, redirect_uri=None):
        if redirect_uri:
            return "%s/login/profile/logout?post_logout_redirect_uri=%s" % (
                self.options.app_host,
                redirect_uri
            )
        else:
            return "%s/login/profile/logout" % (
                self.options.app_host
            )

    def __build_cas_logout_url(self, redirect_uri=None):
        if redirect_uri:
            return "%s/cas-idp/logout?url=%s" % (
                self.options.app_host,
                redirect_uri
            )
        else:
            return "%s/cas-idp/logout" % (
                self.options.app_host
            )

    def build_logout_url(self, expert=None, redirect_uri=None, id_token=None):
        """拼接登出 URL。"""
        if not self.options.app_host:
            raise ApprowWrongArgumentException('must provider app_host when you init AuthenticationClient')

        if self.options.protocol == 'oidc':
            if not expert:
                return self.__build_easy_logout_url(redirect_uri)
            else:
                return self.__build_oidc_logout_url(
                    id_token=id_token,
                    redirect_uri=redirect_uri
                )
        elif self.options.protocol == 'cas':
            return self.__build_cas_logout_url(redirect_uri=redirect_uri)

    def __get_new_access_token_by_refresh_token_with_client_secret_post(self, refresh_token):
        url = "%s/%s/token" % (self.options.host, 'oidc' if self.options.protocol == 'oidc' else 'oauth')
        data = self.restClient.request(
            method='POST',
            url=url,
            data={
                'client_id': self.options.app_id,
                'client_secret': self.options.secret,
                'grant_type': 'refresh_token',
                'refresh_token': refresh_token
            }
        )
        return data

    def __get_new_access_token_by_refresh_token_with_client_secret_basic(self, refresh_token):
        url = "%s/%s/token" % (self.options.host, 'oidc' if self.options.protocol == 'oidc' else 'oauth')
        data = self.restClient.request(
            method='POST',
            url=url,
            data={
                'grant_type': 'refresh_token',
                'refresh_token': refresh_token
            },
            basic_token=base64.b64encode(('%s:%s' % (self.options.app_id, self.options.secret)).encode()).decode()
        )
        return data

    def __get_new_access_token_by_refresh_token_with_none(self, refresh_token):
        url = "%s/%s/token" % (self.options.host, 'oidc' if self.options.protocol == 'oidc' else 'oauth')
        data = self.restClient.request(
            method='POST',
            url=url,
            data={
                'client_id': self.options.app_id,
                'grant_type': 'refresh_token',
                'refresh_token': refresh_token
            }
        )
        return data

    def get_new_access_token_by_refresh_token(self, refresh_token):
        """
        Refresh token Get new Access token by Refresh token.

        Args:
            refresh_token (str): Refresh token
                                Note: refresh_token only retures with offline_access.

        """
        if self.options.protocol not in ['oauth', 'oidc']:
            raise ApprowWrongArgumentException('protocol must be oauth or oidc')

        if not self.options.secret and self.options.token_endpoint_auth_method != 'none':
            raise ApprowWrongArgumentException('secret must be provided')

        if self.options.token_endpoint_auth_method == 'client_secret_post':
            return self.__get_new_access_token_by_refresh_token_with_client_secret_post(refresh_token)
        elif self.options.token_endpoint_auth_method == 'client_secret_basic':
            return self.__get_new_access_token_by_refresh_token_with_client_secret_basic(refresh_token)
        elif self.options.token_endpoint_auth_method == 'none':
            return self.__get_new_access_token_by_refresh_token_with_none(refresh_token)
        else:
            raise ApprowWrongArgumentException('unsupported argument token_endpoint_auth_method')

    def __revoke_token_with_client_secret_post(self, token):
        url = "%s/%s/token/revocation" % (self.options.host, 'oidc' if self.options.protocol == 'oidc' else 'oauth')
        return self.restClient.request(
            method='POST',
            url=url,
            data={
                'client_id': self.options.app_id,
                'client_secret': self.options.secret,
                'token': token
            }
        )

    def __revoke_token_with_client_secret_basic(self, token):
        url = "%s/%s/token/revocation" % (self.options.host, 'oidc' if self.options.protocol == 'oidc' else 'oauth')
        return self.restClient.request(
            method='POST',
            url=url,
            data={
                'token': token
            },
            basic_token=base64.b64encode(('%s:%s' % (self.options.app_id, self.options.secret)).encode()).decode()
        )

    def __revoke_token_with_none(self, token):
        url = "%s/%s/token/revocation" % (self.options.host, 'oidc' if self.options.protocol == 'oidc' else 'oauth')
        return self.restClient.request(
            method='POST',
            url=url,
            data={
                'client_id': self.options.app_id,
                'token': token
            }
        )

    def revoke_token(self, token):
        """
        Withdraw the Access token or Refresh token. Holders of Access token or Refresh token can notify Approw that the token is no longer needed, and hope that Approw will revoke it.
        Args:
            token (str): Access token or Refresh token can get from AuthenticationClient.get_access_token_by_code.
                        Note: refresh_token only retures with offline_access.
        """
        if self.options.protocol not in ['oauth', 'oidc']:
            raise ApprowWrongArgumentException('protocol must be oauth or oidc')

        if not self.options.secret and self.options.revocation_endpoint_auth_method != 'none':
            raise ApprowWrongArgumentException('secret must be provided')

        if self.options.revocation_endpoint_auth_method == 'client_secret_post':
            return self.__revoke_token_with_client_secret_post(token)

        elif self.options.revocation_endpoint_auth_method == 'client_secret_basic':
            return self.__revoke_token_with_client_secret_basic(token)

        elif self.options.revocation_endpoint_auth_method == 'none':
            return self.__revoke_token_with_none(token)

        else:
            raise ApprowWrongArgumentException('unsupported argument token_endpoint_auth_method')

    def __introspect_token_with_client_secret_post(self, token):
        url = "%s/%s/token/introspection" % (self.options.host, 'oidc' if self.options.protocol == 'oidc' else 'oauth')
        return self.restClient.request(
            method='POST',
            url=url,
            data={
                'client_id': self.options.app_id,
                'client_secret': self.options.secret,
                'token': token
            }
        )

    def __introspect_token_with_client_secret_basic(self, token):
        url = "%s/%s/token/introspection" % (self.options.host, 'oidc' if self.options.protocol == 'oidc' else 'oauth')
        return self.restClient.request(
            method='POST',
            url=url,
            data={
                'token': token
            },
            basic_token=base64.b64encode(('%s:%s' % (self.options.app_id, self.options.secret)).encode()).decode()
        )

    def __introspect_token_with_none(self, token):
        url = "%s/%s/token/introspection" % (self.options.host, 'oidc' if self.options.protocol == 'oidc' else 'oauth')
        return self.restClient.request(
            method='POST',
            url=url,
            data={
                'client_id': self.options.app_id,
                'token': token
            }
        )

    def introspect_token(self, token):
        """
        Check the status of Access token or Refresh token.

        Args:
            token (str): Access token or Refresh token can get from AuthenticationClient.get_access_token_by_code.
                        Note: refresh_token only retures with offline_access.
        """
        if self.options.protocol not in ['oauth', 'oidc']:
            raise ApprowWrongArgumentException('protocol must be oauth or oidc')

        if not self.options.secret and self.options.introspection_endpoint_auth_method != 'none':
            raise ApprowWrongArgumentException('secret must be provided')

        if self.options.introspection_endpoint_auth_method == 'client_secret_post':
            return self.__introspect_token_with_client_secret_post(token)

        elif self.options.introspection_endpoint_auth_method == 'client_secret_basic':
            return self.__introspect_token_with_client_secret_basic(token)

        elif self.options.introspection_endpoint_auth_method == 'none':
            return self.__introspect_token_with_none(token)

        else:
            raise ApprowWrongArgumentException('unsupported argument token_endpoint_auth_method')

    def __validate_id_token(self, id_token):
        url = "%s/api/v2/oidc/validate_token?id_token=%s" % (self.options.app_host, id_token)
        return self.restClient.request(
            method='GET',
            url=url,
        )

    def __validate_access_token(self, access_token):
        url = "%s/api/v2/oidc/validate_token?access_token=%s" % (self.options.app_host, access_token)
        return self.restClient.request(
            method='GET',
            url=url,
        )

    def validate_token(self, id_token=None, access_token=None):
        """
        Verifying the Id token or Access token through the online interface provided by Approw will generate a network request.
        Args:
            id_token (str):
            access_token (str): Access token. It can get from AuthenticationClient.get_access_token_by_code.
        """

        if not access_token and not id_token:
            raise ApprowWrongArgumentException('must provide id_token or access_token')

        if id_token:
            return self.__validate_id_token(id_token)
        elif access_token:
            return self.__validate_access_token(access_token)

    def validate_ticket_v1(self, ticket, service):
        """
        Verify the legality of CAS 1.0 Ticket.

        Args:
            ticket (str): After the certification process by CAS，Approw will issue a ticket。
            service (str): CAS callback address.
        """
        url = '%s/cas-idp/%s/validate?service=%s&ticket=%s' % (self.options.app_host, self.options.app_id, service, ticket)
        data = self.restClient.request(
            method='GET',
            url=url
        )
        raw_valid, username = data.split('\n')
        valid = raw_valid == 'yes'
        res = {
            'valid': valid
        }
        if username:
            res['username'] = username
        if not valid:
            res['message'] = 'ticket is not valid'
