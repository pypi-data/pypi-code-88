import concurrent
import os
import time
import urllib
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from types import SimpleNamespace
from typing import *

import pandas as pd
import wget
from fastprogress.fastprogress import progress_bar

"""
This module contains all the general add ons
"""


def ifnone(a, b):
    """
    Return if None
    """
    return b if a is None else a


def listify(o):
    """
    Convert to list
    """
    if o is None:
        return []
    if isinstance(o, list):
        return o
    if isinstance(o, str):
        return [o]
    if isinstance(o, Iterable):
        return list(o)
    return [o]


def compose(x, funcs, *args, order_key="_order", **kwargs):  #%t
    """
    Chain functions
    """
    key = lambda o: getattr(o, order_key, 0)
    for f in sorted(listify(funcs), key=key):
        x = f(x, **kwargs)
    return x


def timeit(method):  #%t
    """
    Helper to time a function
    """

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if "log_time" in kw:
            name = kw.get("log_name", method.__name__.upper())
            kw["log_time"][name] = int((te - ts) * 1000)
        else:
            print("%r  %2.2f ms" % (method.__name__, (te - ts) * 1000))
        return result

    return timed


def num_cpus() -> int:
    "Get number of cpus"
    try:
        return len(os.sched_getaffinity(0))
    except AttributeError:
        return os.cpu_count()


_default_cpus = min(16, num_cpus())
defaults = SimpleNamespace(
    cpus=_default_cpus, cmap="viridis", return_fig=False, silent=False
)


def parallel(func, arr: Collection, max_workers: int = None, leave=False):  #%t
    "Call `func` on every element of `arr` in parallel using `max_workers`."
    max_workers = ifnone(max_workers, defaults.cpus)
    if max_workers < 2:
        results = [
            func(o, i)
            for i, o in progress_bar(enumerate(arr), total=len(arr), leave=leave)
        ]
    else:
        with ProcessPoolExecutor(max_workers=max_workers) as ex:
            futures = [ex.submit(func, o, i) for i, o in enumerate(arr)]
            results = []
            for f in progress_bar(
                concurrent.futures.as_completed(futures), total=len(arr), leave=leave
            ):
                results.append(f.result())
    if any([o is not None for o in results]):
        return results


def get_name_from_url(url, name):
    """
    Take a url and grab the name if not specified
    """
    if len(name) != None:
        return url.split("/")[-1]
    else:
        return name


def bar_progress(current, total, width=80):
    """
    Custom progress bar for dataset download
    """
    progress_message = "Downloading: %d%% [%d / %d] bytes" % (
        current / total * 100,
        current,
        total,
    )
    # Don't use print() as it will print in new line every time.
    sys.stdout.write("\r" + progress_message)
    sys.stdout.flush()


def download_and_check(url, fpath=".", name=""):  #%t
    """
    Download and save if url or just take path
    """
    down_path = Path.joinpath(Path(fpath), get_name_from_url(url, name))
    if any(x for x in ["www", "http"] if x in url):
        status_code = urllib.request.urlopen(url).getcode()
        if status_code != 200:
            print("Sorry, invalid url")
        else:
            if not Path.exists(down_path):
                wget.download(url, str(down_path), bar=bar_progress)
                print(f"Downloaded to {down_path}")
            else:
                print(f"Already downloaded at {down_path}")
    else:
        if not Path.exists(down_path):
            return "Invalid path"
    return down_path


def get_last_log(name, fpath="logs"):  #%t
    """
    Get last log and print last 5 lines

    """
    fpath = Path(fpath)
    t = os.listdir(fpath / name)

    nos = [str(x.split("_")[1]) for x in t]
    nos.sort()
    nos = [int(x) for x in nos[:-1]]
    nos.sort()

    print(pd.read_csv(fpath / f"{name}/version_{nos[-1]}/metrics.csv").tail(5))


def split_by_func(items, f):
    """
    Split a list by a function

    """
    mask = [f(o) for o in items]
    f = [o for o, m in zip(items, mask) if m == False]
    t = [o for o, m in zip(items, mask) if m == True]
    return f, t
