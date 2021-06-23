import os
from copy import deepcopy

from confluent_kafka.cimpl import Producer
import requests

from mobio.libs.Singleton import Singleton
from mobio.libs.kafka_lib import KAFKA_BOOTSTRAP, MobioEnvironment, lru_cache_kafka


@Singleton
class KafkaConfigHelper:
    TOPICS = "topics"
    DC = "dc"
    CONFIGS = "configs"
    MBO_DC = "mbo_dc"
    PRODUCER = "producer"

    configs = {}

    def __init__(self):
        self.init_configs()

    def get_producer_by_topic(self, topic):
        producer = None
        _dc = None
        for dc, config in self.configs.items():
            if topic in config.get(self.TOPICS):
                producer = config.get(self.PRODUCER)
                _dc = dc
                break
        if not producer:
            _dc = _dc if _dc else self.MBO_DC
            if topic not in self.configs.get(_dc).get(self.TOPICS):
                self.configs[_dc][self.TOPICS].append(topic)
            producer = self.configs.get(_dc).get(self.PRODUCER)
            if not producer:
                producer_config = self.get_producer_config(topic=topic)
                producer = Producer(producer_config)
                producer_config["producer"] = producer
            self.configs[_dc][self.PRODUCER] = producer
        return producer

    @staticmethod
    @lru_cache_kafka.add()
    def get_admin_config():
        try:
            headers = {
                "authorization": "Basic {}".format(os.getenv(MobioEnvironment.YEK_REWOP))
            }
            response = requests.get(
                "{admin_host}/adm/api/v2.1/app-setting".format(
                    admin_host=os.getenv(MobioEnvironment.ADMIN_HOST)
                ), headers=headers
            )
            result = response.json()
            kafka_configs = [x for x in result.get("data") if x.get("type_config") == "listen_kafka"]
        except Exception as ex:
            print("call_admin_to_get_config: {}".format(ex))
            kafka_configs = []
        return kafka_configs

    def init_configs(self):
        kafka_configs = self.get_admin_config()
        for data in kafka_configs:
            try:
                data[self.CONFIGS] = {key.replace("-", "."): value for key, value in data.get(self.CONFIGS).items()}
                if data.get(self.DC) not in self.configs:
                    self.configs[data.get(self.DC)] = data
            except Exception as ex:
                print('parse kafka_configs ERROR: {}'.format(ex))
        if self.MBO_DC not in self.configs:
            self.configs[self.MBO_DC] = {
                self.DC: self.MBO_DC,
                self.TOPICS: [],
                self.CONFIGS: {
                    # "request.timeout.ms": 30000,
                    "bootstrap.servers": KAFKA_BOOTSTRAP,
                },
            }

    def get_config_by_topic(self, topic: object):
        config = None
        for dc, cf in self.configs.items():
            if dc != self.MBO_DC and topic in cf.get(self.TOPICS):
                config = deepcopy(cf[self.CONFIGS])
                break
        if not config:
            config = deepcopy(self.configs[self.MBO_DC][self.CONFIGS])
            if topic not in self.configs[self.MBO_DC][self.TOPICS]:
                self.configs[self.MBO_DC][self.TOPICS].append(topic)
        return config

    def get_consumer_config(self, topic, group):
        config = self.get_config_by_topic(topic=topic)
        config["group.id"] = group
        print("get_consumer_config: {}".format(config))
        return config

    def get_producer_config(self, topic):
        config = self.get_config_by_topic(topic=topic)
        print("get_producer_config: {}".format(config))
        return config
