# -*- coding: utf-8 -*-

'''
键盘、鼠标、剪切板、屏幕截图控制合集
'''

from pyWebBrowser import b64decode
from pyWebBrowser import Win64Browser

class MKC:
    def __init__(self):
        self.__hook = Win64Browser.Hook()
        self.__hook.MKListen()

        self.__mkc = Win64Browser.MKC()

    # 鼠标控制
    def LeftDown(self):
        '''
        左键按下
        '''
        self.__mkc.LeftDown()
    
    def LeftUp(self):
        '''
        左键抬起
        '''
        self.__mkc.LeftUp()
    
    def LeftClick(self):
        '''
        左键单击
        '''
        self.__mkc.LeftClick()
    
    def RightDown(self):
        '''
        右键按下
        '''
        self.__mkc.RightDown()
    
    def RightUp(self):
        '''
        右键抬起
        '''
        self.__mkc.RightUp()
    
    def RightClick(self):
        '''
        右键单击
        '''
        self.__mkc.RightClick()
    
    def MiddleDown(self):
        '''
        中键按下
        '''
        self.__mkc.MiddleDown()
    
    def MiddleUp(self):
        '''
        中键抬起
        '''
        self.__mkc.MiddleUp()
    
    def MiddleClick(self):
        '''
        中键单击
        '''
        self.__mkc.MiddleClick()
    
    def Position(self) -> list:
        '''
        获取当前鼠标坐标
        '''
        return [int(x) for x in self.__mkc.Position().split(',')]

    def Move(self, x: int, y: int):
        '''
        鼠标移动
        :param x: int. 必填。x 坐标
        :param y: int. 必填。y 坐标 
        '''
        self.__mkc.Move(x, y)
    
    def SmoothMove(self, endX: float, endY: float, startX: float = -1, startY: float = -1, pointCount: int = 10, moveSpeed: int = 5):
        '''
        鼠标平滑直线移动
        :param endX      : float. 必填。终止点 x 坐标
        :param endY      : float. 必填。终止点 y 坐标
        :param startX    : float. 选填。起始点 x 坐标, 起始点 x 或 y 为 -1 时, 则以当前鼠标位置为起始点
        :param startY    : float. 选填。起始点 y 坐标, 起始点 x 或 y 为 -1 时, 则以当前鼠标位置为起始点
        :param pointCount: int. 选填。拆分点数量
        :param moveSpeed : int. 选填。移动总速度
        '''
        self.__mkc.SmoothMove(endX, endY, startX, startY, pointCount, moveSpeed)
        
    def RelativeMove(self, offsetX: float = 0, offsetY: float = 0, pointCount: int = 10, moveSpeed: int = 5):
        '''
        鼠标相对平滑移动
        :param offsetX   : int. 选填。x 坐标的相对偏移量
        :param offsetY   : int. 选填。y 坐标的相对偏移量
        :param pointCount: int. 选填。拆分点数量
        :param moveSpeed : int. 选填。移动总速度
        '''
        x, y = self.Position()
        endX = x + offsetX
        endY = y + offsetY

        self.SmoothMove(endX, endY, float(x), float(y), pointCount, moveSpeed)

    # 键盘控制
    def KeyDown(self, keyName: str = None, keyValue: int = -1):
        '''
        键盘按键按下
        :param keyName : str. 非必填但 keyName/keyValue 必填一个。键盘按键值
        :param keyValue: int. 非必填但 keyName/keyValue 必填一个。键盘按键 ASCII 值
        '''
        
        self.__mkc.KeyDown(keyName, keyValue)
    
    def KeyUp(self, keyName: str = None, keyValue: int = -1):
        '''
        键盘按键弹起
        :param keyName : str. 非必填但 keyName/keyValue 必填一个。键盘按键值
        :param keyValue: int. 非必填但 keyName/keyValue 必填一个。键盘按键 ASCII 值
        '''
        
        self.__mkc.KeyUp(keyName, keyValue)
    
    def KeyPress(self, keyName: str = None, keyValue: int = -1):
        '''
        键盘按键单击
        :param keyName : str. 非必填但 keyName/keyValue 必填一个。键盘按键值
        :param keyValue: int. 非必填但 keyName/keyValue 必填一个。键盘按键 ASCII 值
        '''
        
        self.__mkc.KeyPress(keyName, keyValue)
    
    def KeyCombination(self, keyNameList: list = None, keyValueList: list = None, clickWaitTime: int = 10):
        '''
        键盘组合按键。组合按键执行顺序为列表索引顺序
        :param keyNameList  : list. 元素数据类型为 str. 非必填但 keyNameList/keyValueList 必填一个。键盘按键值列表
        :param keyValueList : list. 元素数据类型为 int. 非必填但 keyNameList/keyValueList 必填一个。键盘按键 ASCII 值列表
        :param clickWaitTime: int. 按键执行间隔时间
        '''
        
        self.__mkc.KeyCombination(keyNameList, keyValueList, clickWaitTime)

    # 剪切板
    def SetClipboard(self, data: str):
        '''
        设置剪切板内容
        :param data: str. 需要存入剪切板的文本数据
        '''
        return self.__mkc.SetClipboard(data)
    
    def GetClipboard(self):
        '''
        获取剪切板内容
        :return 当前剪切板的文本数据
        '''
        return self.__mkc.GetClipboard()
    
    # 屏幕截图
    def Screenshot(self, startX: int, startY: int, endX: int, endY: int) -> bytes:
        '''
        任意尺寸屏幕截图
        :param startX: int. 截图起始点 x 坐标
        :param startY: int. 截图起始点 y 坐标
        :param endX  : int. 截图终止点 x 坐标
        :param endY  : int. 截图终止点 y 坐标
        :return bytes. 返回二进制图片类型
        '''
        base64 = self.__mkc.AnySize(startX, startY, endX, endY)
        return b64decode(base64.replace('data:image/png;base64,', ''))
