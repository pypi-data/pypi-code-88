import os


def text_stream(txt):
    if txt is None:
        return open(os.devnull, 'w')
    if isinstance(txt, str):
        return open(str, 'w')
    return txt  # assume this is a stream
