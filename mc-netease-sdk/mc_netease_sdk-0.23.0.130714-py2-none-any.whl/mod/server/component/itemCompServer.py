# -*- coding: utf-8 -*-

from typing import List
from mod.common.component.baseComponent import BaseComponent
from typing import Tuple

class ItemCompServer(BaseComponent):
    def SpawnItemToLevel(self, itemDict, dimensionId=0, pos=(0, 0, 0)):
        # type: (dict, int, Tuple[float,float,float]) -> bool
        """
        生成物品掉落物，如果需要获取物品的entityId，可以调用服务端系统接口CreateEngineItemEntity
        """

    def SpawnItemToPlayerCarried(self, itemDict, playerId):
        # type: (dict, str) -> bool
        """
        生成物品到玩家右手
        """

    def ClearPlayerOffHand(self, playerId):
        # type: (str) -> bool
        """
        清除玩家左手物品
        """

    def SpawnItemToPlayerInv(self, itemDict, playerId, slotPos=-1):
        # type: (dict, str, int) -> bool
        """
        生成物品到玩家背包
        """

    def GetPlayerItem(self, posType, slotPos=0, getUserData=False):
        # type: (int, int, bool) -> dict
        """
        获取玩家物品，支持获取背包，盔甲栏，副手以及主手物品
        """

    def ChangePlayerItemTipsAndExtraId(self, posType, slotPos=0, customTips='', extraId=''):
        # type: (int, int, str, str) -> bool
        """
        修改玩家物品的自定义tips和自定义标识符
        """

    def AddEnchantToInvItem(self, slotPos, enchantType, level):
        # type: (int, int, int) -> bool
        """
        给物品栏的物品添加附魔信息
        """

    def GetInvItemEnchantData(self, slotPos):
        # type: (int) -> List[Tuple[int,int]]
        """
        获取物品栏的物品附魔信息
        """

    def SetInvItemNum(self, slotPos, num):
        # type: (int, int) -> bool
        """
        设置玩家背包物品数目
        """

    def SetInvItemExchange(self, pos1, pos2):
        # type: (int, int) -> bool
        """
        交换玩家背包物品
        """

    def SetInvItemDurability(self, slotPos, damage):
        # type: (int, int) -> bool
        """
        设置背包物品的耐久值
        """

    def GetInvItemDurability(self, slotPos):
        # type: (int) -> int
        """
        获取背包物品的耐久值
        """

    def SetEquItemDurability(self, slotPos, damage):
        # type: (int, int) -> bool
        """
        设置装备槽位中盔甲的耐久值
        """

    def GetEquItemDurability(self, slotPos):
        # type: (int) -> int
        """
        获取装备槽位中盔甲的耐久值
        """

    def GetDroppedItem(self, itemEntityId, getUserData=False):
        # type: (str, bool) -> dict
        """
        获取掉落在世界的指定entityid的物品信息
        """

    def GetEquItemEnchant(self, slotPos):
        # type: (int) -> List[Tuple[int,int]]
        """
        获取装备槽位中盔甲的附魔
        """

    def GetItemBasicInfo(self, itemName, auxValue=0, isEnchanted=False):
        # type: (str, int, bool) -> dict
        """
        获取物品的基础信息
        """

    def GetPlayerAllItems(self, posType, getUserData=False):
        # type: (int, bool) -> List[dict]
        """
        获取玩家指定的槽位的批量物品信息
        """

    def SetPlayerAllItems(self, itemsDictMap):
        # type: (dict) -> dict
        """
        添加批量物品信息到指定槽位
        """

    def GetEntityItem(self, posType, slotPos=0, getUserData=False):
        # type: (int, int, bool) -> dict
        """
        获取生物物品，支持获取背包，盔甲栏，副手以及主手物品
        """

    def SetEntityItem(self, posType, itemDict, slotPos=0):
        # type: (int, dict, int) -> bool
        """
        设置生物物品，建议开发者根据生物特性来进行设置，部分生物设置装备后可能不显示但是死亡后仍然会掉落所设置的装备
        """

    def GetCustomName(self, itemDict):
        # type: (dict) -> str
        """
        获取物品的自定义名称，与铁砧修改的名称一致
        """

    def SetCustomName(self, itemDict, name):
        # type: (dict, str) -> bool
        """
        设置物品的自定义名称，与使用铁砧重命名一致
        """

    def GetUserDataInEvent(self, eventName):
        # type: (str) -> bool
        """
        使物品相关服务端事件的物品信息字典参数带有userData。在mod初始化时调用即可
        """

    def GetSelectSlotId(self):
        # type: () -> int
        """
        获取玩家当前选中槽位
        """

    def GetContainerItem(self, pos, slotPos, dimensionId=-1, getUserData=False):
        # type: (Tuple[int,int,int], int, int, bool) -> dict
        """
        获取容器内的物品
        """

    def GetEnderChestItem(self, playerId, slotPos, getUserData=False):
        # type: (str, int, bool) -> dict
        """
        获取末影箱内的物品
        """

    def GetOpenContainerItem(self, playerId, containerId, getUserData=False):
        # type: (str, int, bool) -> dict
        """
        获取开放容器的物品
        """

    def SpawnItemToContainer(self, itemDict, slotPos, blockPos, dimensionId=-1):
        # type: (dict, int, Tuple[int,int,int], int) -> bool
        """
        生成物品到容器方块的物品栏
        """

    def SpawnItemToEnderChest(self, itemDict, playerId, slotPos):
        # type: (dict, str, int) -> bool
        """
        生成物品到末影箱
        """

    def GetContainerSize(self, pos, dimensionId=-1):
        # type: (Tuple[int,int,int], int) -> int
        """
        获取容器容量大小
        """

    def MayPlaceOn(self, identifier, auxValue, blockPos, facing):
        # type: (str, int, Tuple[int,int,int], int) -> bool
        """
        判断物品是否可以放到指定的位置上
        """

    def GetItemDurability(self, posType, slotPos):
        # type: (int, int) -> int
        """
        获取指定槽位的物品耐久
        """

    def SetItemDurability(self, posType, slotPos, durability):
        # type: (int, int, int) -> bool
        """
        设置物品的耐久值
        """

    def SetMaxStackSize(self, itemDict, maxStackSize):
        # type: (dict, int) -> bool
        """
         设置物品的最大堆叠数量（存档）
        """

    def SetAttackDamage(self, itemDict, attackDamage):
        # type: (dict, int) -> bool
        """
         设置物品的攻击伤害值
        """

    def SetItemTierLevel(self, itemDict, level):
        # type: (dict, int) -> bool
        """
         设置工具类物品的挖掘等级
        """

    def SetItemTierSpeed(self, itemDict, speed):
        # type: (dict, float) -> bool
        """
         设置工具类物品的挖掘速度
        """

    def SetShearsDestoryBlockSpeed(self, blockName, speed):
        # type: (str, float) -> bool
        """
         设置剪刀对某一方块的破坏速度
        """

    def CancelShearsDestoryBlockSpeed(self, blockName):
        # type: (str) -> bool
        """
         取消剪刀对某一方块的破坏速度设置
        """

    def CancelShearsDestoryBlockSpeedAll(self):
        # type: () -> bool
        """
         取消剪刀对全部方块的破坏速度设置
        """

