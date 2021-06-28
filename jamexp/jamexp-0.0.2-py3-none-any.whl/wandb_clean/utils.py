import datetime
import os.path as osp
import shutil
import socket

from loguru import logger

# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
TIME_PARTTERN = "%Y-%m-%dT%H:%M:%S"


def extract_time(run):
    """extract run info

    :param run: [description]
    :type run: [type]
    :return: duration, run2now
    :rtype: datetime.timedelta
    """
    create_time_str = run.createdAt
    last_time_str = run.heartbeatAt
    start_time = datetime.datetime.strptime(create_time_str, TIME_PARTTERN)
    end_time = datetime.datetime.strptime(last_time_str, TIME_PARTTERN)
    now_time = datetime.datetime.now()
    duration = end_time - start_time
    run2now = now_time - end_time
    return duration, run2now


def delete_run(run, delete=True, is_all=False):
    # FIXME: should be a better approach to get hostname
    if not is_all and run.config["host"] != socket.gethostname():
        logger.info(f"skip {run.config['host']} {run.name}\t{run.url}")
    delete_info = f"{run.name}\t{run.url}"
    cfg = run.config
    if "run_path" in cfg:
        if osp.exists(cfg["run_path"]):
            if delete:
                shutil.rmtree(cfg["run_path"], ignore_errors=True)
            delete_info += f"\n\t{cfg['run_path']}"
    logger.info(delete_info)
    if delete:
        run.delete()
