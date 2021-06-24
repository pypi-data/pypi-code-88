__version__ = '0.1.0'
from pathlib import Path


def write(file, s, overwrite=True):
    """ Open file for write mode, write string into it, and close.

    Write string to a file in encoding ``utf-8``.

    If the file already exists, overwrite that by default,
    or FileExistsError on overwrite=False.



    Parameters
    ----------
    file: str or pathlib.Path
    s: str
        A string to write to file.
    overwrite: bool, default=True
        Overwrite file with s, instead of raise FileExistsError.
        The default value is True, so you should specify this parameter to False
        if you want to use this function safely.

    Returns
    -------
    int
        Character count that were written to file.

    Raises
    ------
    FileExistsError:
        If file already exists and overwrite set to False.
    PermissionError
        If can not open or create file due to permission problem.
    """
    with open(file, 'w', encoding='utf-8') as writer:
        writer.write(s)


def append(file, s):
    raise NotImplemented()


def prepend(file, s):
    raise NotImplemented()


def insert(file, s, position):
    raise NotImplemented()


def read(file):
    raise NotImplemented()
