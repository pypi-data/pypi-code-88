import json
from abc import abstractmethod
from datetime import datetime, timedelta
from confluent_kafka import Consumer

from mobio.libs.kafka_lib import RequeueStatus
from mobio.libs.kafka_lib.helpers.kafka_config_helper import KafkaConfigHelper
from mobio.libs.kafka_lib.models.mongo.requeue_consumer_model import (
    RequeueConsumerModel,
)


class BaseKafkaConsumer:
    def __init__(self, topic: object, group_id: object, client_mongo, retryable=False):
        consumer_config = (
            KafkaConfigHelper()
            .get_consumer_config(topic=topic, group=group_id)
        )
        consumer_config["enable.auto.commit"] = False
        c = Consumer(consumer_config)
        self.client_mongo = client_mongo
        self.retryable = retryable
        c.subscribe([topic])
        self.topic_name = topic
        try:
            print("consume %s is started" % topic)

            while True:
                msg = c.poll(1.0)

                if msg is None:
                    continue
                if msg.error():
                    print("Consumer error: {}".format(msg.error()))
                    continue
                key = msg.key()
                json_obj = json.loads(msg.value().decode("utf-8"))

                self.process(data=json_obj, key=key)
                c.commit()
        except RuntimeError as e:
            print("something unexpected happened: {}".format(topic))
        finally:
            print("consumer is stopped")
            c.close()

    def process(self, data, key=None):
        count_err = 0
        try:
            if "count_err" in data:
                count_err = int(data.pop("count_err"))
            self.message_handle(data=data)
        except Exception as e:
            print("consumer::run - topic: {} ERR: {}".format(self.topic_name, e))
            if data and self.retryable:
                count_err += 1
                data_error = {
                    "topic": self.topic_name,
                    "key": key.decode("ascii") if key else key,
                    "data": data,
                    "error": str(e),
                    "count_err": count_err,
                    "next_run": datetime.utcnow() + timedelta(minutes=5 + count_err),
                    "status": RequeueStatus.ENABLE
                    if count_err <= 10
                    else RequeueStatus.DISABLE,
                }
                result = RequeueConsumerModel(self.client_mongo).insert(data=data_error)
                print("RequeueConsumerModel result: {}".format(result))

    @abstractmethod
    def message_handle(self, data):
        pass
