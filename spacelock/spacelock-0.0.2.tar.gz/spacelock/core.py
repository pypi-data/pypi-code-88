"""
Author:     LanHao
Date:       2021/6/24 9:19

"""
import asyncio
import logging
import json
from dataclasses import dataclass, field, asdict
from typing import Optional, List, Callable, Dict

from asyncio import transports
from sortedcontainers import SortedDict
from rtree import index


# 基础数据类

@dataclass
class BaseMessage(object):
    """
    基础的消息类

    """
    pass


@dataclass
class SpaceKeyMessage(BaseMessage):
    key: str = "default_space_key"


@dataclass
class LockMessage(BaseMessage):
    box: List = field(default_factory=lambda: [])
    release: bool = False


@dataclass
class ResultMessage(BaseMessage):
    message: BaseMessage = field(default=BaseMessage())  # 尽量通过这个来实现
    status: int = 200  # 模仿http status 状态码


@dataclass
class HandleMessage(BaseMessage):
    message: BaseMessage = field(default=BaseMessage())
    handle_status: int = 0  # 不同int 对应不同的处理方式


class BoxLock(object):
    """
    空间锁

    """

    func_lock_released_call: List = None
    could_use: int = 0
    func_got_lock: Callable = None
    box: List = None

    def __init__(self, box: List, func_got_lock: Callable):
        self.box = box
        self.func_lock_released_call = []
        self.func_got_lock = func_got_lock

    def signal_call(self):
        self.could_use -= 1
        if self.could_use == 0:  # 可以使用了
            self.func_got_lock()  # 通知锁

    def register_release_call(self, func: Callable):
        """
        增加在锁释放时调用的函数

        :param func:
        :return:
        """
        self.func_lock_released_call.append(func)

    def release(self):
        """
        释放锁

        :return:
        """
        for func in self.func_lock_released_call:
            func: Callable
            func()


class Space(object):
    """
    锁空间

    """
    name: str = None  # 空间别名
    count: int = 0  # 多少个链接在用
    id: int = 0  # 该空间下递增的id
    box_cache: SortedDict = None  # box 缓存
    tree: index.Index = None  # 空间索引

    def __init__(self, name: str):
        self.name = name  # 空间的别名,用于区分多个空间占用,用于对多个程序提供服务
        p = index.Property()
        p.dimension = 3

        self.tree = index.Index(properties=p)
        self.box_cache = SortedDict()  # 缓存所有的box_cache

    def get_increase_id(self):
        """
        获取递增id

        :return:
        """
        self.id += 1
        return self.id

    def lock(self, box: List, call_lock) -> int:
        """
        枷锁,枷锁成功后通过call_lock 通知

        :param box:
        :param call_lock:
        :return:
        """
        aabb_box = BoxLock(box, call_lock)
        logging.debug(f"box:{box}")
        intersection_boxs = self.tree.intersection(box)

        for id_intersection in intersection_boxs:
            aabb_box_tmp: BoxLock = self.box_cache.get(id_intersection)
            if aabb_box_tmp:
                aabb_box_tmp.register_release_call(aabb_box.signal_call)
                aabb_box.could_use += 1
            else:
                # id存在某个锁,但是现在box_cache 中已经不存在了
                logging.debug(f"逻辑异常部分")

        lock_id = self.get_increase_id()

        self.tree.insert(lock_id, box)
        self.box_cache[lock_id] = aabb_box

        if aabb_box.could_use == 0:
            call_lock()

        return lock_id

    def release(self, box_lock_id: int) -> bool:
        """
        释放该空间中的某个锁

        :param box_lock_id:
        :return:
        """
        logging.debug(self.tree.leaves())
        aabb_box: BoxLock = self.box_cache.pop(box_lock_id)
        aabb_box.release()
        self.tree.delete(box_lock_id, coordinates=aabb_box.box)

        logging.debug(self.tree.leaves())

        return True


class LockHandler(asyncio.Protocol):
    """
    尝试提供一个基于TCP 的锁服务,此处对应的是每一次建立链接时被调用

    """
    transport: transports.BaseTransport = None
    logger: logging.Logger = None

    spaces: SortedDict = None

    space_key: str = None  # 同一个client 链接,只能属于一个space 空间
    space: Space = None  # 所处空间
    lock_id: int = None  # 同一时刻,一个client 只能加一个锁

    def __init__(self, spaces: SortedDict, logger: logging.Logger = None, *args, **kwargs):
        """
        server 初始化

        :param args:
        :param kwargs:
        """
        if logger is None:
            logger = logging.getLogger(__name__)
        self.logger = logger
        self.spaces = spaces

    # 扩展函数
    def register_space(self, name: str) -> Space:
        """
        注册一个空间

        :param name:
        :return:
        """
        space = Space(name)
        self.spaces[name] = space
        return space

    def delete_space(self) -> bool:
        """
        删除一个空间

        :param name:
        :return:
        """
        space = self.spaces.pop(self.space.name)
        self.space = None
        self.space_key = None
        return True

    def get_lock(self):

        self.logger.debug(f"枷锁成功")
        self.logger.debug(f"leaves:{self.space.tree.leaves()}")
        self.transport.write(json.dumps(asdict(ResultMessage())).encode("utf8"))

    def lock(self, box: List) -> None:
        """
        通过回调枷锁

        :param box:
        :return:
        """
        self.logger.debug("正在枷锁")
        space: Space = self.spaces[self.space_key]
        self.lock_id = space.lock(box, self.get_lock)

    def release_lock(self):
        """
        释放那个占据的锁
        :return:
        """
        if self.lock_id:
            self.space.release(self.lock_id)

        self.lock_id = None

    # 继承函数
    def connection_made(self, transport: transports.BaseTransport) -> None:
        """
        建立链接

        :param transport:
        :return:
        """

        self.transport = transport

    def data_received(self, data: bytes) -> None:
        """
        接收数据

        :param data:
        :return:
        """
        json_data = json.loads(data.decode("utf8"))
        self.logger.debug(f"json_data:{json_data}")
        handle_message = HandleMessage(**json_data)
        if handle_message.handle_status == 0:  # 获取空间
            self.logger.debug(f"handle_message.message:{handle_message.message}")
            key_message = SpaceKeyMessage(**handle_message.message)
            self.space_key = key_message.key
            self.space = self.spaces.get(self.space_key)

            if not self.space:
                self.space = Space(self.space_key)
            self.space.count += 1
            self.spaces[self.space_key] = self.space
            self.transport.write(json.dumps(asdict(ResultMessage())).encode("utf8"))
        else:
            self.logger.debug(f"等待枷锁")
            lock_message = LockMessage(**handle_message.message)
            if lock_message.release:  # 释放锁
                if self.lock_id:
                    self.release_lock()
            else:
                self.lock(lock_message.box)

    def connection_lost(self, exc: Optional[Exception]) -> None:
        """
        断开链接

        断开链接时：

        - 如果已经枷锁了，就去掉这个锁,如果没有锁，这跳过

        - 如果空间已经归属了，这在其归属的空间上,count 自减,如果空间count 小于等于0，则消除空间

            此时,space 中的rtree，内容应该为空了

        - transport 为None

        :param exc:
        :return:
        """

        if self.lock_id:
            self.release_lock()

        if self.space:
            self.space.count -= 1
            if self.space.count == 0:
                self.delete_space()

        self.transport = None


def get_lock_handler(*args, **kwargs):
    """

    闭包形式,供调用
    :param args:
    :param kwargs:
    :return:
    """

    def wrapper():
        return LockHandler(*args, **kwargs)

    return wrapper
