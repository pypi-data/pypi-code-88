# -*- coding: utf-8 -*-

from Preset.Model.GameObject import GameObject
from typing import Matrix

class Transform(GameObject):
    def __init__(self):
        # type: () -> None
        """
        坐标变换，包含位置、旋转和缩放
        """
        self.pos = None
        self.rotation = None
        self.scale = None

    def GetMatrix(self):
        # type: () -> Matrix
        """
        获取坐标变换矩阵
        """

