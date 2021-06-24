# ***************************************************************
# Copyright (c) 2021 Jittor. All Rights Reserved.
# Maintainers:
#   Dun Liang <randonlang@gmail.com>.
#   Meng-Hao Guo <guomenghao1997@gmail.com>
#
#
# This file is subject to the terms and conditions defined in
# file 'LICENSE.txt', which is part of this source code package.
# ***************************************************************
__version__ = '1.0.0.0'
import pickle
import hashlib
import sys, os
from .utils import LOG, cache_path
ck_path = os.path.join(cache_path, "checkpoints")

def make_cache_dir(cache_path):
    if not os.path.isdir(cache_path):
        LOG.i(f"Create cache dir: {cache_path}")
        os.mkdir(cache_path)

make_cache_dir(ck_path)

def safepickle(obj, path):
    # Protocol version 4 was added in Python 3.4. It adds support for very large objects, pickling more kinds of objects, and some data format optimizations.
    # ref: <https://docs.python.org/3/library/pickle.html>
    s = pickle.dumps(obj, 4)
    checksum = hashlib.sha1(s).digest()
    s += bytes(checksum)
    s += b"HCAJSLHD"
    with open(path, 'wb') as f:
        f.write(s)

def safeunpickle(path):
    if path.startswith("rcthub://"):
        path = path.replace("rcthub://", "http://192.168.0.175:8100/rct/checkpoints/")
    if path.startswith("https:") or path.startswith("http:"):
        base = path.split("/")[-1]
        fname = os.path.join(ck_path, base)
        from utils.misc import download_url_to_local
        download_url_to_local(path, base, ck_path, None)
        path = fname
    with open(path, "rb") as f:
        s = f.read()
    if not s.endswith(b"HCAJSLHD"):
        return pickle.loads(s)
    checksum = s[-28:-8]
    s = s[:-28]
    if hashlib.sha1(s).digest() != checksum:
        raise ValueError("Pickle checksum does not match! path: "+path)
    return pickle.loads(s)

def sync_model(path, network='local', host_port='192.168.0.175:8100'):
    if network=='local':
        host_port = '192.168.0.175:8100'
    else:#internet
        host_port = '121.89.245.64:8100'
    if path.startswith("rcthub://"):
        path = path.replace("rcthub://", "http://"+host_port+"/rct/checkpoints/")
    if path.startswith("https:") or path.startswith("http:"):
        base = path.split("/")[-1]
        fname = os.path.join(ck_path, base)
        from utils.misc import download_url_to_local
        download_url_to_local(path, base, ck_path, None)
        path = fname
    return path