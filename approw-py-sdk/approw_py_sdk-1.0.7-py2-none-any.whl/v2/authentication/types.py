from ..exceptions import ApprowException


def DEFAULT_ONERROR(code, message):
    raise ApprowException(code=code, errmsg=message)


DEFAULT_ENCRYPT_PUBLICKEY = """
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC4xKeUgQ+Aoz7TLfAfs9+paePb
5KIofVthEopwrXFkp8OCeocaTHt9ICjTT2QeJh6cZaDaArfZ873GPUn00eOIZ7Ae
+TiA2BKHbCvloW3w5Lnqm70iSsUi5Fmu9/2+68GZRH9L7Mlh8cFksCicW2Y2W2uM
GKl64GDcIq3au+aqJQIDAQAB
-----END PUBLIC KEY-----
"""


class AuthenticationClientOptions:
    def __init__(
        self,
        app_id=None,
        app_host=None,
        user_pool_id=None,
        token=None,
        host=None,
        enc_public_key=None,
        on_error=None,
        timeout=10.0,
        lang=None,
        websocket_host=None,
        protocol=None,
        secret=None,
        token_endpoint_auth_method=None,
        introspection_endpoint_auth_method=None,
        revocation_endpoint_auth_method=None,
        redirect_uri=None
    ):

        """
        Initialize AuthenticationClient parameters

        Args:
            app_id (str): app ID
            app_host (str): app host, exp: https://your-app.approw.com
            token (str): user id_token，You can use id_token to initialize the SDK to achieve the purpose of remembering login
            enc_public_key (str): asymmetric encryption public key (optional), if you are using Approw public cloud service, you can ignore it; if you are using a privatized deployment of Approw, please contact the Approw IDaaS service administrator
            timeout (int): Request timeout time.The default is 10000ms (10 seconds).
            lang (str): The interface Message returns the language format (optional), the optional values are zh-CN and en-US, and the default is zh-CN.
            websocket_host (str): Approw Websocket Server domain name, if not filled in, it will default to http(s)://ws.YOUR_APPROW_SERVER.
            protocol (str): protocol type: oidc、oauth、saml、cas
            secret (str): key
            token_endpoint_auth_method (str): Get the token endpoint verification method: client_secret_post、client_secret_basic、none，默认为 client_secret_post.
            introspection_endpoint_auth_method (str): Verify the token endpoint verification method: `client_secret_post`、`client_secret_basic`、`none`，the default is `client_secret_post`.
            revocation_endpoint_auth_method (str): Withdraw token endpoint verification method: `client_secret_post`、`client_secret_basic`、`none`，默认为 `client_secret_post`.
            redirect_uri (str): callback URL
        """
        if not app_id and not user_pool_id:
            raise Exception('Please provide app_id or user_pool_id')

        self.app_id = app_id
        self.user_pool_id = user_pool_id
        self.host = app_host or host or "https://core.approw.com"
        self.app_host = app_host
        self.on_error = on_error or DEFAULT_ONERROR
        self.timeout = timeout
        self.graphql_endpoint = "%s/graphql/v2" % self.host
        self.enc_public_key = enc_public_key or DEFAULT_ENCRYPT_PUBLICKEY
        self.token = token
        self.lang = lang
        self.websocket_host = websocket_host
        self.protocol = protocol or 'oidc'
        self.secret = secret
        self.token_endpoint_auth_method = token_endpoint_auth_method
        self.introspection_endpoint_auth_method = introspection_endpoint_auth_method
        self.revocation_endpoint_auth_method = revocation_endpoint_auth_method
        self.redirect_uri = redirect_uri
