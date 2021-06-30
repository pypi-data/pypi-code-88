# -*- coding: utf-8 -*-


class GameObject(object):
    def __init__(self):
        # type: () -> None
        """
        GameObject（游戏对象）是所有预设对象的基类，即API文档中Preset API - 预设对象下的所有类都继承自GameObject。
        """
        self.id = None
        self.classType = None
        self.isClient = None

    def LoadFile(self, path):
        # type: (str) -> str
        """
        加载指定路径的非python脚本文件内容，如配置文件
        """




def registerGenericClass(genericType):
    # type: (str) -> None
    """
    注册为游戏对象
    """

