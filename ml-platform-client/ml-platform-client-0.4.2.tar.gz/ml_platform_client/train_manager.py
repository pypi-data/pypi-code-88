from multiprocessing import Manager

from .config import client_config
from .constants import MODE_CLUSTER, TRAIN_STATUS_UNKNOWN
from .mysql_accessor import MysqlAccessor


class TrainManager:
    def __init__(self):
        manager = Manager()
        self.train_status_mapping = manager.dict()

    def update(self, model_id, status):
        self.train_status_mapping[model_id] = status

    def check(self, model_id):
        if model_id in self.train_status_mapping:
            return self.train_status_mapping[model_id]
        if client_config.mode == MODE_CLUSTER:
            return MysqlAccessor.get_model_train_status(model_id)
        return TRAIN_STATUS_UNKNOWN


train_manager = TrainManager()
