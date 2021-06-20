"""Filex."""


def read(file_name):
    """Read."""
    with open(file_name, 'r') as fin:
        content = fin.read()
        fin.close()
        return content


def write(file_name, content, mode='w'):
    """Write."""
    with open(file_name, mode) as fout:
        fout.write(content)
        fout.close()
