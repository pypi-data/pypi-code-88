import os

import allure
import requests
from rrunner.common.handle_config import config
from rrunner.common.handle_data import replace_data

from random import randint

# 封装请求和断言
from rrunner.common.handle_path import DATA_DIR


class RequestsAssert():
    @staticmethod
    # 定义一个请求静态方法，传入的参数item为测试数据，headers为请求header
    def apiRequest(item, headers):
        allure.dynamic.title(item["title"])
        # 从配置文件中取url，和excel中的url拼接成一个完成的url
        url = config.get("env", "base_url") + item["url"]
        # 获取excel中接口请求的方法
        method = item["method"]
        headers = headers
        if item["data"] != None and item["data"] != {}:
            # 调用replace_data方法，替换excel中用#xxx#表示的参数
            param = replace_data(RequestsAssert, item["data"])
            # 取出来的param为string类型，eval去掉'',将param转换成字典类型
            params = eval(param)
            if item["content-type"] == "json":
                res = requests.request(method=method, url=url, json=params, headers=headers).json()
            if item["content-type"] == "params":
                res = requests.request(method=method, url=url, params=params, headers=headers).json()
            if item["content-type"] == "data":
                res = requests.request(method=method, url=url, data=params, headers=headers).json()
            if item["content-type"] == "file":
                # 上传文件时file_path中传入文件存放地址
                file_name = params["file_name"]
                upload_file_path = os.path.join(DATA_DIR, file_name)
                # 上传文件的文件数据
                file_data = {"file": open(upload_file_path, "rb")}
                # 判断上传文件时是否需要添加参数
                # 上传文件时upload_data中传入需要参数
                if "upload_data" in params.keys():
                    upload_data = params["upload_data"]
                    res = requests.request(method=method, url=url, files=file_data, data=upload_data,
                                           headers=headers).json()
                else:
                    res = requests.request(method=method, url=url, files=file_data, headers=headers).json()
                    print(res)
            if item["content-type"]=="stream":
                r=requests.get(url=url, headers=headers)
                excel_name="导出文件"+item["interface"].split("/")[1]+".xls"
                with open(os.path.join(DATA_DIR, excel_name), "wb") as fp:
                    fp.write(r.content)
                res=r.content
        else:
            res = requests.request(method=method, url=url, headers=headers).json()
        return res

    @staticmethod
    # 定义一个断言静态方法，传入的参数res为请求返回的结果，item为测试数据，将self.excel.write_excel当成write变量来传入
    def apiAssert(res, item, write):
        expected = eval(item["expected"])
        row = int(item["case_id"]) + 1
        # 断言实际返回的code和期望返回的code是否相等
        try:
            if "innerCode" in expected:
                assert res["innerCode"] == expected["innerCode"]
            if "message" in expected:
                assert res["message"] == expected["message"]
        except AssertionError as e:
            write(row=row, column=10, value="失败")
            raise e
        else:
            write(row=row, column=10, value="通过")


RequestsAssert = RequestsAssert()
