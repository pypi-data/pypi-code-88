# -*- coding: utf-8 -*-

from Preset.Model.Entity.EntityPreset import EntityPreset

class PlayerPreset(EntityPreset):
    def __init__(self):
        # type: () -> None
        """
        PlayerPreset（玩家预设）是一类特殊的实体预设，玩家预设与玩家实体进行绑定。每个AddOn（编辑器作品）只允许创建一个玩家预设。不同AddOn的玩家预设均会与玩家实体绑定。
        """
        self.entityId = None

    def GetPlayerId(self):
        # type: () -> str
        """
        获取玩家预设的玩家ID
        """

