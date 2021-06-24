import boto3


class AwsCognitoApi:

    def __init__(
            self,
            access_key=None,
            secret_key=None,
            region_name=None,
            verbose=False
    ):
        self._client = boto3.client(
            'cognito-idp',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region_name
        )
        self._verbose = verbose

    def get_user_access_token(self, client_id, user, password):
        auth_response = self._client.initiate_auth(
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': user,
                'PASSWORD': password
            },
            ClientId=client_id
        )

        auth_result = None
        if auth_response:
            auth_result = auth_response['AuthenticationResult']
        if auth_result:
            return auth_result['AccessToken']

        return ""
