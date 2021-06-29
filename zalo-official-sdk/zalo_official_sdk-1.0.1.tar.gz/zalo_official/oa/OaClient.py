import json
import time

import requests

from zalo_official import APIConfig
from zalo_official.APIException import APIException
from zalo_official.ApiBaseClient import ApiBaseClient
from zalo_official.utils.MacUtils import MacUtils

"""
TODO: 
Description here
"""


class OaClient(ApiBaseClient):
    def __init__(self, oa_info):
        self.oa_info = oa_info

    def get(self, url, data):
        endpoint = "%s/%s/oa/%s" % (APIConfig.DEFAULT_OA_API_BASE, APIConfig.DEFAULT_OA_API_VERSION, url)
        params = self.create_oa_params(data, self.oa_info)
        return self.send_request(endpoint, params, 'GET')

    def post(self, url, data):
        endpoint = "%s/%s/oa/%s" % (APIConfig.DEFAULT_OA_API_BASE, APIConfig.DEFAULT_OA_API_VERSION, url)
        params = self.create_oa_params(data, self.oa_info)

        if 'file' in data:
            timestamp = int(round(time.time() * 1000))
            file = self.load_file(data['file'])
            params['mac'] = MacUtils.build_mac(self.oa_info.oa_id, timestamp, self.oa_info.secret_key)
            return self.upload_file(endpoint, params, file)
        else:
            return self.send_request(endpoint, params, 'POST')

    def load_file(self, path):
        if 'http' in path:
            file = requests.get(path, stream=True).content
        else:
            file = open(path, 'rb').read()
        if len(file) > APIConfig.MAXIMUM_FILE_SIZE:
            raise APIException("file size exceeded the maximum size permitted")
        return file
