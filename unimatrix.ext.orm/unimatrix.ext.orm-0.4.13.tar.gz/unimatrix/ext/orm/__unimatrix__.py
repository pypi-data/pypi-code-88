"""Specifies entrypoint operations for Unimatrix integration."""
from . import destroy_engines


# Provides a hint to unimatrix.runtime.boot.shutdown()
# to indicate when this module should run.
WEIGHT = 1000


def on_teardown(*args, **kwargs):
    destroy_engines()
