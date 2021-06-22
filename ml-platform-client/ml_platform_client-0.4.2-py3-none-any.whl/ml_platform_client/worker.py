import json
import traceback
from collections import defaultdict

from .context import request_context
from .logger import log


class Worker:
    def __init__(self):
        super(Worker, self).__init__()
        self.model_pool = {}
        self.alg_mapping = {}
        self.registry = defaultdict(list)

    def work(self, command, data):
        if command == 'exit':
            return
        try:
            result = self._process(command, data)
        except Exception as e:
            result = False, None
            log.error('worker process error: {}, {}'.format(command, e))
            traceback.print_exc()
        return result

    def _process(self, command, data):
        if command == 'load':
            return self._process_load(data)
        if command == 'unload':
            return self._process_unload(data)
        if command == 'predict':
            return self._process_predict(data)
        if command == 'init_alg':
            return self._process_init_alg(data)
        if command == 'remove_alg':
            return self._process_remove_alg(data)
        return False, None

    def _process_remove_alg(self, alg):
        del self.alg_mapping[alg]
        model_ids = self.registry[alg]
        for model_id in model_ids:
            del self.model_pool[model_id]
        self.registry[alg].clear()

    def _process_init_alg(self, data):
        self.alg_mapping.update(data)

    def _process_load(self, data):
        model_id = data['model_id']
        model_path = data['model_path']
        algorithm = data['algorithm']
        if algorithm not in self.alg_mapping:
            return False, 'algorithm not support'

        try:
            model = self.alg_mapping[algorithm].load(model_id, model_path)
            self.model_pool[model_id] = model
            self.registry[algorithm].append(model_id)
            return True, None
        except Exception as e:
            log.error('load fail', e)
            log.error(traceback.format_exc())
            return False, 'load fail {}'.format(e)

    def _process_unload(self, data):
        try:
            model_id = data['model_id']
            algorithm = data['algorithm']
            self.alg_mapping[algorithm].unload(model_id)
            self.registry[algorithm].remove(model_id)
            if model_id in self.model_pool:
                del self.model_pool[model_id]
            return True, None
        except Exception as e:
            log.error('unload fail', e)
            log.error(traceback.format_exc())
            return False, 'unload fail {}'.format(e)

    def _process_predict(self, data):
        model_id = data['model_id']
        features = data['features']
        params = data['params']
        uuid = data['uuid']
        request_context.uuid = uuid
        if model_id not in self.model_pool:
            message = 'model [{}] not loaded'.format(model_id)
            log.warn(message)
            return False, message

        try:
            prediction = self.model_pool[model_id].predict(features, params)
            log.info('[{}]model: {}, features: {}, prediction: {}, params: {}'
                     .format(uuid, model_id,
                             json.dumps(features, ensure_ascii=False),
                             json.dumps(prediction, ensure_ascii=False),
                             json.dumps(params, ensure_ascii=False)))

            return True, prediction
        except Exception as e:
            log.error('predict fail', e)
            log.error(traceback.format_exc())
            return False, 'predict fail {}'.format(e)
        finally:
            request_context.uuid = None
