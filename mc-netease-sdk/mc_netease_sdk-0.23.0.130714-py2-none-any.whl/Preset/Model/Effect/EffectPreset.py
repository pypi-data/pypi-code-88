# -*- coding: utf-8 -*-

from Preset.Model.PresetBase import PresetBase

class EffectPreset(PresetBase):
    def __init__(self):
        # type: () -> None
        """
        EffectPreset（特效预设）是一类绑定特效资源的预设。
        """
        self.resource = None
        self.effectType = None
        self.auto = None

    def Play(self):
        # type: () -> None
        """
        播放特效，仅客户端有效
        """

    def Stop(self):
        # type: () -> None
        """
        停止播放特效，仅客户端有效
        """

    def GetResource(self):
        # type: () -> str
        """
        获取绑定的json资源
        """

    def SetResource(self, resource):
        # type: (str) -> None
        """
        设置绑定的json资源
        """

