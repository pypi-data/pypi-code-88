import os
import os.path as osp
from shutil import rmtree


def mkdir_or_exist(dir_name, mode=0o777, is_delete=True):
    if dir_name == '':
        return

    if os.path.exists(dir_name) and is_delete:
        rmtree(dir_name)
    dir_name = osp.expanduser(dir_name)
    os.makedirs(dir_name, mode=mode, exist_ok=True)


def clear_directory(dir_path:str):
    rmtree(dir_path)
    os.mkdir(dir_path)
