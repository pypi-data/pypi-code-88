import os.path
import sys
from abc import ABC, abstractmethod
from threading import RLock
from typing import Dict

from .utils import TopicAware

# 日志文件每隔 512m 进行一次分割
FILE_OUTPUT_MAX_SIZE = 512 * 1024 * 1024
# 最多保留 4 个分割
FILE_OUTPUT_MAX_COUNT = 4


class Output(ABC):

    @abstractmethod
    def append_event(self, event: "Event") -> None:
        pass


class ConsoleOutput(Output):
    topic_aware: TopicAware
    lock: RLock

    def __init__(self, opts: dict):
        self.topic_aware = TopicAware(opts["topics"])
        self.lock = RLock()

    def append_event(self, event: "Event") -> None:
        if not self.topic_aware.is_enabled(event.topic):
            return
        self.lock.acquire()
        try:
            sys.stdout.write(
                "[{}] [{}] {} {}\n".format(event.timestamp, event.topic, event.format_extra(),
                                           "" if event.message is None else event.message))
        finally:
            self.lock.release()


class FileOutput(Output):
    topic_aware: TopicAware
    lock: RLock
    dir: str
    subdirs: Dict[str, TopicAware]
    fds: Dict[str, int]
    fsizes: Dict[str, int]

    def __init__(self, opts: dict):
        self.topic_aware = TopicAware(opts["topics"])
        self.lock = RLock()
        self.dir = opts["dir"]
        self.subdirs = {}
        self.fds = {}
        self.fsizes = {}
        if "subdirs" in opts:
            for (k, v) in opts["subdirs"].items():
                self.subdirs[k] = TopicAware(v)

    def release_fds(self):
        fds = self.fds
        self.fds = {}
        self.fsizes = {}
        for (k, v) in fds.items():
            try:
                os.close(v)
            finally:
                pass

    def calculate_filename(self, event: "Event") -> str:
        subdir = "others"
        if self.subdirs is not None:
            for (k, v) in self.subdirs.items():
                found = False
                if v.is_enabled(event.topic):
                    subdir = k
                    found = True
                if found:
                    break

        return os.path.abspath(
            os.path.join(self.dir, subdir, "{}.{}.{}.log".format(event.env, event.topic, event.project)))

    def get_fd(self, filename: str) -> int:
        fd = None
        if filename in self.fds:
            fd = self.fds[filename]
        else:
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            fd = os.open(filename, os.O_CREAT | os.O_WRONLY | os.O_APPEND)
            self.fds[filename] = fd
            self.fsizes[filename] = os.fstat(fd).st_size
        return fd

    def on_fd_write(self, filename: str, size: int):
        # 如果当前文件大于分割大小，则关闭当前 fd 并删除记录，下次写入时会自动重新打开
        self.fsizes[filename] += size
        if self.fsizes[filename] < FILE_OUTPUT_MAX_SIZE:
            return
        fd = self.fds[filename]
        try:
            os.close(fd)
        finally:
            pass
        del self.fds[filename]
        del self.fsizes[filename]
        # 获取当前日志目录已经存在的，和当前日志文件前缀一致的分片编号，并从小到大排序
        dirname = os.path.dirname(filename)
        prefix = os.path.basename(filename)[:-4] + "."
        rotated_ids = []
        for rotated_files in os.listdir(dirname):
            if not rotated_files.startswith(prefix):
                continue
            rotated_id_raw = rotated_files[len(prefix):-4]
            if len(rotated_id_raw) == 0:
                continue
            try:
                rotated_ids.append(int(rotated_id_raw))
            finally:
                pass
        rotated_ids.sort()
        # 计算下个分片编号，并删除过于久远的分片
        next_rotated_id = 1
        if len(rotated_ids) > 0:
            next_rotated_id = rotated_ids[-1] + 1
        if len(rotated_ids) >= FILE_OUTPUT_MAX_COUNT:
            for rotated_id in rotated_ids[:len(rotated_ids) - FILE_OUTPUT_MAX_COUNT]:
                try:
                    os.unlink(os.path.join(dirname, prefix + str(rotated_id) + ".log"))
                finally:
                    pass
        # 将当前文件重命名为最新编号，等待下次写入时打开新文件
        try:
            os.rename(filename, os.path.join(dirname, prefix + str(next_rotated_id) + ".log"))
        finally:
            pass

    def append_event(self, event: "Event") -> None:
        if not self.topic_aware.is_enabled(event.topic):
            return
        self.lock.acquire()
        try:
            filename = self.calculate_filename(event)
            fd = self.get_fd(filename)
            buf = "[{}] [{}] {}\n".format(event.timestamp, event.format_extra(),
                                          "" if event.message is None else event.message).encode()
            os.write(fd, buf)
            self.on_fd_write(filename, len(buf))
        finally:
            self.lock.release()
