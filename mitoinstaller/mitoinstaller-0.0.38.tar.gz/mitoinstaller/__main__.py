"""
The Mito Installer package contains utils for installing
Mito within your Python enviornment.

Long term, we aim to meet:
1. This package has minimal dependencies, both for speed of download and the ultimate portability.
2. The installation attempts to fail as early as possible, and to give the user as much help
   help as possible while doing so.
"""
from mitoinstaller.install import do_install_or_upgrade

def main():
    """
    The main function of the Mito installer, this function is responsible
    for either installing mitosheet or upgrading mitosheet.

    To install Mito (for the first time):
    python -m mitoinstaller install

    To upgrade Mito:
    python -m mitoinstaller upgrade
    """
    import sys

    if len(sys.argv) > 1:
        command = sys.argv[1]
    else:
        command = ''

    if command == 'install':
        do_install_or_upgrade('install')
    elif command == 'uninstall':
        print('To uninstall, run `pip uninstall mitosheet` and `pip uninstall mitosheet3`')
    elif command == 'upgrade':
        do_install_or_upgrade('upgrade')
    else:
        print('\nProper usage is `python -m mitoinstaller install` or `python -m mitoinstaller upgrade`\n\nTry running the command `python -m mitoinstaller install`\n')
 

if __name__ == '__main__':
    main()