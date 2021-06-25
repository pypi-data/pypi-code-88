# @Time    : 2021/6/7 18:13
# @Author  : Boyang
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm
from mlflow.projects.backend.abstract_backend import AbstractBackend


class WaveletAiBackend(AbstractBackend):
    def run(self, project_uri, entry_point, params, version, backend_config, tracking_uri, experiment_id):
        print('进来了')
        print('哈哈哈哈哈哈哈')
