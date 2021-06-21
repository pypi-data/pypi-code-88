# no-redef: ignore
"""
File reader module.
"""

try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources


def get_file_contents(folder, filename: str) -> str:  # type: ignore
    """
    Reads the contents of a file and returns it.
    :param folder:
    :param filename:
    :return:
    """
    return pkg_resources.read_text(folder, filename)  # pylint: disable=broad-except
