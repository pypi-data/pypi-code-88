"""System utils."""
import os
import time

import subprocess
import psutil


def log_metrics():
    """Log system metrics.

    .. code-block:: python

        >>> from utils import sysx
        >>> print(sysx.log_metrics())
        {"ut": 1620724794.43984, "pid": 15129,
            "cpu_percent": 16.3, "vm_percent": 65.7}

    Note:
        Needs psutil

        .. code-block:: bash

            pip install psutil
    """
    log = {
        'ut': time.time(),
        'pid': os.getpid(),
        'cpu_percent': psutil.cpu_percent(),
        'vm_percent': psutil.virtual_memory().percent,
    }
    return log


def run(cmd):
    """Run commands.

    .. code-block:: python

        >>> from utils import sysx
        >>> print(sysx.run('echo "hello"'))
        ['hello']

    """
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, _) = process.communicate()
    return output.decode().split('\n')[:-1]


def str_color(output_str, color_code=31):
    """Wrap standard print command, to add color."""
    color_cmd = '\033[0;%dm' % (color_code)
    end_cmd = '\033[0m'
    return '%s%s%s' % (color_cmd, str(output_str), end_cmd)
