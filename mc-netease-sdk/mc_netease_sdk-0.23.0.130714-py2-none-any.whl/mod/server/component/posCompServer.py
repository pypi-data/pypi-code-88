# -*- coding: utf-8 -*-

from typing import Tuple

class PosComponentServer(object):
    def SetPos(self, pos):
        # type: (Tuple[int,int,int]) -> bool
        """
        设置实体位置
        """

    def GetPos(self):
        # type: () -> Tuple[float,float,float]
        """
        获取实体位置
        """

    def GetFootPos(self):
        # type: () -> Tuple[float,float,float]
        """
        获取实体脚所在的位置
        """

    def SetFootPos(self, footPos):
        # type: (Tuple[float,float,float]) -> bool
        """
        设置实体脚底所在的位置
        """

