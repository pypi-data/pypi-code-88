#   coding: utf-8
#   This file is part of DancingCell.

#   DancingCell is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Lesser General Public License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = "2020/06/19"

import bz2
import gzip
import zipfile
import io
from pathlib import Path


def clean_lines(string_list, remove_empty_lines=True, remove_return=True):
    """
    Strips whitespace, carriage returns and empty lines from a list of strings.

    Args:
        string_list: List of strings
        remove_empty_lines: Set to True to skip lines which are empty after stripping.
        remove_return:

    Returns: Iterator of clean strings with no whitespaces and no carriage return.

    """

    for s in string_list:
        clean_s = s
        if '#' in s:
            ind = s.index('#')
            clean_s = s[:ind]
        clean_s = clean_s.strip()

        if remove_return:
            clean_s = clean_s.replace('\n', '')

        if (not remove_empty_lines) or clean_s != '':
            yield clean_s


def gopen(filename, *args, **kwargs):
    """
    This function contains bz2, gzip and standard python open
    for intelligent processing of bzip, gzip or standard text function files

    Args:
        filename: (str or Path) filename or pathlib.Path.
        *args: Standard args for python open(..).
                E.g. mode: 'r' for read, 'w' for write.
        **kwargs: kwargs for python open

    Returns: File-like object. Supports with context.

    """

    filename = Path(filename)
    suf = filename.suffix.upper()
    if suf == ".BZ2":
        return bz2.open(filename, *args, **kwargs)
    elif suf in (".GZ", ".Z", ".TAR"):
        return gzip.open(filename, *args, **kwargs)
    elif suf == ".ZIP":
        allfile = zipfile.ZipFile(filename)
        index = kwargs.get('index', 0)
        return allfile.open(allfile.filelist[index])
    else:
        return io.open(filename, *args, **kwargs)
