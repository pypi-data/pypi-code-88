from grpc import AuthMetadataPlugin

from . import AUTHORIZATION_HEADER, BASIC_AUTH_PREFIX
from base64 import b64encode


class BasicAuth(AuthMetadataPlugin):
    def __init__(self, username: str, password: str) -> None:
        encoded = b64encode(f"{username}:{password}".encode("UTF-8")).decode("UTF-8")
        self.auth_string = f"{BASIC_AUTH_PREFIX} {encoded}"

    def __call__(self, context, callback) -> None:  # noqa: ANN001
        """Implements authentication by passing metadata to a callback.

        Implementations of this method must not block.

        Args:
            context: An AuthMetadataContext providing information on the RPC that
            the plugin is being called to authenticate.
            callback: An AuthMetadataPluginCallback to be invoked either
            synchronously or asynchronously.
        """

        callback(((AUTHORIZATION_HEADER, self.auth_string),), None)
