# 基本爬取模板
import hashlib
import time
import traceback
import urllib
from queue import Queue
from threading import Timer

import requests
import urllib3
from gerapy_auto_extractor import extract_list
from gne import GeneralNewsExtractor
from lxml import etree
from requests import Request, sessions
from retrying import retry
from w3lib.url import canonicalize_url

from com.common.util.joinUtil import absUrl

urllib3.disable_warnings()


def xpath(xpathStr):
    return xpathStr


# 自动抽取下一页算法
def extract_next(curHtmlStr):
    _element = etree.HTML(curHtmlStr)
    # 获取下一页,现在只能做最简单的规则，后面再完善下一页的规则匹配算法
    # 先找有没有下一页的 a标签
    xpath = '//a[text()="下一页"]/@href'
    hrefs = _element.xpath(xpath)
    return hrefs


class BaseModel:
    count = 0

    cache = set()
    sleepTime = 1

    ListQueue = Queue()
    ContextQueue = Queue()
    # 这里还是不保存到集合中了.
    # ListPageResult=set()
    # ContextPageResult=set()
    curHtmlStr = ""
    curRes = None
    curReq = None
    # 当前的data
    curData = None

    def __init__(self):
        pass

    def urls(self, *args):
        [self.addListSeed(url) for url in args]
        return self

    def setSleepTime(self, times):
        self.sleepTime = times
        return self

    def genStartSeed(self):
        pass

    # @retry(stop_max_attempt_number=3)  # 重试三次
    def BaseReq(self, req):
        if (req.method is None): req.method = "GET"
        # if(req.headers is None) :req.headers=get_headers()
        with sessions.Session() as session:
            res = session.send(session.prepare_request(req), verify=False)
        # res = session.send(session.prepare_request(req), verify=False)
        time.sleep(self.sleepTime)
        self.curReq = req
        self.curRes = res
        self.curHtmlStr = res.content.decode()

    # 解析列表页 产生内容页链接
    def ParseListPage(self):
        # 读取列表页的属性
        targetXpath = self.TargetUrl_Xpath
        # 根据xpath 获取url
        _element = etree.HTML(self.curHtmlStr)
        hrefs = _element.xpath(targetXpath)
        [self.addContextSeed(absUrl(self.curReq.url, i)) for i in hrefs]

    # 前置处理器处理list
    def postProcessBeforeList(self):
        pass

    # 后置处理器处理list
    def postProcessAfterList(self):
        pass

    def postProcessBeforeContext(self):
        pass

    def postProcessAfterContext(self, result):
        pass

    # 解析单个页 产生内容
    def ParseContextPage(self):
        # 解析内容页
        # 获取所有的属性
        PageField = self.getClsFieldAndVal()
        # 遍历解析内容页 并返回结果
        _element = etree.HTML(self.curHtmlStr)
        item = {}
        for k in PageField:
            item[k] = "".join(_element.xpath(PageField[k]))
        return item

    def getClsFieldAndVal(cls):
        s = ["startUrl", "isNews", "schedNum", "TargetUrl_Xpath", "HelpUrl_Xpath", "count", "cache", "sleepTime",
             "ListQueue", "ContextQueue", "curHtmlStr", "curRes", "curReq", "curData"]

        PageField = {}
        for a in dir(cls):
            if not str(a).startswith('_') and not callable(getattr(cls, a)):
                if s.__contains__(str(a)): continue
                PageField[str(a)] = getattr(cls, str(a))
        return PageField

    # 解析传入的页面，产生下一页链接
    def genNextPageReq(self):
        helpXpath = self.HelpUrl_Xpath
        # 根据xpath 获取url
        _element = etree.HTML(self.curHtmlStr)
        hrefs = _element.xpath(helpXpath)
        [self.addListSeed(absUrl(self.curReq.url, i)) for i in hrefs]

    # 默认的save方法去保存
    def save(self, result):
        # 这是一个结果，需要为 dict 类型
        # result = {'name': 'crawlab'}
        # 调用保存结果方法
        print(result)
        # save_item(result)
        pass

    def crawler(self):
        try:
            print(self.__class__.__name__ + "爬虫运行开始")
            time_start = time.time()
            # 调用起始种子
            self.genStartSeed()

            # 采集列表页数据
            while (self.ListQueue.qsize() > 0):
                req = self.ListQueue.get()
                self.BaseReq(req)  # 消费一个种子
                self.postProcessBeforeList()
                self.ParseListPage()  # 解析页面
                self.postProcessAfterList()
                self.genNextPageReq()

                while (self.ContextQueue.qsize() > 0):
                    # 消费一个内容页种子
                    self.BaseReq(self.ContextQueue.get())
                    # 调用前置处理器 对req 做前置处理
                    self.postProcessBeforeContext()
                    # 解析内容页
                    result = self.ParseContextPage()
                    # 调用后置处理器  对 result 做后置处理
                    self.postProcessAfterContext(result)
                    # 保存方法,默认实现是 insert 到 data表
                    self.save(result)

            time_end = time.time()
            print(self.__class__.__name__ + "爬虫运行完毕  运行时间: " + str((time_end - time_start)) + "新增数据:" + str(
                self.count) + "条")
        except Exception as ex:
            print(self.__class__.__name__ + "爬虫运行出现异常%s" % ex)
            print(traceback.print_exc())


    def run(self):
        self.crawler()
        # 判断有没有 schedTime 没有的话 直接跑crawler
        if hasattr(self, 'schedTime'):
            # 获取当前定时任务的时间
            t = Timer(self.schedTime, self.run)
            # 执行定时任务
            t.start()

    def addListSeed(self, url, **kwargs):

        if (not kwargs.__contains__("method")):
            if (kwargs.__contains__("data")):
                kwargs['method'] = "POST"
            else:
                kwargs['method'] = "GET"

        req = Request(url=url, **kwargs)
        if self.fingerprint(req):
            print("增加列表页种子" + url)
            self.ListQueue.put(req)

    def addContextSeed(self, url, **kwargs):
        if not kwargs.__contains__("method"):  kwargs['method'] = "GET"
        req = Request(url=url, **kwargs)
        if self.fingerprint(req):
            print("增加内容页种子" + url)
            self.ContextQueue.put(req)

    """
    fingerprint Check  if cache already contains fingerprintKey  return False 
    else return False
    """

    def fingerprint(self, req):
        fp = hashlib.sha1()
        """计算指纹时，请求方法(如GET、POST)被计算在内"""
        fp.update(str(req.method).encode('utf-8'))
        """canonicalize_url()将url规范化 这样参数位置变化，但参数值不变的网址，表示的仍是同一个网址 """
        fp.update(canonicalize_url(str(req.url)).encode('utf-8'))
        if req.data is not None:
            fp.update(urllib.parse.urlencode(req.data).encode('utf-8'))
        fingerprintKey = fp.hexdigest()
        if self.cache.__contains__(fingerprintKey):
            return False
        self.cache.add(fingerprintKey)
        return True
