from pathlib import Path


__version__ = '0.1.1'
_ENCODING = 'utf-8'


def write(file, s, overwrite=True):
    """ Open file for write mode, write string into it, and close.

    Write string to a file in ``utf-8`` encoding.

    If the file already exists, overwrite that by default,
    or FileExistsError if overwrite parameter set to False.

    Parameters
    ----------
    file: str or os.PathLike
        File to write to.
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
        Could not open or create file due to permission problem.
    IsADirectoryError
        A value specified to file parameter was a directory.
    TypeError
        Illegal type of parameter specified.
    """
    with open(file, 'w', encoding=_ENCODING) as writer:
        writer.write(s)


def append(file, s):
    raise NotImplemented()


def prepend(file, s):
    raise NotImplemented()


def insert(file, s, position):
    raise NotImplemented()


def read(file, silent=False):
    """ Open file for read mode, read string from it, and close.

    Read string from a file with the assumption that it is encoded in ``utf-8``.

    If the file not exists, raise FileNotFoundError, or get empty string as return value
    if silent parameter set to True.

    Parameters
    ----------
    file: str or os.PathLike
        File to read from.
    silent: bool, default=False
        If set to True, read empty string when file not exists.
        If set to False, raise FileNotFoundError when file not exists.

    Returns
    -------
    str
        Read string.

    Raises
    ------
    FileNotFoundError
        File is not exist and silent parameter set to False.
    PermissionError
        Could not open or create file due to permission problem.
    IsADirectoryError
        A value specified to file parameter was a directory.
    TypeError
        Illegal type of parameter specified.
    """
    file = Path(file)
    if not file.exists():
        if silent:
            return ''
        else:
            raise FileNotFoundError(str(file))

    with open(file, encoding=_ENCODING) as reader:
        return reader.read()
