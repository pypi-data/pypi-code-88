from importlib import metadata

try:
    from .celery import app as celery_app
except ModuleNotFoundError:
    # Celery is not available
    celery_app = None

try:
    __version__ = metadata.distribution("AlekSIS-Core").version
except Exception:
    __version__ = "unknown"

default_app_config = "aleksis.core.apps.CoreConfig"
