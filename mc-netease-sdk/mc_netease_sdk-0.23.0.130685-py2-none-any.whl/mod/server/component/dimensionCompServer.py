# -*- coding: utf-8 -*-

from typing import List
from mod.common.component.baseComponent import BaseComponent
from typing import Tuple

class DimensionCompServer(BaseComponent):
    def ChangePlayerDimension(self, dimensionId, pos):
        # type: (int, Tuple[int,int,int]) -> bool
        """
        传送玩家
        """

    def GetEntityDimensionId(self):
        # type: () -> int
        """
        获取实体所在维度
        """

    def ChangeEntityDimension(self, dimensionId, pos=None):
        # type: (int, Tuple[int,int,int]) -> bool
        """
        传送实体
        """

    def MirrorDimension(self, fromId, toId):
        # type: (int, int) -> bool
        """
        复制不同dimension的地形
        """

    def CreateDimension(self, dimensionId):
        # type: (int) -> bool
        """
        创建新的dimension
        """

    def RegisterEntityAOIEvent(self, dimension, name, aabb, ignoredEntities, entityType=1):
        # type: (int, str, Tuple[float,float,float,float,float,float], List[str], int) -> bool
        """
        注册感应区域，有实体进入时和离开时会有消息通知
        """

    def UnRegisterEntityAOIEvent(self, dimension, name):
        # type: (int, str) -> bool
        """
        反注册感应区域
        """

    def SetUseLocalTime(self, dimension, value):
        # type: (int, bool) -> bool
        """
        让某个维度拥有自己的局部时间规则，开启后该维度可以拥有与其他维度不同的时间与是否昼夜更替的规则
        """

    def GetUseLocalTime(self, dimension):
        # type: (int) -> bool
        """
        获取某个维度是否设置了使用局部时间规则
        """

    def SetLocalTime(self, dimension, time):
        # type: (int, int) -> bool
        """
        设置使用局部时间规则维度的时间
        """

    def SetLocalTimeOfDay(self, dimension, timeOfDay):
        # type: (int, int) -> bool
        """
        设置使用局部时间规则维度在一天内所在的时间
        """

    def GetLocalTime(self, dimension):
        # type: (int) -> int
        """
        获取维度的时间
        """

    def SetLocalDoDayNightCycle(self, dimension, value):
        # type: (int, bool) -> bool
        """
        设置使用局部时间规则的维度是否打开昼夜更替
        """

    def GetLocalDoDayNightCycle(self, dimension):
        # type: (int) -> bool
        """
        获取维度是否打开昼夜更替
        """

