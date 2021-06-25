import os
import re
from itertools import chain

from Alexandria.general.project import root


def find_file(extension, path=None):
    """
    :param extension: File extension
    :param path: root/path
    :return: Single file.extension in folder
    """
    r = re.compile(f'.*{extension}?')
    tgt = os.path.join(root(), path) if not isinstance(path, type(None)) else root()
    print(tgt)
    matches = list((filter(r.match, list(chain.from_iterable(chain.from_iterable(os.walk(tgt)))))))
    paths = list(map(lambda x: os.path.join(str(root()), x).replace("\\", "/"), matches))
    return paths
