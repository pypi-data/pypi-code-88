from typing import Any

from us_libraries.client.base_client import BaseClient
from us_libraries.graphite import client_timing

service_name = "usf-auth-service"


class AuthClient(BaseClient):

    def __init__(self) -> None:
        super().__init__(service_name)

    @client_timing
    def login(self, username: str, password: str) -> Any:
        return self.post('login', username=username, password=password)

    @client_timing
    def has_permission(self, login_token: str, permission_id: int, permission_name: str) -> Any:
        return self.get(f'permission/has_permission?login_token={login_token}'
                        f'&permission_id={permission_id}&permission_name={permission_name}')

    @client_timing
    def logout(self, login_token: str) -> Any:
        return self.get('logout/%s' % login_token)

    @client_timing
    def send_otp(self, mobile_number: str) -> Any:
        return self.get('send_otp/%s' % mobile_number)

    @client_timing
    def check_otp(self, mobile_number: str, otp: str) -> Any:
        return self.get(f'check_otp?mobile_number={mobile_number}&otp={otp}')

    @client_timing
    def user_login_with_mobile_number(self, mobile_number: str) -> Any:
        return self.get(f'user_login_with_mobile_number?mobile_number={mobile_number}')

    @client_timing
    def user_sign_up(self,
                     auth_user_name: str = None,
                     auth_user_number: str = None,
                     auth_user_email: str = None,
                     auth_user_status: str = None,
                     auth_user_platform: str = None,
                     auth_user_password: str = None) -> Any:
        return self.post('user_sign_up',
                         auth_user_name=auth_user_name,
                         auth_user_number=auth_user_number,
                         auth_user_email=auth_user_email,
                         auth_user_status=auth_user_status,
                         auth_user_platform=auth_user_platform,
                         auth_user_password=auth_user_password)
