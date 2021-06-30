# -*- coding: utf-8 -*-

from typing import Union
from mod.common.component.baseComponent import BaseComponent

class PlayerCompClient(BaseComponent):
    def OpenPlayerHitBlockDetection(self, precision):
        # type: (float) -> bool
        """
        开启碰撞方块的检测，开启后碰撞时会触发OnPlayerHitBlockClientEvent事件
        """

    def ClosePlayerHitBlockDetection(self):
        # type: () -> bool
        """
        关闭碰撞方块的检测，关闭后将不会触发OnPlayerHitBlockClientEvent事件
        """

    def OpenPlayerHitMobDetection(self):
        # type: () -> bool
        """
        开启玩家碰撞到生物的检测，开启后该玩家碰撞到生物时会触发OnPlayerHitMobClientEvent事件
        """

    def ClosePlayerHitMobDetection(self):
        # type: () -> bool
        """
        关闭碰撞生物的检测，关闭后将不会触发OnPlayerHitMobClientEvent事件
        """

    def isGliding(self):
        # type: () -> bool
        """
        是否鞘翅飞行
        """

    def isSwimming(self):
        # type: () -> bool
        """
        是否游泳
        """

    def isRiding(self):
        # type: () -> bool
        """
        是否骑乘
        """

    def isSneaking(self):
        # type: () -> bool
        """
        是否潜行
        """

    def setSneaking(self):
        # type: () -> bool
        """
        设置是否潜行，只能设置本地玩家（只适用于移动端）
        """

    def isSprinting(self):
        # type: () -> bool
        """
        是否在疾跑
        """

    def setSprinting(self):
        # type: () -> bool
        """
        设置是否疾跑，只能设置本地玩家（只适用于移动端）
        """

    def isInWater(self):
        # type: () -> bool
        """
        是否在水中
        """

    def isMoving(self):
        # type: () -> bool
        """
        是否在行走
        """

    def setMoving(self):
        # type: () -> bool
        """
        设置是否行走，只能设置本地玩家（只适用于移动端）
        """

    def getUid(self):
        # type: () -> Union[long,None]
        """
        获取本地玩家的uid
        """

