import os
import stat


def add_xu(fn: str) -> None:
    os.chmod(fn, os.stat(fn).st_mode | stat.S_IXUSR)
