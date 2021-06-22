import re
import subprocess

from . import rule
from .util import Colors, ensure_dir, info, run

import os

def parse_deps(path):
    with open(path) as f:
        deps = f.read().replace("\\\n", "")
        deps = re.sub(r'[^:]*:', "", deps)
        return deps.split()

@rule
def object(output, cflags, src):
    base, ext = os.path.splitext(src)
    out = os.path.join(output.dir, base + '.o')
    ensure_dir(out)
    dep_file = os.path.join(output.dir, base + '.d')
    info(f'[cc] {src}')
    run(['gcc'] + cflags + ['-MD', '-c', '-o', out, src])
    output.add_file(out)
    for dep in parse_deps(dep_file):
        output.add_file(dep)

    return out

@rule
def link(output, exe, ldflags, *objs):
    info(f'[ld] {exe}')
    exe = os.path.join(output.dir, exe)
    deps = run(['gcc', '-Wl,--trace'] + ldflags + ['-o', exe] + list(objs),
               stdout=subprocess.PIPE).decode('utf-8').splitlines()
    for dep in deps:
        output.add_file(dep)
    output.add_file(exe)
    return exe

