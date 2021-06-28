import os
import json
import torch
import numpy as np
import subprocess
from tqdm.auto import tqdm


def create_folders(folder):
    try:
        if not os.path.isdir(folder):
            path, fold = os.path.split(folder)
            if not os.path.isdir(path):
                create_folders(path)
            os.mkdir(folder)
    except Exception:
        pass


def list_gpus():
    """
    List of available GPUs
    """
    try:
        p = subprocess.Popen(
            [
                "nvidia-smi",
                "--query-gpu=index,memory.total,memory.used,name",
                "--format=csv,noheader,nounits",
            ],
            stdout=subprocess.PIPE,
        )
        (out, _) = p.communicate()
        gpusstr = str(out.decode("utf-8")).split("\n")
        gpus = list()
        if gpusstr:
            for gstr in gpusstr:
                if gstr != "":
                    attr = gstr.split(",")
                    gpu = {
                        "index": int(attr[0]),
                        "name": attr[3][1:],
                        "total": float(attr[1][1:]),
                        "used": float(attr[2][1:]),
                    }
                    gpus += [gpu]
    except Exception:
        gpus = [{"index": 0, "name": "CPU", "total": 1024.0, "used": 0.0}]

    return gpus


def parse_cuda(use_gpu):
    os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
    if len(use_gpu) == 1:
        use_parallel = False
        use_gpu = use_gpu[0]

        if use_gpu == -1:
            device = torch.device("cpu")
        else:
            device = torch.device("cuda:" + str(use_gpu))
    else:
        use_parallel = use_gpu
        device = torch.device("cuda:" + str(min(use_gpu)))

    return device, use_parallel


class AverageMeter(object):
    """Computes and stores the average and current value"""

    def __init__(self):
        self.reset()

    def reset(self):
        self.array = []
        self.val = 0
        self.total_avg = 0
        self.total_sum = 0
        self.total_count = 0

        self.avg = 0
        self.sum = 0
        self.count = 0

    def new_local(self):
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.array = self.array + [val]

        self.total_sum += val * n
        self.total_count += n
        if self.total_count > 50:
            self.total_avg = np.median(np.array(self.array[-50:]))
        else:
            self.total_avg = self.total_sum / self.total_count

        self.sum += val * n
        self.count += n
        self.avg = self.total_avg

    def load(self, narray, n=1):
        for val in narray:
            self.update(val, n)


class print_logger:
    def __init__(self):
        self.pbar = None

    def print(self, n, total, prefix, postfix):
        if self.pbar is None:
            self.pbar = tqdm()
        if n == 0:
            self.pbar.reset()
        self.pbar.total = total
        self.pbar.n = n
        self.pbar.set_description(desc=prefix, refresh=False)
        self.pbar.set_postfix(postfix, refresh=True)


class Decoder(json.JSONDecoder):
    def decode(self, s):
        result = super().decode(s)
        return self._decode(result)

    def _decode(self, o):
        if isinstance(o, str):
            try:
                return int(o)
            except ValueError:
                try:
                    return float(o)
                except ValueError:
                    return self.str_to_bool(o)
        elif isinstance(o, dict):
            return {k: self._decode(v) for k, v in o.items()}
        elif isinstance(o, list):
            return [self._decode(v) for v in o]
        else:
            return o

    def str_to_bool(self, s):
        if s == "True":
            return True
        elif s == "False":
            return False
        else:
            return s


def get_class(kls):
    parts = kls.split(".")
    module = ".".join(parts[:-1])
    m = __import__(module)
    for comp in parts[1:]:
        m = getattr(m, comp)
    return m
