from datetime import datetime

from prometheus_client import Gauge, push_to_gateway, Counter, CollectorRegistry

labels_list = ['application', 'kubernetes_pod_name', 'env']


class MetricsClient:

    def __init__(self, push_gateway, env, service_name, job_name, pod_name):
        self.push_gateway = push_gateway
        self.env = env
        self.service_name = service_name
        self.job_name = job_name
        self.pod_name = pod_name
        self.registry = CollectorRegistry()

    def push_start_metric(self):
        self.push_counter_metric('start', 'Training started')
        pass

    def push_end_metric(self):
        self.push_counter_metric('end', 'Training ended')
        pass

    def meter_pu_size(self, size):
        self.push_gauge_metric('pu_size', 'Pu matrix size', size)
        pass

    def meter_qi_size(self, size):
        self.push_gauge_metric('qi_size', 'Qi matrix size', size)
        pass

    def meter_bi_size(self, size):
        self.push_gauge_metric('bi_size', 'Bi matrix size', size)
        pass

    def meter_item_dict_size(self, size):
        self.push_gauge_metric('item_dict_size', 'Item dict size', size)
        pass

    def meter_user_dict_size(self, size):
        self.push_gauge_metric('user_dict_size', 'User dict size', size)
        pass

    def meter_reverse_item_dict_size(self, size):
        self.push_gauge_metric('reverse_item_dict_size', 'Reverse item dict size', size)
        pass

    def push_counter_metric(self, name, documentation):
        c = Counter(name, documentation, labels_list, registry=self.registry)
        c.labels(self.service_name, self.pod_name, self.env).inc()
        push_to_gateway(self.push_gateway, job=self.job_name, registry=self.registry)
        pass

    def push_gauge_metric(self, name, documentation, value):
        g = Gauge(name, documentation, labels_list, registry=self.registry)
        g.labels(self.service_name, self.pod_name, self.env).set(value)
        push_to_gateway(self.push_gateway, job=self.job_name, registry=self.registry)

    # decorator to meter execution times and add to metrics
    def meter_execution_time(self, func):
        def wrapper(*function_args, **function_kwargs):
            start = datetime.utcnow()
            result = func(*function_args, **function_kwargs)
            end = datetime.utcnow()

            g = Gauge(f'{func.__name__}_duration',
                      f'{func.__name__} duration',
                      labels_list,
                      registry=self.registry)
            g.labels(self.service_name, self.pod_name, self.env).set((end - start).total_seconds())
            push_to_gateway(self.push_gateway, job=self.job_name, registry=self.registry)
            return result

        return wrapper
