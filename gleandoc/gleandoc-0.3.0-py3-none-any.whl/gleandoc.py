#!/usr/bin/env python3

"""See top level package docstring for documentation"""

import ast
import importlib
import logging
import os
import pathlib
import sys

myself = pathlib.Path(__file__).stem

# configure library-specific logger
logger = logging.getLogger(myself)
logging.getLogger(myself).addHandler(logging.NullHandler())

logging.basicConfig(level=logging.DEBUG)

########################################################################


def docstring(name=os.path.basename(os.getcwd())):
    """
    Return the doctring for a module

    - The default name is the basename of the current working directory
        - For example: if /var/tmp, name = 'tmp'
    - First try relative import in current directory
    - Then try general import (read docstring from installed package)

    Parameters
    ----------

    name : str or object, default=os.path.basename(os.getcwd())
        Name of entity from which to attempt docstring extraction

    Returns
    -------
    str, default=''
        The extracted docstring
    """
    logger.info(f"searching for docstring belonging to {name}")

    try:
        # logger.info(f"trying relative import in working directory...")
        # hit = importlib.import_module(name, package='.')
        # logger.info(f"relative import: loaded module from {hit.__file__}")
        # return hit.__doc__
        cwd = os.getcwd()
        python_file = f"{cwd}/{name}/__init__.py"
        logger.info(f"attempting abstract syntax tree parse: {python_file}")
        parsed = ast.parse(open(python_file).read())
        logger.info('abstract syntax tree parse succeeded')
        doc = ast.get_docstring(parsed)
        logger.info('retrieved docstring from abstract syntax tree')
        return doc
    except Exception as e:
        logger.info('failed parse')
        logger.debug(f"exception details: {e}")

    try:
        logger.info('trying general import...')
        hit = importlib.import_module(name)
        logger.info(f"general import: loaded module from {hit.__file__}")
        return hit.__doc__
    except ModuleNotFoundError as e:
        logger.info(f"failed general import of {name}")
        logger.debug(f"exception details: {e}")
    except AttributeError as e:
        logger.info(f"import succeeded for {name}")
        logger.info(f"however, {name} lacks __doc__ attribute")
        logger.debug(f"exception details: {e}")

    logger.info(f"unable to extract docstring for {name}")
    logger.info('returning empty string')
    return ''


def interpolate(input, output):
    """Interpolate docstring into template and write file"""

    try:
        template = open(input).read()
    except Exception:
        logger.error(f"failed reading {input}")
        sys.exit(1)
    try:
        doc = docstring()
        interpolated = template.format(**{'__doc__': doc})
    except Exception:
        logger.error(f"failed interpolating {input}")
        sys.exit(1)
    try:
        if os.path.exists(output):
            logger.warning(f"replacing {output}")
        open(output, 'wt').write(interpolated)
        logger.info(f"wrote {output}")
    except Exception:
        logger.error(f"failed writing {output}")
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
        logger.error('too many arguments\n')
        usage()
        sys.exit(1)


if __name__ == '__main__':
    main()
