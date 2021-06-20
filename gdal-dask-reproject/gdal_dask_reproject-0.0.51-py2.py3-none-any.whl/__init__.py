try:
    from .version import __version__
except ImportError:
    __version__ = "unknown"

try:
    from .warp import reproject  # noqa: F401
except ImportError as e:
    raise ImportError(f"{e}:\n can't find module")
