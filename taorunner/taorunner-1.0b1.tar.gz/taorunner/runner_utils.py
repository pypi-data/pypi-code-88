# Author: Botao Yu
import time
import hashlib


def get_command_and_update_command_file(command_file):
    with open(command_file, 'r') as f:
        lines = f.readlines()

    current_command = None
    current_line_idx = None
    for idx, line in enumerate(lines):
        line_strip = line.strip()
        if line_strip == '':
            continue
        current_command = line.rstrip('\n')
        current_line_idx = idx
        break

    if current_line_idx is not None:
        with open(command_file, 'w') as f:
            f.writelines(lines[current_line_idx + 1:])

    return current_command


def get_time_str():
    local_time = time.localtime()
    return time.strftime("%Y-%m-%d %H:%M:%S", local_time)


def get_md5_value(src, length=5):
    hash_object = hashlib.md5(str(src).encode('utf-8'))
    return hash_object.hexdigest()[:length]

