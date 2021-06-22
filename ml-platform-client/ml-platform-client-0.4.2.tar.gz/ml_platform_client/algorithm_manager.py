import logging
import os
import threading
from queue import Queue
from threading import Semaphore

from flask import request

from .api_util import catch_exception
from .config import client_config
from .constants import MODE_CLUSTER
from .context import request_context
from .mysql_accessor import MysqlAccessor
from .service_response import success_response_with_data, format_service_response, success_response
from .train_manager import train_manager
from .validation.exceptions import ArgValueError


class AlgorithmManager:
    def __init__(self):
        self.alg_mapping = {}
        self.alg_offline_mapping = {}
        self.train_queue = Queue(int(os.environ.get('MLP_TRAIN_QUEUE_SIZE', 100)))
        self.semaphore = Semaphore(int(os.environ.get('MLP_TRAIN_TASK_NUM', 5)))

    def register(self, name, algorithm):
        self.alg_mapping[name] = algorithm

    def unregister(self, name):
        del self.alg_mapping[name]

    @catch_exception
    def train(self, algorithm, model_path, data_config, parameters, extend):
        if algorithm not in self.alg_mapping:
            raise ArgValueError(message='algorithm [{}] not support'.format(algorithm))
        extend['remote_ip'] = request.remote_addr

        model_id = self.alg_mapping[algorithm].generate_model_id(extend)
        self.train_queue.put({
            'args': (algorithm, model_id, model_path, data_config, parameters, extend, request_context.uuid)
        })

        train_manager.update(model_id, 'init')
        if client_config.mode == MODE_CLUSTER:
            MysqlAccessor.update_model_train_status(model_id, 'inactive')
        return format_service_response(success_response_with_data({'model_id': model_id}))

    def _update_model_status(self, model_id, status):
        if client_config.mode == MODE_CLUSTER:
            MysqlAccessor.update_model_train_status(model_id, status)

    def _train_async(self, uuid, algorithm, model_id, model_path, data_config, parameters, extend):
        try:
            train_manager.update(model_id, 'training')
            request_context.uuid = uuid
            result = self.alg_mapping[algorithm].train(model_id, model_path, data_config, parameters, extend)
            if result is False:
                logging.info('train model [{}] failed'.format(model_id))
                train_manager.update(model_id, 'error')
            else:
                logging.info('train model [{}] success'.format(model_id))
                train_manager.update(model_id, 'completed')
        except Exception as e:
            logging.error(e)
            logging.error('train model [{}] failed'.format(model_id))
            train_manager.update(model_id, 'error')
        finally:
            # 执行完成后释放锁
            self.semaphore.release()

    @catch_exception
    def status(self, algorithm, model_id):
        status = self.alg_mapping[algorithm].status(model_id)
        return format_service_response(success_response_with_data({'status': status}))

    @catch_exception
    def delete(self, algorithm, model_uid):
        self.alg_mapping[algorithm].delete(model_uid)
        return format_service_response(success_response())

    def start(self):
        t = threading.Thread(target=self.loop)
        t.start()

    def loop(self):
        while True:
            train_data = self.train_queue.get()
            algorithm, model_id, model_path, data_config, parameters, extend, uuid = train_data['args']
            p = threading.Thread(target=self._train_async,
                                 args=(uuid, algorithm, model_id, model_path, data_config, parameters, extend))

            # 训练进程启动前获取锁
            self.semaphore.acquire()
            p.start()


alg_manager = AlgorithmManager()
