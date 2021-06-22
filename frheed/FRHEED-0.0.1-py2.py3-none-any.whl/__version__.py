# Version change guidelines:
#   - Increment the MAJOR version when making incompatible API changes
#   - Increment the MINOR version when adding backwards-compatible functionality
#   - Increment the PATCH version when making backwards-compatible bug fixes
VERSION = (0, 0, 1)  # (MAJOR, MINOR, PATCH)
__version__ = ".".join(map(str, VERSION))