# -*- coding: utf-8 -*-

from Preset.Model.PartBase import PartBase
from typing import List
from Preset.Model.Transform import Transform
from Preset.Model.GameObject import GameObject
from Preset.Model.PresetBase import PresetBase
from Preset.Model.Block.BlockPreset import BlockPreset
import Preset.Controller.PresetManager as PresetManager

def GetAllPresets():
    # type: () -> List[PresetBase]
    """
    获取所有预设
    """

def GetBlockPresetByPosition(x, y, z):
    # type: (int, int, int) -> BlockPreset
    """
    获取指定位置的第一个方块预设
    """

def GetGameObjectByEntityId(entityId):
    # type: (str) -> GameObject
    """
    获取指定实体ID的游戏对象
    """

def GetGameObjectById(id):
    # type: (int) -> GameObject
    """
    获取指定对象ID的游戏对象
    """

def GetManager():
    """
    获取预设管理器
    """

    return PresetManager

def GetPresetByName(name):
    # type: (str) -> PresetBase
    """
    获取指定名称的第一个预设
    """

def GetPresetByType(classType):
    # type: (str) -> PresetBase
    """
    获取指定类型的第一个预设
    """

def GetPresetsByName(name):
    # type: (str) -> List[PresetBase]
    """
    获取指定名称的所有预设
    """

def GetPresetsByType(classType):
    # type: (str) -> List[PresetBase]
    """
    获取指定类型的所有预设
    """

def GetTickCount():
    # type: () -> int
    """
    获取当前帧数
    """

def LoadPartByModulePath(modulePath):
    # type: (str) -> PartBase
    """
    通过模块相对路径加载零件并实例化
    """

def LoadPartByType(partType):
    # type: (str) -> PartBase
    """
    通过类名加载零件并实例化
    """

def SpawnPreset(presetId, transform):
    # type: (int, Transform) -> PresetBase
    """
    在指定坐标变换处生成指定预设
    """

