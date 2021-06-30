# -*- coding: utf-8 -*-

from typing import Matrix
from typing import Tuple
from Preset.Model.GameObject import GameObject
from typing import List
from Preset.Model.Transform import Transform
import Preset.Controller.PresetManager as PresetManager
from Preset.Model.TransformObject import TransformObject
from Preset.Model.PresetBase import PresetBase

class TransformObject(GameObject):
    def __init__(self):
        # type: () -> None
        """
        TransformObject（变换对象）是拥有变换属性的GameObject（游戏对象）的基类，他们在游戏世界中有着确切的位置等信息。
        """
        self.name = None
        self.transform = None
        self.isBroken = None
        self.isRemoved = None

    def GetDependencyChunks(self):
        # type: () -> set
        """
        获取所有依赖的chunkPos
        """

    def GetChildTransformObjects(self, recursive=False):
        # type: (bool) -> List[TransformObject]
        """
        获取子TransformObject列表
        """

    def GetTransformObjects(self, recursive=False):
        # type: (bool) -> List[TransformObject]
        """
        获取TransformObject列表，包含自身
        """

    def GetChildGameObjects(self, recursive=False):
        # type: (bool) -> List[GameObject]
        """
        获取子GameObject列表
        """

    def GetGameObjects(self, recursive=False):
        # type: (bool) -> List[GameObject]
        """
        获取GameObject列表，包含自身
        """

    def GetGameObjectById(self):
        # type: () -> GameObject
        """
        根据ID获取GameObject
        """

    def GetGameObjectByEntityId(self):
        # type: () -> GameObject
        """
        根据实体ID获取GameObject
        """

    def GetLevelId(self):
        # type: () -> str
        """
        获取当前预设所在的level_id
        """

    def GetDisplayName(self):
        # type: () -> str
        """
        获取当前预设的显示名称
        """

    def GetDisplayPath(self):
        # type: () -> str
        """
        获取当前预设到根节点的显示路径
        """

    def GetLocalTransform(self):
        # type: () -> Transform
        """
        获取当前预设的局部坐标变换
        """

    def SetLocalTransform(self, transform):
        # type: (Transform) -> None
        """
        设置当前预设的局部坐标变换
        """

    def GetLocalPosition(self):
        # type: () -> Tuple[float,float,float]
        """
        获取当前预设的局部坐标位置
        """

    def SetLocalPosition(self, pos):
        # type: (Tuple[float,float,float]) -> None
        """
        设置当前预设的局部坐标位置
        """

    def GetLocalRotation(self):
        # type: () -> Tuple[float,float,float]
        """
        获取当前预设的局部坐标旋转
        """

    def SetLocalRotation(self, rotation):
        # type: (Tuple[float,float,float]) -> None
        """
        设置当前预设的局部坐标旋转
        """

    def GetLocalScale(self):
        # type: () -> Tuple[float,float,float]
        """
        获取当前预设的局部坐标缩放
        """

    def SetLocalScale(self, scale):
        # type: (Tuple[float,float,float]) -> None
        """
        设置当前预设的局部坐标缩放
        """

    def GetWorldTransform(self):
        # type: () -> Transform
        """
        获取当前预设的世界坐标变换
        """

    def GetWorldMatrix(self):
        # type: () -> Matrix
        """
        获取世界坐标变换矩阵
        """

    def GetLocalMatrix(self):
        # type: () -> Matrix
        """
        获取局部坐标变换矩阵
        """

    def SetWorldTransform(self, transform):
        # type: (Transform) -> None
        """
        设置当前预设的世界坐标变换
        """

    def GetWorldPosition(self):
        # type: () -> Tuple[float,float,float]
        """
        获取当前预设的世界坐标位置
        """

    def SetWorldPosition(self, pos):
        # type: (Tuple[float,float,float]) -> None
        """
        设置当前预设的世界坐标位置
        """

    def GetWorldRotation(self):
        # type: () -> Tuple[float,float,float]
        """
        获取当前预设的世界坐标旋转
        """

    def SetWorldRotation(self, rotation):
        # type: (Tuple[float,float,float]) -> None
        """
        设置当前预设的世界坐标旋转
        """

    def GetWorldScale(self):
        # type: () -> Tuple[float,float,float]
        """
        获取当前预设的世界坐标缩放
        """

    def SetWorldScale(self, scale):
        # type: (Tuple[float,float,float]) -> None
        """
        设置当前预设的世界坐标缩放
        """

    def GetRootParent(self):
        # type: () -> PresetBase
        """
        获取当前预设所在的根预设
        """

    def GetParent(self):
        # type: () -> PresetBase
        """
        获取当前预设的父预设
        """

    def SetParent(self, parent):
        # type: (PresetBase) -> None
        """
        设置当前预设的父预设
        """

    def GetManager(self):
        """
        获取当前预设所在的预设管理器
        """

        return PresetManager

    def Unload(self):
        # type: () -> None
        """
        卸载当前预设
        """

    def Destroy(self):
        # type: () -> None
        """
        销毁当前预设
        """

