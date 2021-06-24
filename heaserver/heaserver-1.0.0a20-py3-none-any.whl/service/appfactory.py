from aiohttp import web, TCPConnector
from heaserver.service import appproperty, requestproperty
from typing import AsyncGenerator


@web.middleware
async def new_wstl_builder(request: web.Request, handler) -> web.Response:
    wstl_builder_factory = request.app[appproperty.HEA_WSTL_BUILDER_FACTORY]
    request[requestproperty.HEA_WSTL_BUILDER] = wstl_builder_factory()
    response = await handler(request)
    return response


def new_app() -> web.Application:
    """
    Creates and returns an aiohttp Application object. Installs middleware that sets the HEA_WSTL_BUILDER request
    property, and also sets the HEA_CONNECTOR application property. Assumes that the HEA_WSTL_BUILDER_FACTORY app
    property has already been set.

    :return: the Application property.
    """
    app = web.Application(middlewares=[new_wstl_builder])
    app.cleanup_ctx.append(_connector)
    return app


async def _connector(app: web.Application) -> AsyncGenerator:
    """
    Manages connection pool for connecting to other services.

    :param app: the aiohttp application.
    """
    app[appproperty.HEA_CONNECTOR] = TCPConnector()
    yield
    await app[appproperty.HEA_CONNECTOR].close()
