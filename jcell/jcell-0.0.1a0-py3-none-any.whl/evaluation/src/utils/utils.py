import subprocess
import torch
import os
import json
import numpy as np


def create_folders(folder):
    if not os.path.isdir(folder):
        path, fold = os.path.split(folder)
        if not os.path.isdir(path):
            create_folders(path)
        os.mkdir(folder)


def get_colors():
    np.random.seed(0)
    basic_colors = np.random.random((65535, 3))

    return basic_colors.tolist()


def get_class(kls):
    parts = kls.split(".")
    module = ".".join(parts[:-1])
    m = __import__(module)
    for comp in parts[1:]:
        m = getattr(m, comp)
    return m


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


def loadnet(modelpath):
    """
    Load a previously saved model stored in modelpath
    """

    print("Loading model: {} - ".format(modelpath), end=" ")
    if not os.path.isfile(modelpath):
        resource_line = ""
        resource_file = os.path.expanduser(
            os.path.join("~", ".jcell", "jcellrc")
        )
        if os.path.exists(resource_file):
            f = open(resource_file, "r")
            resource_line = f.read()
            f.close()
        else:
            print(
                "Pre-trained models not found. Please, do jcell-update for downloading the latest version."
            )
        if resource_line != "":
            path_jcell = os.path.expanduser(
                os.path.join(resource_line, "models")
            )
            current_models_path = os.path.join(path_jcell, "models.json")
            current_models = (
                json.load(open(current_models_path))
                if os.path.exists(current_models_path)
                else {}
            )

            if modelpath not in current_models:
                raise ValueError("Model path or name is not valid.")

            modelpath = current_models[modelpath]["path"]
            if "$JCELLRES" in modelpath:
                modelpath = modelpath.replace(
                    "$JCELLRES", os.path.split(path_jcell)[0]
                )
        else:
            raise ValueError("Model path or name is not valid.")

    checkpoint = torch.load(modelpath, map_location="cpu")
    net = checkpoint["net"]
    if "arch" in checkpoint:
        arch = checkpoint["arch"]
    else:
        arch = type(net).__name__

    normalization_type = (
        checkpoint["normalization"]
        if "normalization" in checkpoint
        else "max_norm"
    )

    print("Succeeded")

    return net, arch, normalization_type


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
