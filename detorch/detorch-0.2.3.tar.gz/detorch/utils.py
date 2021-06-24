import math
import numpy as np
from functools import wraps, lru_cache
import hashlib
import cloudpickle
from pathlib import Path
import inspect
from mpi4py import MPI
from typing import Iterable
from pipcs import Config
import os
from collections import OrderedDict


class SummaryWriter():
    def __init__(self, config):
        config_dump = cloudpickle.dumps(config)
        hash = hashlib.sha1(config_dump).hexdigest()
        if isinstance(config, Iterable) and not isinstance(config, Config):
            config = config[0]
        # if config.writer.clear:
        #     rmtree(config.writer.log_dir, True)
        Path(config.writer.log_dir).mkdir(parents=True, exist_ok=True)
        with open(os.path.join(config.writer.log_dir, hash), 'wb') as f:
            f.write(config_dump)
        path = os.path.join(config.writer.log_dir, hash + '.log')
        self.columns = set()
        self.label_loc = 0
        self.f = open(path, 'w+')
        self.values = OrderedDict()

    def add(self, **kwargs):
        for k in kwargs:
            if k not in self.values:
                self.f.seek(0, os.SEEK_SET)
                contents = self.f.readlines()
                if not len(contents):
                    contents.append(k)
                else:
                    contents[0] = contents[0].rstrip() + f',{k}\n'
                self.f.seek(0, os.SEEK_SET)
                self.f.writelines(contents)
            self.values[k] = kwargs[k]

    def flush(self):
        for i, k in enumerate(self.values):
            if i:
                self.f.write(',')
            self.f.write(str(self.values[k]))
        self.f.write('\n')
        self.f.flush()

    def __exit__(self):
        self.f.close()


if MPI.COMM_WORLD.Get_rank() != 0:
    for name, fn in inspect.getmembers(SummaryWriter, inspect.isfunction):
        setattr(SummaryWriter, name, lambda *args, **kwargs: None)


def hook(func):
    func.before_register = []
    func.after_register = []
    def add_hook(after=True):
        def _add_hook(hook):
            if after:
                func.after_register.append(hook)
            else:
                func.before_register.append(hook)
        return _add_hook

    func.add_hook = add_hook

    @wraps(func)
    def wrapped(*args, **kwargs):
        for hook in func.before_register:
            hook(*args, **kwargs)
        ret = func(*args, **kwargs)
        for hook in func.after_register:
            hook(*args, **kwargs, ret=ret)
        return ret

    return wrapped


def calculate_cr(size):
    return np.exp(-0.5) / (np.log(size) * np.sqrt(2 * np.pi) + np.exp(-0.5))


@lru_cache(maxsize=1)
def _center_function(population_size):
    centers = np.arange(0, population_size, dtype=np.float32)
    centers = centers / (population_size - 1)
    centers -= 0.5
    centers *= 2.0
    return centers


def _compute_ranks(rewards):
    rewards = np.array(rewards)
    ranks = np.empty(rewards.size, dtype=int)
    ranks[rewards.argsort()] = np.arange(rewards.size)
    return ranks


def rank_transformation(rewards):
    ranks = _compute_ranks(rewards)
    values = _center_function(rewards.size)
    return values[ranks]
