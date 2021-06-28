from .lambda_client import AbstractLambdaClient
from rest_framework.serializers import ValidationError


class UserInfoClient(AbstractLambdaClient):

    USER_INFO = 'user_info'
    USERNAME = 'username'
    GET_USER_POOL_INFO = 'get_user_pool_info'
    GET_USER_ATTRIBUTE_INFO = 'get_user_attribute_info'

    valid_triggers = [USERNAME, USER_INFO,
                      GET_USER_POOL_INFO, GET_USER_ATTRIBUTE_INFO]

    def __init__(self):
        super().__init__("us-east-2", "UserInfo", True, True)

    def get_user_info(self, unique_user_identifier):
        return super().invoke(self.USER_INFO, {
            "value": unique_user_identifier
        })['body']

    def get_username(self, unique_user_identifier):
        return super().invoke(self.USERNAME, {
            "value": unique_user_identifier
        })['body']['value']

    def get_user_pool_info(self):
        return super().invoke(self.GET_USER_POOL_INFO)['body']

    def get_user_attribute_info(self):
        return super().invoke(self.GET_USER_ATTRIBUTE_INFO)['body']

    def get_user_display_name(self, unique_user_identifier_or_user_info, fail_on_unknown: bool = False):
        name = ''
        
        if isinstance(unique_user_identifier_or_user_info, dict):
            user_info = unique_user_identifier_or_user_info
        else:
            user_info = self.get_user_info(unique_user_identifier_or_user_info)

        if 'first_name' in user_info and len(user_info['first_name']) > 0:
            name = user_info['first_name']
        
        if 'last_name' in user_info and len(user_info['last_name']) > 0:
            if len(name) > 0:
                name = name + " "

            name = name + user_info['last_name']

        if name != '':
            return name
        elif fail_on_unknown:
            raise ValidationError("User has invalid name")
        else:
            return "Unknown User"
