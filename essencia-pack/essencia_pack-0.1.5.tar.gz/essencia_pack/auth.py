import sys
import uvicorn
import yaml
from starlette.authentication import (
    AuthenticationBackend, AuthenticationError, SimpleUser, UnauthenticatedUser,
    AuthCredentials
)
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.responses import PlainTextResponse
from starlette.routing import Route
import base64
import binascii
from starlette.applications import Starlette
from starlette.schemas import SchemaGenerator

schemas = SchemaGenerator(
    {"openapi": "3.0.0", "info": {"title": "Example API", "version": "1.0"}}
)


def openapi_schema(request):
    return schemas.OpenAPIResponse(request=request)


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

def list_users(request):
    """
    responses:
      200:
        description: A list of users.
        examples:
          [{"username": "tom"}, {"username": "lucy"}]
    """
    raise NotImplementedError()


def create_user(request):
    """
    responses:
      200:
        description: A user.
        examples:
          {"username": "tom"}
    """
    raise NotImplementedError()

async def homepage(request):
    if request.user.is_authenticated:
        return PlainTextResponse('Hello, ' + request.user.display_name)
    return PlainTextResponse('Hello, you')

routes = [
    Route("/", endpoint=homepage),
    Route("/users", endpoint=list_users, methods=[ "GET" ]),
    Route("/users", endpoint=create_user, methods=[ "POST" ]),
    Route("/schema", endpoint=openapi_schema, include_in_schema=False)
]

middleware = [
    Middleware(AuthenticationMiddleware, backend=BasicAuthBackend())
]

app = Starlette(routes=routes, middleware=middleware)


if __name__ == '__main__':
    assert sys.argv[-1] in ("run", "schema"), "Usage: auth.py [run|schema]"

    if sys.argv[-1] == "run":
        uvicorn.run("auth:app", host='0.0.0.0', port=8000)
    elif sys.argv[-1] == "schema":
        schema = schemas.get_schema(routes=app.routes)
        print(yaml.dump(schema, default_flow_style=False))