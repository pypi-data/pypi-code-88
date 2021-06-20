#   coding:utf-8
#   This file is part of Alkemiems.
#
#   Alkemiems is free software: you can redistribute it and/or modify
#   it under the terms of the MIT License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = '2021/01/14 17:44:23'

import os


def which(cmd):
    """
    Returns full path to a executable.

    Args:
        cmd (str): Executable command to search for.

    Returns:
        (str) Full path to command. None if it is not found.

    Example::

        full_path_to_python = which("python")
    """
    def is_exe(fp):
        return os.path.isfile(fp) and os.access(fp, os.X_OK)

    fpath, fname = os.path.split(cmd)
    if fpath:
        if is_exe(cmd):
            return cmd
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, cmd)
            if is_exe(exe_file):
                return exe_file
    return None


def echo(cmd):
    """
    Returns full path to a PATH.

    Args:
        cmd (str): Executable command to search for.

    Returns:
        (str) Full path to command. None if it is not found.

    Example::

        full_path_to_python = which("python")
    """
    
    return os.getenv(cmd.replace('$', ''), None)

