import os
import re
import shutil
from datetime import datetime, timedelta
from glob import glob

from loguru import logger

from jexp.utils import latest_time


def extract_all_exp(folder: str = "outputs"):
    """extract whole hyd runs under folder

    :param folder: [description], defaults to "outputs"
    :type folder: str, optional
    :return: list of pathes
    """
    rtn_exps = []
    for cur_path in glob(f"{folder}/*/*/"):
        if re.search(r"\d{4}-\d{2}-\d{2}/\d{2}-\d{2}-\d{2}/$", cur_path):
            rtn_exps.append(cur_path)
    return sorted(rtn_exps, reverse=True)


def time_from_folder(folder_str: str):
    """hyd folder name 2 its creation time

    :param folder_str: [description]
    :type folder_str: str
    :return: datetime
    """
    assert folder_str[-1] == "/"
    exp_path_time = folder_str[-20:]
    return datetime.strptime(exp_path_time, "%Y-%m-%d/%H-%M-%S/")


def clear_empty(folder: str = "outputs"):
    """clear empty hyd runs folder

    :param folder: [description], defaults to "outputs"
    :type folder: str, optional
    """
    for cur_path in glob(f"{folder}/*/"):
        if len(os.listdir(cur_path)) == 0:
            shutil.rmtree(str(cur_path), ignore_errors=True)


def filter_hyd_short(folder: str = "outputs", delete=True):
    survive = []
    for run_f in extract_all_exp(folder):
        create_time = time_from_folder(run_f)
        end_time = latest_time(run_f)
        now = datetime.now()
        run2now = now - end_time
        duration = end_time - create_time
        time_thred = [[0, 10], [7, 60], [3, 180], [1, 600]]
        for thr_d, thr_s in time_thred:
            if run2now > timedelta(days=thr_d) and duration < timedelta(seconds=thr_s):
                logger.info(f"SHORT: {run_f}")
                if delete:
                    shutil.rmtree(run_f, ignore_errors=True)
                break
        survive.append(run_f)
    return survive
