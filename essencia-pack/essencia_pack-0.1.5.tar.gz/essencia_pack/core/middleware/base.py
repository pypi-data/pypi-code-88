from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.authentication import (
    AuthenticationBackend, AuthenticationError, SimpleUser, UnauthenticatedUser,
    AuthCredentials
)
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware
import base64
import binascii


class BasicAuthBackend(AuthenticationBackend):
    async def authenticate(self, request):
        if "Authorization" not in request.headers:
            return

        auth = request.headers["Authorization"]
        try:
            scheme, credentials = auth.split()
            if scheme.lower() != 'basic':
                return
            decoded = base64.b64decode(credentials).decode("ascii")
        except (ValueError, UnicodeDecodeError, binascii.Error) as exc:
            raise AuthenticationError('Invalid basic auth credentials')

        username, _, password = decoded.partition(":")
        # TODO: You'd want to verify the username and password here.
        return AuthCredentials(["authenticated"]), SimpleUser(username)


# PROJECT IMPORTS

base_middleware = [
    Middleware(SessionMiddleware,
               secret_key=str(settings.SESSION_SECRET),
               session_cookie=settings.SESSION_COOKIE),
    Middleware(AuthenticationMiddleware, backend=BasicAuthBackend()),
    Middleware(CORSMiddleware,
               allow_origins=settings.ALLOW_ORIGINS,
               allow_headers=settings.ALLOW_HEADERS,
               allow_methods=settings.ALLOW_METHODS,
               allow_origin_regex=settings.ALLOW_ORIGIN_REGEX,
               allow_credentials=settings.ALLOW_CREDENTIALS,
               expose_headers=settings.EXPOSE_HEADERS),
    Middleware(TrustedHostMiddleware,
               allowed_hosts=settings.ALLOWED_HOSTS),
]
