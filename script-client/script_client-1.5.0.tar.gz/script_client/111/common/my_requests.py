
"""
my requests
"""

import requests
from loguru import logger

class MyRequests:
    """
    封装requests
    """
    def __init__(self, timeout=6):
        """
        init
        :param timeout: 超时时间
        """
        self.timeout = timeout

    def get(self, url, **DataAll):
        """
        get请求
        :param url: url
        :param DataAll:all data
        :return:text
        """
        params = DataAll.get('params')
        headers = DataAll.get('headers')
        try:
            resp = requests.get(url=url, params=params, headers=headers, timeout=self.timeout)
            return resp
        except Exception as ex:
            # logger.error(f"url={url}")
            # logger.error(f"headers={headers}")
            # logger.error(f"params={params}")
            # logger.error(str(ex))
            return f"err = {ex}"

    def post(self, url, **DataAll):
        '''
        post请求
        :param url: url
        :param DataAll:all data
        :return:text
        '''
        params = DataAll.get('params')
        headers = DataAll.get('headers')
        data = DataAll.get('data')
        json = DataAll.get('json')
        files = DataAll.get('files')
        try:
            resp = requests.post(url=url, params=params, headers=headers, data=data,
                                 json=json, files=files, timeout=self.timeout)
            return resp
        except Exception as ex:
            # logger.error(f"url={url}")
            # logger.error(f"headers={headers}")
            # logger.error(f"params={params}")
            # logger.error(f"data={data}")
            # logger.error(f"json={json}")
            # logger.error(f"files={files}")
            # logger.error(str(ex))
            return f"{ex}"

    def run(self, url, method, **DataAll):
        """
        run
        :param url: url
        :param method: post or get
        :param DataAll: all data
        :return: resp
        """
        resp = None
        method = method.lower()
        if method == 'get':
            resp = self.get(url, **DataAll)
        elif method == 'post':
            resp = self.post(url, **DataAll)
        else:
            logger.error("method的值不正确")
        return resp


##############################################################################
if __name__ == '__main__':
    url = ''
    headers = {
        'Content-Type': 'application/json;charset=utf-8',
    }
    json={}
    mr = MyRequests()
    t = mr.run(url=url, method='post', json=json, headers=headers)
    print(t.status_code)
    print(t.json())

