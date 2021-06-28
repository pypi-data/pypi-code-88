__version__ = "0.2.0"

__all__ = [
    "AWResourcesClient",
    "AWJobsClient",
    "AWCacheStoreClient",
]

try:
    # Attempts to import the client class
    # Allowed to fail importing so the package metadata can be read for building
    from .resource_client import AWResourcesClient
    from .cache_store_client import AWCacheStoreClient
    from .job_client import AWJobsClient
except (ImportError, ModuleNotFoundError):  # pragma: no cover
    pass  # pragma: no cover
