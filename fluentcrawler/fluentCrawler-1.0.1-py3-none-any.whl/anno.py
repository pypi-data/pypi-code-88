
class TimeUtil:
    secend=1
    min=60
    hour=3600
    day=86400
    week=604800
    month=2626560
    year=31536000




def isNews(*args):
    def wrapper(cls):
        #将爬虫设置为新闻类爬虫
        cls.isNews=True
        #同时把url加入进来
        cls.startUrl=args
        return cls
    return wrapper

def sched(schedNum, timeUtil):
    def wrapper(cls):
        #直接设置循环时间
        cls.schedTime=schedNum*timeUtil
        return cls
    return wrapper



def TargetUrl(selectType=None, xpath=None):
    def wrapper(cls):
        # 设置regex  或者 css  或者xpath 去抽取 中间url  ，css和 regex 做保留，后面再写
        if (xpath is not None):
            cls.TargetUrl_Xpath = xpath
        # if (regex is not None):
        #     cls.TargetUrl_Regex = regex
        # if (css is not None):
        #     cls.TargetUrl_Css = css
        # if (selectType is not None):
        #     cls.TargetUrl_SelectType = selectType

        return cls

    return wrapper


def HelpUrl(selectType=None, xpath=None):
    def wrapper(cls):
        # 设置url  或者 css  或者xpath 去抽取 中间url
        if (xpath is not None):
            cls.HelpUrl_Xpath = xpath
        # if (regex is not None):
        #     cls.HelpUrl_Regex = regex
        # if (css is not None):
        #     cls.HelpUrl_Css = css
        # if (selectType is not None):
        #     cls.HelpUrl_SelectType = selectType
        return cls

    return wrapper