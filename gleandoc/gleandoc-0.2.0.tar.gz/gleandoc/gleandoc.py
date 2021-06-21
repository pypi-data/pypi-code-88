#!/usr/bin/env python3

"""
Simple convenience function to extract docstring

See top level package docstring for documentation
"""

import os
import pathlib
import sys

myself = pathlib.Path(__file__).stem

sys.path.append('.')

########################################################################


def docstring(name=os.path.basename(os.getcwd())):
    """
    Return the doctring for a module or object

    - The default name is the basename of the current working directory
        - For example: if /var/tmp, name = 'tmp'

    Parameters
    ----------

    name : str or object, default=os.path.basename(os.getcwd())
        Name of entity from which to attempt docstring extraction

    Returns
    -------
    str, default=''
        The extracted docstring
    """
    doc = ''
    try:
        exec(f"import {name}")
    except Exception:
        print(f"{myself}: no module {name} (moving on)", file=sys.stderr)
    if name in locals() and hasattr(locals()[name], '__doc__'):
        doc = locals()[name].__doc__
    else:
        print(f"{myself}: {name} has no __doc__ element", file=sys.stderr)

    return doc


def interpolate(input, output):
    """Interpolate docstring into template and write file"""

    try:
        template = open(input).read()
    except Exception:
        print(f"{myself}: ERROR: failed reading {input}", file=sys.stderr)
        sys.exit(1)
    try:
        doc = docstring()
        interpolated = template.format(**{'__doc__': doc})
    except Exception:
        print(f"{myself}: error interpolating {input}", file=sys.stderr)
        sys.exit(1)
    try:
        if os.path.exists(output):
            print(f"{myself}: WARNING: replacing {output}", file=sys.stderr)
        open(output, 'wt').write(interpolated)
        print(f"{myself}: INFO: wrote {output}", file=sys.stderr)
    except Exception:
        print(f"{myself}: ERROR: failed writing {output}", file=sys.stderr)
        sys.exit(1)


def usage():
    usagemsg = f"""Usage: {myself} [-h] [NAME]
Extract docstring from module [NAME]

  -h, --help            show this help message and exit

- If unspecified, NAME defaults to the basename of the current directory
- This is designed for use in build systems to construct README files

Alternative two argument usage: {myself} TEMPLATE README
Interpolate docstring into TEMPLATE and write results to README

- In this mode, always derives NAME from basename of current directory
- Template uses style similar to f-string
- Supported variables which will be interpolated include: {{__doc__}}
- For literal (single) braces, use double braces: {{{{ or }}}}
"""
    print(usagemsg)


def main():
    # intentionally avoiding libraries to keep complexity down
    if len(sys.argv) == 1:
        print(docstring())
    elif len(sys.argv) == 2:
        argv1 = sys.argv[1]
        if argv1 == '-h' or argv1 == '--help':
            usage()
            sys.exit(0)
        else:
            print(docstring(name=argv1))
    elif len(sys.argv) == 3:
        interpolate(input=sys.argv[1], output=sys.argv[2])
    else:
        print(f"{myself}: ERROR: too many arguments\n", file=sys.stderr)
        usage()
        sys.exit(1)


if __name__ == '__main__':
    main()
