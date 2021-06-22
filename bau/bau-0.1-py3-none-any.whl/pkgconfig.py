from .util import run
from .rule import rule

def pkg_config(*args):
    return run(['pkg-config', *args], capture_output=True) \
        .decode('utf-8').split()

@rule
def cflags(output, libs):
    return [arg for lib in libs
                for arg in pkg_config('--cflags', lib)]

@rule
def ldflags(output, libs):
    return [arg for lib in libs
                for arg in pkg_config('--libs', lib)]
