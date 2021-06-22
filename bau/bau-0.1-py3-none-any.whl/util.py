import hashlib
import os
import subprocess

class Colors:
    BOLD = "\x1b[1;37m"
    GREEN = "\x1b[32m"
    YELLOW = "\x1b[33m"
    RED = "\x1b[31m"
    BOLD_RED = "\x1b[1;31m"
    RESET = "\x1b[0m"


def sources(output, dir, ext):
    for root, dirs, files in os.walk(dir):
        for path in files:
            path = os.path.join(dir, root, path)
            base, ext1 = os.path.splitext(path)
            if ext1 == ext:
                yield os.path.relpath(path, dir)

def ensure_dir(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

def info(*args):
    message(Colors.BOLD, *args)

def error(*args):
    message(Colors.BOLD_RED, *args)

def message(col, *args):
    print(col, end='')
    print(*args, end='')
    print(Colors.RESET, end='')
    print()

def run(args, **opts):
    return subprocess.run(args, check=True, **opts).stdout

def sha256sum(filename):
    if not os.path.exists(filename): return None
    h = hashlib.sha256()
    b = bytearray(128 * 1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        for n in iter(lambda: f.readinto(mv), 0):
            h.update(mv[:n])
    return h.digest()

