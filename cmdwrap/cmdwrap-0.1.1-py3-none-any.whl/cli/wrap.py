import sys
import os
import stat
import piest.file as pfile

def template(cmd):
    return f"""#!/usr/bin/env python3

import cmdwrap

BASE_CMD = {cmd}

ROUTING = {{
}}

if __name__ == '__main__':
    cmdwrap.main(ROUTING, BASE_CMD)

"""

def create_file(file_name, cmd):
    with open(file_name, 'w') as fd:
        pfile.add_xu(file_name)
        src = template(cmd)
        fd.write(src)

def main():
    if (argc := len(sys.argv)) > 1:
        file_name = sys.argv[1]

        if argc > 2:
            cmd = ' '.join(sys.argv[2:])
            cmd = f"'{cmd}'"
        else:
            cmd = None

        create_file(file_name, cmd)

