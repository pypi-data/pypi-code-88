import os


def setenv(variable: str, value: str) -> None:
    """
    set system Environment Variable
    example: envset('TESTVARIABLE', 'TESTVALUE')
    """
    if variable and type(variable) == str and type(value) == str:
        os.system(f'setx \"{variable}\" \"{value}\" > nul')
        os.environ[variable]=value
    else:
        raise ValueError('use help(setenv)')


def unsetenv(variable: str) -> None:
    """
    unset system Environment Variable
    example: envunset('TESTVARIABLE')
    """
    if variable and type(variable) == str:
        os.system(f'setx \"{variable}\" \"\" > nul')
        os.system(f'reg delete HKCU\Environment /F /V \"{variable}\" > nul')
        try:
            os.environ.pop(variable)
        except KeyError:
            pass
    else:
        raise ValueError('use help(unsetenv)')
