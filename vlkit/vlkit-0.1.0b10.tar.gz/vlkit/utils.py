import os, re, logging
from os.path import join, isdir
import time

class DayHourMinute(object):
  
  def __init__(self, seconds):
      
      self.days = int(seconds // 86400)
      self.hours = int((seconds- (self.days * 86400)) // 3600)
      self.minutes = int((seconds - self.days * 86400 - self.hours * 3600) // 60)

def get_lr(epoch, base_lr, warmup_epochs=5, warmup_start_lr=0.001):
    lr = 0
    if epoch < warmup_epochs:
        lr = ((base_lr - warmup_start_lr) / warmup_epochs) * epoch
    else:
        lr = base_lr * (0.1 ** ((epoch-warmup_epochs) // 30))
    return lr

class AverageMeter(object):
    """Computes and stores the average and current value"""
    def __init__(self):
        self.reset()

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count

def get_logger(path="log.txt"):
    logger = logging.getLogger("Logger")
    file_handler = logging.FileHandler(path, "w")
    stdout_handler = logging.StreamHandler()
    logger.addHandler(file_handler)
    logger.addHandler(stdout_handler)
    logformatter = logging.Formatter('[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s','%m-%d %H:%M:%S')
    stdout_handler.setFormatter(logformatter)
    file_handler.setFormatter(logformatter)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    return logger


class Logger():
    def __init__(self, path="log.txt"):
        self.logger = logging.getLogger("Logger")
        self.file_handler = logging.FileHandler(path, "w")
        self.stdout_handler = logging.StreamHandler()
        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.stdout_handler)
        logformatter = logging.Formatter('[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s','%m-%d %H:%M:%S')
        self.stdout_handler.setFormatter(logformatter)
        self.file_handler.setFormatter(logformatter)
        self.logger.setLevel(logging.INFO)
    
    def info(self, txt):
        self.logger.info(txt)
    
    def close(self):
        self.file_handler.close()
        self.stdout_handler.close()


def work_dir(prefix=None):
    if prefix is None:
        prefix = "work_dirs/run"
    if prefix.endswith(os.sep):
        prefix = prefix[:-1]
    return prefix + time.strftime('%Y%m%d-%H:%M:%S', time.localtime())
