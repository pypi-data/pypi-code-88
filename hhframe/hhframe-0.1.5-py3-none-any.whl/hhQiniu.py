
# -*- codeing = utf-8 -*-
# @File：hhQiniu.py
# @Ver：1.1.0
# @Author：立树
# @Time：2021/6/28 15:25
# @IDE：PyCharm

"""
更新：
- 新增 qnUpload 上传策略
- 修改 qnUpload、qnFetch 返回值格式
"""

# Python SDK
# https://developer.qiniu.com/kodo/1242/python

from qiniu import Auth,BucketManager,put_file

class hhQiniu(object):

    __hhAuth = None
    __hhOpt = {
        "ak": "",
        "sk": "",
        "bucket_url": ""
    }

    def __init__(self,opt={}):
        try:
            self.__hhOpt.update(opt)
            self.__hhAuth = Auth(self.__hhOpt["ak"],self.__hhOpt["sk"])
        except Exception as err:
            print("hhframe.hhQiniu Error - ",err)

    def __Response(self,opt={}):
        hhRet = {
            "file": "",
            "url": "",
            "key": "",
            "response": {},
            "msg": ""
        }
        hhRet.update(opt)
        print("hhframe.hhQiniu Result - ",hhRet["msg"])
        return hhRet

    # 上传本地图片
    def qnUpload(self,opt={}):
        # 默认参数
        hhOpt = {
            "file": "",
            "bucket": "",
            "key": "",
            "callback": ""
        }
        hhOpt.update(opt)

        file = hhOpt["file"]
        bucket = hhOpt["bucket"]
        key = hhOpt["key"]

        # 参数判断
        if self.__hhAuth==None:
            return self.__Response({
                "msg": "上传失败，密钥无效"
            })
        if file=="" or bucket=="" or key=="":
            return self.__Response({
                "msg": "上传失败，参数异常"
            })

        # 上传
        try:
            # 生成上传 Token，可以指定过期时间等
            token = self.__hhAuth.upload_token(
                bucket=bucket,
                key=key,
                expires=3600,
                policy={
                    "returnBody": '{"key":$(key),"filename":$(fname),"filesize":$(fsize),"width":$(imageInfo.width),"height":$(imageInfo.height),"type":$(mimeType),"ext":$(ext),"imageInfo":$(imageInfo),"avinfo":$(avinfo)}'
                }
            )

            # 要上传文件的本地路径
            ret,response = put_file(token,key,file,version="v2")

            # print(ret)
            # print(response)

            return self.__Response({
                "file": file,
                "url": self.__hhOpt["bucket_url"]+ret["key"],
                "key": ret["key"],
                "response": ret,
                "msg": "上传成功" if response.status_code == 200 else "上传失败"  # 模拟的三元运算符
            })
        except Exception as err:
            return self.__Response({
                "msg": err
            })

    # 拉取网络图片
    def qnFetch(self,opt={}):
        # 默认参数
        hhOpt = {
            "url": "",
            "bucket": "",
            "key": "",
            "callback": ""
        }
        hhOpt.update(opt)

        url = hhOpt["url"]
        bucket = hhOpt["bucket"]
        key = hhOpt["key"]

        # 参数判断
        if self.__hhAuth==None:
            return self.__Response({
                "msg": "上传失败，密钥无效"
            })
        if url=="" or bucket=="" or key=="":
            return self.__Response({
                "msg": "上传失败，参数异常"
            })

        # 抓取文件
        Bucket = BucketManager(self.__hhAuth)
        ret,response = Bucket.fetch(url,bucket,key)

        # print(ret)
        # print(response)

        if response.status_code == 200:
            return self.__Response({
                "file": url,
                "url": self.__hhOpt["bucket_url"]+ret["key"],
                "key": ret["key"],
                "response": ret,
                "msg": "上传成功"
            })
        else:
            return self.__Response({
                "file": url,
                "response": ret,
                "msg": response.text_body
            })
