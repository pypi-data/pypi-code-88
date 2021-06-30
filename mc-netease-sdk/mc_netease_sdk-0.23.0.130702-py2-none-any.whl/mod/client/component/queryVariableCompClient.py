# -*- coding: utf-8 -*-

from mod.common.component.baseComponent import BaseComponent

class QueryVariableComponentClient(BaseComponent):
    def Register(self, variableName, defalutValue):
        # type: (str, float) -> bool
        """
        注册实体计算节点
        """

    def UnRegister(self, variableName):
        # type: (str) -> bool
        """
        注销实体计算节点
        """

    def Set(self, variableName, value):
        # type: (str, float) -> bool
        """
        设置某一个实体计算节点的值
        """

    def Get(self, variableName):
        # type: (str) -> float
        """
        获取某一个实体计算节点的值，如果不存在返回注册时的默认值
        """

    def GetMolangValue(self, molangName):
        # type: (str) -> float
        """
        获取实体molang变量的值
        """

