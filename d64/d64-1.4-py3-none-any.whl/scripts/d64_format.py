import argparse
import sys

from pathlib import Path

from d64.d64_image import D64Image
from d64.d71_image import D71Image
from d64.d80_image import D80Image
from d64.d81_image import D81Image
from d64.d82_image import D82Image


CREATE_METHODS = {
    'd64': D64Image.create,
    'd71': D71Image.create,
    'd80': D80Image.create,
    'd81': D81Image.create,
    'd82': D82Image.create
}


def main():
    parser = argparse.ArgumentParser(description='Create empty Commodore disk images.')
    parser.add_argument('label', help='disk label')
    parser.add_argument('id', help='disk identifier')
    parser.add_argument('filename', type=Path, help='image filename')
    parser.add_argument('--type', default='d64', choices=CREATE_METHODS.keys(), help='image type')
    parser.add_argument('--force', action='store_true', help='overwrite existing image')
    args = parser.parse_args()

    if args.filename.exists():
        if args.force:
            args.filename.unlink()
        else:
            sys.exit("{!s} already exists".format(args.filename))
    print("Creating empty disk image as {!s}, {}:{}, type {}".format(args.filename, args.label, args.id, args.type))

    CREATE_METHODS[args.type](args.filename, args.label.encode(), args.id.encode())
