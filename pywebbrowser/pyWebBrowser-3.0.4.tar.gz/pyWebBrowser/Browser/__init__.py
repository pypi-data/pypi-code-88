# -*- coding: utf-8 -*-

'''
浏览器控制
'''

from pyWebBrowser import datetime
from pyWebBrowser import sleep
from pyWebBrowser import path
from pyWebBrowser import loads
from pyWebBrowser import etree
from pyWebBrowser import math
from pyWebBrowser import Win64Browser
from pyWebBrowser import MKC

class Browser:
    def __init__(self):
        self.__browser = Win64Browser.Browser()

    def Create(self, width: int = 1360, height: int = 768, topMost: bool = False):
        '''
        创建浏览器界面。
        同一进程仅支持创建一个浏览器界面。如有多浏览器界面需求可根据 gitee 网站中源码自行修改。
        Yogurt 可能在未来的一段时期内不会就此方案进行变更。
        如有分布式多设备集群采集需求的, 暂时可自行开发或寻找控制系统。
        未来可能会就此需求进行开发, 敬请期待。
        :param width  : int.  选填。窗体宽度。默认 1360
        :param height : int.  选填。窗体高度。默认 768
        :param topMost: bool. 选填。窗体置顶状态。默认 False。True: 置顶; False: 不置顶
        '''
        self.__browser.Create(width, height, topMost)

    def Location(self) -> list:
        '''
        获取当前浏览器窗口坐标
        :return list. 返回格式 [x, y, width, height]
        '''
        return [int(x) for x in self.__browser.Location().split(',')]

    def Open(self, url: str):
        '''
        打开指定网页链接
        :param url: str. 必填。网页链接
        '''
        self.__browser.Open(url)
    
    def Refresh(self):
        '''
        刷新当前页面
        '''
        self.__browser.Refresh()

    def Url(self) -> str:
        '''
        获取当前页面 Url
        如果页面 Url 会随着页面的交互的变化而变化, 则需要在执行完交互操作后, 再次执行获取 Url
        '''
        return self.__browser.Url()

    def DownLoad(self, url: str, downloadPath: str, timeout: int = 30) -> bool:
        '''
        下载文件
        在 Yogurt 的设定中, 该功能仅用于下载 2MB 以内的文件, 例如: 图片、文档等。
        因此未对中大型文件进行等待或断点续传等方面的处理, 不建议以此下载中大型文件
        :param url         : str. 必填。下载链接
        :param downloadPath: str. 必填。保存路径, 含文件名称
        :param timeout     : int. 选填。超时时间, 单位为秒。默认为 30 秒
        :return bool. 返回下载状态, True: 下载成功; False: 下载失败
        '''
        self.__browser.Download(url, downloadPath)
        current = datetime.now()
    
        while (datetime.now() - current).seconds < timeout:
            if path.exists(downloadPath): return True
            sleep(0.1)
        
        return False
    
    def FrameCount(self) -> int:
        '''
        获取当前网页框架数量(含主页面), 数量至少为 1
        :return int. 返回当前页面框架数量(含主页面)
        '''
        return self.__browser.FrameCount()

    def Html(self, frameIndex: int = 0) -> etree._Element:
        '''
        获取网页源代码
        :param frameIndex: int. iframe 顺序号。默认为 0, 即主页面
        :return object. 返回指定框架源代码, 如 frameIndex <= 0, 则返回主页面源代码, 转成 etree.HTML, 转换失败则返回源代码字符串
        '''
        html = self.__browser.Html(frameIndex)
        try:
            htmlObj = etree.HTML(html)
            return htmlObj
        except:
            return html

    def WaitByElement(self, xpath: str, timeout: int = 5) -> bool:
        '''
        等待指定元素加载完毕
        :param xpath  : str. 必填。用于寻找指定元素的 XPath 语句, 仅限于主页面。
        :param timeout: int. 选填。超时时间, 单位为秒。默认为 5 秒
        :return bool. 返回加载状态. True: 加载已完成; False: 加载失败
        '''
        current = datetime.now()
        while (datetime.now() - current).seconds < timeout:
            html = self.Html()

            if type(html) == etree._Element:
                if len(html.xpath(xpath)) > 0:
                    return True
            sleep(0.1)

        return False

    def ElementLocation(self, xpath: str) -> list:
        '''
        获取指定元素位置。仅支持主页面, 如需操作 iframe 可使用 ExecJS 自行编写语句。
        :param xpath: str. 必填。定位元素的 xpath 语句。
        :return list. 返回 xpath 指定元素的坐标信息字符串。格式: [[x, y, width, height]]
        '''
        json = self.__browser.ElementLocation(xpath)
        return loads(json)

    def ExecJS(self, query: str):
        '''
        执行 javaScript 语句
        :param query: str. 必填。需要执行的 javaScript 语句
        :return object. 返回执行语句的结果
        '''
        return self.__browser.ExecJS(query)

    def ElementTouch(self, MKC: MKC, xpath: str, ):
        '''
        鼠标移动到元素的位置。
        xpath 的返回值为多个结果时, 仅执行第一个
        :param MKC  : MKC. 必填。键鼠控制对象
        :param xpath: str. 必填。用于寻找指定元素的 XPath 语句, 仅限于主页面。
        '''

        self.ExecJS('window.scrollTo(0, 0)')
        elementLocationList = self.ElementLocation(xpath)
        if len(elementLocationList) > 0:
            browserX, browserY, browserWidth, browserHeight = self.Location()
            x, y, width, height = elementLocationList[0]

            offsetX, offsetY = 0, 0

            innerX = x - browserX
            if innerX + int(width / 2) >= browserWidth:
                scrollX = (math.ceil((innerX / browserWidth)) - 1) * browserWidth
                offsetX = (innerX - scrollX) / 2 + scrollX - int(width / 2)

            innerY = y - browserY
            if innerY + int(height / 2) >= browserHeight:
                scrollY = (math.ceil((innerY / browserHeight)) - 1) * browserHeight
                offsetY = (innerY - scrollY) / 2 + scrollY - int(height / 2)

            self.ExecJS('window.scrollTo({offsetX}, {offsetY})'.format(offsetX = offsetX, offsetY = offsetY))
        
        sleep(0.1)

        elementLocationList = self.ElementLocation(xpath)
        if len(elementLocationList) > 0:
            x, y, width, height = elementLocationList[0]
            MKC.SmoothMove(x + int(width / 2), y + int(height / 2))

    def InputData(self, MKC: MKC, xpath: str, data: str, mode: str = 'C'):
        '''
        在 xpath 执行位置输入内容。
        xpath 的返回值为多个结果时, 仅执行第一个
        :param MKC  : MKC. 必填。键鼠控制对象
        :param xpath: str. 必填。用于寻找指定元素的 XPath 语句, 仅限于主页面。
        :param data : str. 必填。需要输入字符串
        :param mode : str. 选填。输入模式。默认为 C。C: 剪切板, 绝大多数使用场景可用; K: 键盘输入, 少部分密码、验证码场景使用, 仅支持输入键盘按键
        '''

        self.ElementTouch(MKC, xpath)
        sleep(0.1)
        MKC.LeftClick()

        mode = mode.upper()
        if mode == 'C':
            MKC.SetClipboard(data)
            sleep(0.1)
            MKC.KeyCombination(['CTRL', 'V'])
        elif mode == 'K':
            sleep(0.1)
            for item in data:
                self.__inputDataKeyInput(MKC, item)
                sleep(0.05)
    
    def __inputDataKeyInput(self, MKC: MKC, keyName: str):
        keyCodeDict = {
            'a': 65,       'j': 74,       's': 83,       '1': 49,       ';': 186,       ']': 221,
            'b': 66,       'k': 75,       't': 84,       '2': 50,       '=': 187,      '\'': 222,
            'c': 67,       'l': 76,       'u': 85,       '3': 51,       ',': 188,       ' ': 32,
            'd': 68,       'm': 77,       'v': 86,       '4': 52,       '-': 189,
            'e': 69,       'n': 78,       'w': 87,       '5': 53,       '.': 190,
            'f': 70,       'o': 79,       'x': 88,       '6': 54,       '/': 191,
            'g': 71,       'p': 80,       'y': 89,       '7': 55,       '`': 192,
            'h': 72,       'q': 81,       'z': 90,       '8': 56,       '[': 219,
            'i': 73,       'r': 82,       '0': 48,       '9': 57,      '\\': 220,
            'A': [16, 65], 'J': [16, 74], 'S': [16, 83], '!': [16, 49], ':': [16, 186], '}': [16, 221],
            'B': [16, 66], 'K': [16, 75], 'T': [16, 84], '@': [16, 50], '+': [16, 187], '"': [16, 222],
            'C': [16, 67], 'L': [16, 76], 'U': [16, 85], '#': [16, 51], '<': [16, 188],
            'D': [16, 68], 'M': [16, 77], 'V': [16, 86], '$': [16, 52], '_': [16, 189],
            'E': [16, 69], 'N': [16, 78], 'W': [16, 87], '%': [16, 53], '>': [16, 190],
            'F': [16, 70], 'O': [16, 79], 'X': [16, 88], '^': [16, 54], '?': [16, 191],
            'G': [16, 71], 'P': [16, 80], 'Y': [16, 89], '&': [16, 55], '~': [16, 192],
            'H': [16, 72], 'Q': [16, 81], 'Z': [16, 90], '*': [16, 56], '{': [16, 219],
            'I': [16, 73], 'R': [16, 82], ')': [16, 48], '(': [16, 57], '|': [16, 220],            
        }

        keyCode = keyCodeDict[keyName]
        if type(keyCode) == int:
            MKC.KeyPress(keyValue = keyCode)
        elif type(keyCode) == list:
            MKC.KeyCombination(keyValueList = keyCode)

    def Close(self):
        '''
        关闭浏览器
        '''
        self.__browser.Close()
