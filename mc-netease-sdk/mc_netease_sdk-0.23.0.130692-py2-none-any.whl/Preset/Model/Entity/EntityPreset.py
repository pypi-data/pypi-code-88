# -*- coding: utf-8 -*-

from Preset.Model.PresetBase import PresetBase

class EntityPreset(PresetBase):
    def __init__(self):
        # type: () -> None
        """
        EntityPreset（实体预设）是一类特殊的预设，实体预设通常会绑定MC的某类实体，实体预设实例与MC的某一个实体绑定，因此可以使用实体预设来进行一些实体相关的逻辑的编程。
        """
        self.engineTypeStr = None
        self.entityId = None

    def GetHealth(self):
        # type: () -> float
        """
        获取实体预设的生命值
        """

    def SetHealth(self, hp):
        # type: (float) -> None
        """
        设置实体预设的生命值
        """

