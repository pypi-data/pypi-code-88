# -*- coding: utf-8 -*-

from Preset.Model.PresetBase import PresetBase
from Preset.Model.TransformObject import TransformObject

class PartBase(TransformObject):
    def __init__(self):
        # type: () -> None
        """
        PartBase（零件基类）是可以与零件进行绑定，而零件可以挂接在预设下，以实现带逻辑的预设的组装。所有的自定义零件都需要继承PartBase，预设系统下的大部分代码都需要写在自定义零件中。注意，自定义零件只有挂接到预设，并且在游戏中实例化才能生效。
        """
        self.tickEnable = None
        self.replicated = None

    def InitClient(self):
        # type: () -> None
        """
        客户端的零件对象初始化入口
        """

    def InitServer(self):
        # type: () -> None
        """
        服务端的零件对象初始化入口
        """

    def TickClient(self):
        # type: () -> None
        """
        客户端的零件对象逻辑驱动入口
        """

    def TickServer(self):
        # type: () -> None
        """
        服务端的零件对象逻辑驱动入口
        """

    def UnloadClient(self):
        # type: () -> None
        """
        客户端的零件对象卸载逻辑入口
        """

    def UnloadServer(self):
        # type: () -> None
        """
        服务端的零件对象卸载逻辑入口
        """

    def DestroyClient(self):
        # type: () -> None
        """
        客户端的零件对象销毁逻辑入口
        """

    def DestroyServer(self):
        # type: () -> None
        """
        服务端的零件对象销毁逻辑入口
        """

    def CanAdd(self, parent):
        # type: (PresetBase) -> str
        """
        判断零件是否可以挂接到指定的父节点上
        """

    def ListenForEvent(self, namespace, systemName, eventName, instance, func, priority=0):
        # type: (str, str, str, object, object, str) -> None
        """
        监听指定的事件
        """

    def UnListenForEvent(self, namespace, systemName, eventName, instance, func, priority=0):
        # type: (str, str, str, object, object, str) -> None
        """
        反监听指定的事件
        """

    def DefineEvent(self, eventName):
        # type: (str) -> None
        """
        定义事件
        """

    def UnDefineEvent(self, eventName):
        # type: (str) -> None
        """
        反定义事件
        """

    def BroadcastEvent(self, eventName, eventData):
        # type: (str, object) -> None
        """
        广播事件，双端通用
        """

    def BroadcastClientEvent(self, eventName, eventData):
        # type: (str, object) -> None
        """
        广播给所有客户端
        """

    def BroadcastServerEvent(self, eventName, eventData):
        # type: (str, object) -> None
        """
        广播给所有服务端
        """

    def NotifyToServer(self, eventName, eventData):
        # type: (str, object) -> None
        """
        通知服务端触发事件
        """

    def NotifyToClient(self, playerId, eventName, eventData):
        # type: (str, str, object) -> None
        """
        通知指定客户端触发事件
        """

    def BroadcastToAllClient(self, eventName, eventData):
        # type: (str, object) -> None
        """
        通知指所有客户端触发事件
        """

    def ListenSelfEvent(self, eventName, target, func):
        # type: (str, object, object) -> None
        """
        监听来自自己的事件
        """

    def UnListenSelfEvent(self, eventName, target, func):
        # type: (str, object, object) -> None
        """
        反监听来自自己的事件
        """

