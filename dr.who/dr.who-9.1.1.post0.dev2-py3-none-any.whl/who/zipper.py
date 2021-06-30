# encoding: utf-8


'''Some zipfile testing.'''

import os, sys, tempfile, zipfile


def main():
    if len(sys.argv) != 2:
        print('🚨 Usage: DIRNAME', file=sys.stderr)
        sys.exit(1)
    fd, tmpFileName = tempfile.mkstemp('.zip')
    with zipfile.ZipFile(os.fdopen(fd, 'wb'), 'w') as zf:
        for folder, subdirs, filenames in os.walk(sys.argv[1]):
            for fn in filenames:
                path = os.path.join(folder, fn)
                if os.path.isfile(path):
                    zf.write(path, path[len(sys.argv[1]) + 1:])
        zf.close()
    print(tmpFileName)


if __name__ == '__main__':
    main()
