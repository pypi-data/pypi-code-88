C64_MAGIC = b'C64-TAPE-RAW'


def is_valid_image(filepath):
    with filepath.open('rb') as fileh:
        magic = fileh.read(len(C64_MAGIC))

    return magic == C64_MAGIC
