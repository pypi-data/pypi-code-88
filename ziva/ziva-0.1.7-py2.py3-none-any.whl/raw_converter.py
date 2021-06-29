import sys
from datetime import datetime
from jda_to_dtv import Jda2dtv
from comm_package import replace_repeating_chars, data_decompress


def save_data(data: bytes, filepath='test.jda', dtv=True) -> str:
    with open(filepath, 'wb') as f:
        f.write(data)
    print (f'Jda created: {filepath}')
    conv = Jda2dtv()
    conv.load_file(filepath)
    if dtv:
        conv.write_dtv_files(file_name=filepath.replace('.jda', ''))
    conv.write_dJ_file(file_name=filepath.replace('.jda', '.dJ'))
    return filepath.replace('.jda', '.dJ')


filepath = sys.argv[1]
with open(filepath, 'rb') as f:
    lines = f.readlines()

data = [eval(i) for i in lines]

# Get only data layer from packages. Strip address, confirmation code (e.g. @OT), crc, start-end sign
data_layer = b''
for package in data:
    package = replace_repeating_chars(package, reverse=True)
    package = package[package.find(b'@') + 3:-3]
    package = data_decompress(package)
    data_layer += package

# Split to header and body(actual data) and decompress header
header, body = data_layer.split(b'$HEADER END\r\n')
header = header.replace(b'\r\n', b'\n') + b'$HEADER END\n'

data = header + body
ts = datetime.strftime(datetime.now(), "%d%m%Y_%H%M")
filepath = f'{filepath}_{ts}.jda'
save_data(data, filepath=filepath)
