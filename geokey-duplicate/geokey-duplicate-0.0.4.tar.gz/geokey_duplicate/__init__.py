from geokey.extensions.base import register


VERSION = (0, 0, 4)
__version__ = '.'.join(map(str, VERSION))

register(
    'geokey_duplicate',
    'Duplicate',
    display_admin=True,
    superuser=False,
    version=__version__
)
