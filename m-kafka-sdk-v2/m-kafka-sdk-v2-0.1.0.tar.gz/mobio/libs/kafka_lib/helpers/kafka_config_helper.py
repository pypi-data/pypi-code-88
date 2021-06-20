import os

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

    configs = {}

    def __init__(self):
        self.init_configs()

    def get_producer_by_topic(self, topic):
        producer = None
        _dc = None
        for dc, config in self.configs.items():
            if topic in config.get("topics"):
                producer = config.get("producer")
                _dc = dc
                break
        if not producer:
            producer_config = self.get_producer_config(topic=topic)
            # producer_config_tmp = deepcopy(producer_config)
            producer = Producer(producer_config.get(self.CONFIGS))
            producer_config["producer"] = producer
            if topic not in producer_config.get(self.TOPICS):
                producer_config[self.TOPICS].append(topic)
            self.configs[_dc if _dc else self.MBO_DC] = producer_config
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
                "dc": self.MBO_DC,
                "topics": [],
                "configs": {
                    # "request.timeout.ms": 30000,
                    "bootstrap.servers": KAFKA_BOOTSTRAP,
                },
            }

    def get_config_by_topic(self, topic: object):
        config = None
        for dc, config in self.configs.items():
            if dc != self.MBO_DC and topic in config.get(self.TOPICS):
                config = config
                break
        if not config:
            self.configs[self.MBO_DC][self.TOPICS].append(topic)
        return config

    def get_consumer_config(self, topic, group):
        config = self.get_config_by_topic(topic=topic)
        config[self.CONFIGS]["group.id"] = group
        return config

    def get_producer_config(self, topic):
        return self.get_config_by_topic(topic=topic)
