import os
from os.path import join


def _rcpath():
    home = os.environ.get('HOME')
    shell = os.environ.get('SHELL')
    shellrc = f".{shell.split('/')[-1]}rc"
    rcpath = join(home,shellrc)
    return rcpath


def _delete_changes(variable):
    rc = ''
    with open(_rcpath(), 'r') as file:
        for line in file:
            if line.startswith('export') and variable in line.lstrip('export ').split('=')[0]:
                continue
            elif line.startswith('unset') and variable in line.lstrip('unset '):
                continue
            rc += line
    with open(_rcpath(), 'w') as file:
        file.write(rc)


def setenv(variable: str, value: str) -> None:
    """
    set system Environment Variable
    example: envset('TESTVARIABLE', 'TESTVALUE')
    """
    if variable and type(variable) == str and type(value) == str:
        _delete_changes(variable)
        cmd = f'export \"{variable}\"=\"{value}\"'
        with open(_rcpath(), 'a') as file:
            file.write(f'\n{cmd}')
        os.environ[variable]=value
    else:
        raise ValueError('use help(setenv)')


def unsetenv(variable: str) -> None:
    """
    unset system Environment Variable
    example: envunset('TESTVARIABLE')
    """
    if variable and type(variable) == str:
        _delete_changes(variable)
        cmd = f'unset \"{variable}\"'
        with open(_rcpath(), 'a') as file:
            file.write(f'\n{cmd}')
        try:
            os.environ.pop(variable)
        except KeyError:
            pass
    else:
        raise ValueError('use help(unsetenv)')
