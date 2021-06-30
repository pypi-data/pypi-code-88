# -*- coding: utf-8 -*-

from mod.common.component.baseComponent import BaseComponent
from typing import Tuple

class ExpComponentServer(BaseComponent):
    def GetPlayerExp(self, isPercent=True):
        # type: (bool) -> float
        """
        获取玩家当前等级下的经验值
        """

    def AddPlayerExperience(self, exp):
        # type: (int) -> bool
        """
        增加玩家经验值
        """

    def SetOrbExperience(self, exp):
        # type: (int) -> bool
        """
        设置经验球经验
        """

    def CreateExperienceOrb(self, exp, position, isSpecial):
        # type: (int, Tuple[float,float,float], bool) -> bool
        """
        创建专属经验球
        """

    def GetOrbExperience(self):
        # type: () -> int
        """
        获取经验球的经验
        """

    def GetPlayerTotalExp(self):
        # type: () -> int
        """
        获取玩家的总经验值
        """

    def SetPlayerTotalExp(self, exp):
        # type: (int) -> bool
        """
        设置玩家的总经验值
        """

