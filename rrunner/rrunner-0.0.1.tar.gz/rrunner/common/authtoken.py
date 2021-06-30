import base64
import hmac
import hashlib
import urllib.parse
import time


# 调用第三方接口时获取authontokn的类
class AuthonToken:
    def __init__(self):
        self.key = "111111"
        self.key1 = "HYWVOQ6wszJrXMmVnnKN1ngLWnafnDVP"
        self.key2 = "cEQT3SysXk94ozxJFSbuqnS5u4z6aHSd"
        self.timeStamp = time.strftime("%Y%m%d%H%M%S")

    def sort(self, params):
        # 对参数进行排序
        aa = sorted(params.items(), key=lambda d: d[0], reverse=False)
        # 排序后的数据转换成字典格式
        params = dict(aa)
        # 字符串拼接
        b = ""
        for k in params.keys():
            a = k + "=" + params[k] + "&"
            b = b + a
        # 去掉字符串最后面的&
        b = b[:-1]
        return b

    def hmac_sha256(self, key, value):
        """
        hmacsha256加密
        return:加密结果转成16进制字符串形式
        """
        message = value.encode('utf-8')
        return hmac.new(key.encode('utf-8'), message, digestmod=hashlib.sha256).digest()

    def base_64(self, value):
        """
        base64加密
        return:加密结果转成16进制字符串形式
        """
        return base64.b64encode(value).decode('utf-8')


authon = AuthonToken()
