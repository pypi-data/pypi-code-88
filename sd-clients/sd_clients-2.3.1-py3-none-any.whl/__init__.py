__version__ = "2.3.1"

__all__ = ["ServiceDirectoryClient", "ApiGatewayProvider", "ClientStore"]

try:
    # Attempts to import the client class
    # Allowed to fail importing so the package metadata can be read for building
    from .api_gateway_client import ApiGatewayProvider
    from .service_directory_client import ServiceDirectoryClient
    from .client_store import ClientStore
except (ImportError, ModuleNotFoundError):  # pragma: no cover
    pass  # pragma: no cover
