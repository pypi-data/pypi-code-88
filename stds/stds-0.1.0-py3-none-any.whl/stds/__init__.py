__version__ = "0.1.0"
__doc__ = """
This is a small package that provides 3 high-level APIs to interact elegantly with stdin, stdout and stderr:

    - stdin
    - stderr
    - stdout

You can use it as such:

if __name__ == "__main__":
    stdin | print
    "This prints out stuff on stdout" | stdout
    "This prints out stuff on stderr" | stderr
"""

import io
from sys import stdin as stdin_fd, stderr as stderr_fd, stdout as stdout_fd


class STDWrapper:
    def __init__(self, fd):
        self.fd: io.TextIOWrapper = fd

    def __or__(self, other):
        return other.__call__(str(self))

    def __ror__(self, other):
        if not self.fd.writable():
            raise ValueError(f"{self.fd.name} is not writable")
        return self.fd.write(other)

    def __str__(self):
        if self.fd.readable():
            return self.fd.read()
        return self.fd.name


stdin = STDWrapper(stdin_fd)
stdout = STDWrapper(stdout_fd)
stderr = STDWrapper(stderr_fd)